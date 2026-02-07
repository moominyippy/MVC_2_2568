"""
Main Flask application for Promise Tracking System
Implements MVC pattern with clear separation of concerns
"""
from flask import Flask, render_template, request, redirect, url_for, session, flash
from controllers.promise_controller import PromiseController
from models.promise import Promise
from utils.constants import SORT_DESC, VALID_SORT_ORDERS, ROLE_ADMIN

app = Flask(__name__, template_folder='views')
app.secret_key = 'your-secret-key-here-change-in-production'

# Simple authentication (for demo purposes - should use proper auth in production)
USERS = {
    'admin': {'password': 'admin123', 'role': 'admin'},
    'user': {'password': 'user123', 'role': 'user'}
}

def require_login(f):
    """Decorator to require login for certain routes"""
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            flash('กรุณาเข้าสู่ระบบก่อน', 'error')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function

def require_admin(f):
    """Decorator to require admin role"""
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            flash('กรุณาเข้าสู่ระบบก่อน', 'error')
            return redirect(url_for('login'))
        if session.get('role') != ROLE_ADMIN:
            flash('คุณไม่มีสิทธิ์เข้าถึงหน้านี้', 'error')
            return redirect(url_for('all_promises'))
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function

@app.route('/')
def index():
    """Home page - redirect to promises page"""
    if 'user' not in session:
        return redirect(url_for('login'))
    return redirect(url_for('all_promises'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page"""
    # If already logged in, redirect to promises
    if 'user' in session:
        return redirect(url_for('all_promises'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username in USERS and USERS[username]['password'] == password:
            session['user'] = username
            session['role'] = USERS[username]['role']
            flash('เข้าสู่ระบบสำเร็จ', 'success')
            return redirect(url_for('all_promises'))
        else:
            flash('ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง', 'error')
    
    return render_template('login.html')

@app.route('/logout')
@require_login
def logout():
    """Logout"""
    session.clear()
    return redirect(url_for('login'))

@app.route('/promises')
@require_login
def all_promises():
    """Display all promises page with sorting option"""
    # Validate and get sort order from query parameter
    sort_order = request.args.get('sort', SORT_DESC)
    if sort_order not in VALID_SORT_ORDERS:
        sort_order = SORT_DESC
    
    # Get data through controller (business logic)
    promises = PromiseController.get_all_promises(sort_order)
    
    # Prepare politician data for display
    from models.politician import Politician
    politicians = Politician.get_all()
    politician_dict = {p.politician_id: p for p in politicians}
    
    return render_template('all_promises.html', 
                         promises=promises, 
                         politicians=politician_dict,
                         sort_order=sort_order)

@app.route('/promises/<promise_id>')
@require_login
def promise_detail(promise_id):
    """Display promise detail page with updates history"""
    promise, context = PromiseController.get_promise_detail(promise_id)
    
    if not promise or not context:
        flash('ไม่พบคำสัญญาที่ต้องการ', 'error')
        return redirect(url_for('all_promises'))
    
    return render_template('promise_detail.html',
                         promise=promise,
                         updates=context['updates'],
                         politician=context['politician'])

@app.route('/promises/<promise_id>/update', methods=['GET', 'POST'])
@require_admin
def update_progress(promise_id):
    """Handle promise progress update (admin only)"""
    promise = Promise.get_by_id(promise_id)
    
    if not promise:
        flash('ไม่พบคำสัญญาที่ต้องการ', 'error')
        return redirect(url_for('all_promises'))
    
    if request.method == 'POST':
        progress_details = request.form.get('progress_details', '').strip()
        
        if not progress_details:
            flash('กรุณากรอกรายละเอียดความคืบหน้า', 'error')
            return render_template('update_progress.html', promise=promise)
        
        # Business logic handled by controller
        success, message = PromiseController.update_progress(promise_id, progress_details)
        
        flash(message, 'success' if success else 'error')
        return redirect(url_for('promise_detail', promise_id=promise_id))
    
    return render_template('update_progress.html', promise=promise)

@app.route('/politicians')
@require_login
def politicians_list():
    """Display list of all politicians with promise counts"""
    from models.politician import Politician
    
    politicians = Politician.get_all()
    # Business logic moved to controller
    promise_counts = PromiseController.get_promise_counts_by_politician()
    
    return render_template('politicians_list.html',
                         politicians=politicians,
                         promise_counts=promise_counts)

@app.route('/politicians/<politician_id>')
@require_login
def politician_detail(politician_id):
    """Politician detail page with all promises"""
    politician, promises = PromiseController.get_politician_promises(politician_id)
    
    if not politician:
        flash('ไม่พบข้อมูลนักการเมือง', 'error')
        return redirect(url_for('politicians_list'))
    
    return render_template('politician.html',
                         politician=politician,
                         promises=promises)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

