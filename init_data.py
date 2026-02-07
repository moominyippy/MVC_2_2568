"""Script to initialize sample data"""
from models.politician import Politician
from models.campaign import Campaign
from models.promise import Promise
from models.promise_update import PromiseUpdate
import os

def init_sample_data():
    """Initialize sample data"""
    
    # Create data directory
    os.makedirs('data', exist_ok=True)
    
    # 1. Politicians (10 people)
    politicians = [
        Politician('12345678', 'สมชาย ใจดี', 'พรรคเพื่อประชาชน'),
        Politician('23456789', 'สมหญิง รักชาติ', 'พรรคพัฒนาไทย'),
        Politician('34567890', 'วิชัย เก่งมาก', 'พรรคประชาธิปไตย'),
        Politician('45678901', 'มาลี สวยงาม', 'พรรคเพื่อประชาชน'),
        Politician('56789012', 'ประเสริฐ ดีงาม', 'พรรคพัฒนาไทย'),
        Politician('67890123', 'สุรชัย กล้าหาญ', 'พรรคประชาธิปไตย'),
        Politician('78901234', 'นงเยาว์ อ่อนโยน', 'พรรคเพื่อประชาชน'),
        Politician('89012345', 'วิทยา ฉลาดมาก', 'พรรคพัฒนาไทย'),
        Politician('90123456', 'รัตนา สวยใส', 'พรรคประชาธิปไตย'),
        Politician('10234567', 'สมศักดิ์ เข้มแข็ง', 'พรรคเพื่อประชาชน'),
    ]
    Politician.save_all(politicians)
    print(f"Created {len(politicians)} politicians")
    
    # 2. Campaigns
    campaigns = [
        Campaign('CAMP001', '2024', 'เขต 1 กรุงเทพมหานคร'),
        Campaign('CAMP002', '2024', 'เขต 2 กรุงเทพมหานคร'),
        Campaign('CAMP003', '2024', 'เขต 3 กรุงเทพมหานคร'),
        Campaign('CAMP004', '2024', 'เขต 1 เชียงใหม่'),
        Campaign('CAMP005', '2024', 'เขต 1 ขอนแก่น'),
    ]
    Campaign.save_all(campaigns)
    print(f"Created {len(campaigns)} campaigns")
    
    # 3. Promises (25 promises with all statuses)
    promises = [
        # ยังไม่เริ่ม (8 promises)
        Promise('PROM001', '12345678', 'จะสร้างถนนใหม่ในเขตเลือกตั้ง 10 กิโลเมตร', '2024-01-15', Promise.STATUS_NOT_STARTED, 'CAMP001'),
        Promise('PROM002', '23456789', 'จะจัดตั้งศูนย์สุขภาพชุมชน 5 แห่ง', '2024-01-20', Promise.STATUS_NOT_STARTED, 'CAMP002'),
        Promise('PROM003', '34567890', 'จะสร้างสวนสาธารณะขนาดใหญ่ 3 แห่ง', '2024-02-01', Promise.STATUS_NOT_STARTED, 'CAMP003'),
        Promise('PROM004', '45678901', 'จะปรับปรุงระบบน้ำประปาให้ครอบคลุมทุกครัวเรือน', '2024-02-10', Promise.STATUS_NOT_STARTED, 'CAMP001'),
        Promise('PROM005', '56789012', 'จะสร้างโรงเรียนใหม่ 2 แห่ง', '2024-02-15', Promise.STATUS_NOT_STARTED, 'CAMP004'),
        Promise('PROM006', '67890123', 'จะจัดตั้งกองทุนช่วยเหลือผู้สูงอายุ', '2024-02-20', Promise.STATUS_NOT_STARTED, 'CAMP002'),
        Promise('PROM007', '78901234', 'จะสร้างศูนย์กีฬาชุมชน', '2024-03-01', Promise.STATUS_NOT_STARTED, 'CAMP003'),
        Promise('PROM008', '89012345', 'จะปรับปรุงระบบไฟฟ้าให้ทันสมัย', '2024-03-05', Promise.STATUS_NOT_STARTED, 'CAMP005'),
        
        # กำลังดำเนินการ (10 promises)
        Promise('PROM009', '12345678', 'จะสร้างสะพานข้ามแม่น้ำ 2 แห่ง', '2023-12-01', Promise.STATUS_IN_PROGRESS, 'CAMP001'),
        Promise('PROM010', '23456789', 'จะจัดตั้งตลาดนัดชุมชนทุกวันอาทิตย์', '2023-12-10', Promise.STATUS_IN_PROGRESS, 'CAMP002'),
        Promise('PROM011', '34567890', 'จะสร้างห้องสมุดประชาชน 3 แห่ง', '2023-12-15', Promise.STATUS_IN_PROGRESS, 'CAMP003'),
        Promise('PROM012', '45678901', 'จะปรับปรุงระบบขนส่งสาธารณะ', '2023-12-20', Promise.STATUS_IN_PROGRESS, 'CAMP001'),
        Promise('PROM013', '56789012', 'จะสร้างศูนย์ฝึกอาชีพ', '2024-01-05', Promise.STATUS_IN_PROGRESS, 'CAMP004'),
        Promise('PROM014', '67890123', 'จะจัดตั้งกองทุนช่วยเหลือเกษตรกร', '2024-01-10', Promise.STATUS_IN_PROGRESS, 'CAMP002'),
        Promise('PROM015', '78901234', 'จะสร้างโรงพยาบาลชุมชน', '2024-01-15', Promise.STATUS_IN_PROGRESS, 'CAMP003'),
        Promise('PROM016', '89012345', 'จะปรับปรุงระบบอินเทอร์เน็ตให้ครอบคลุม', '2024-01-20', Promise.STATUS_IN_PROGRESS, 'CAMP005'),
        Promise('PROM017', '90123456', 'จะสร้างศูนย์ดูแลเด็กเล็ก', '2024-01-25', Promise.STATUS_IN_PROGRESS, 'CAMP001'),
        Promise('PROM018', '10234567', 'จะจัดตั้งกองทุนช่วยเหลือผู้พิการ', '2024-02-01', Promise.STATUS_IN_PROGRESS, 'CAMP004'),
        Promise('PROM019', '12345678', 'จะสร้างศูนย์วัฒนธรรมชุมชน', '2024-02-05', Promise.STATUS_IN_PROGRESS, 'CAMP001'),
        
        # เงียบหาย (7 promises)
        Promise('PROM020', '23456789', 'จะสร้างสนามบินเล็กในจังหวัด', '2023-11-01', Promise.STATUS_SILENT, 'CAMP002'),
        Promise('PROM021', '34567890', 'จะสร้างโรงงานแปรรูปผลผลิตทางการเกษตร', '2023-11-10', Promise.STATUS_SILENT, 'CAMP003'),
        Promise('PROM022', '45678901', 'จะสร้างศูนย์วิจัยและพัฒนา', '2023-11-15', Promise.STATUS_SILENT, 'CAMP001'),
        Promise('PROM023', '56789012', 'จะสร้างท่าเรือสำหรับการท่องเที่ยว', '2023-11-20', Promise.STATUS_SILENT, 'CAMP004'),
        Promise('PROM024', '67890123', 'จะสร้างศูนย์ประชุมและแสดงสินค้า', '2023-11-25', Promise.STATUS_SILENT, 'CAMP002'),
        Promise('PROM025', '78901234', 'จะสร้างศูนย์บำบัดน้ำเสีย', '2023-12-01', Promise.STATUS_SILENT, 'CAMP003'),
        Promise('PROM026', '89012345', 'จะสร้างศูนย์ฝึกอบรมเทคโนโลยี', '2023-12-05', Promise.STATUS_SILENT, 'CAMP005'),
    ]
    Promise.save_all(promises)
    print(f"Created {len(promises)} promises")
    
    # 4. Promise Updates (some updates for in-progress promises)
    updates = [
        PromiseUpdate('PROM009', '2024-01-15', 'เริ่มสำรวจพื้นที่และออกแบบสะพานแล้ว'),
        PromiseUpdate('PROM009', '2024-02-20', 'ได้รับอนุมัติงบประมาณและเริ่มก่อสร้างแล้ว'),
        PromiseUpdate('PROM010', '2024-01-20', 'จัดหาพื้นที่และเตรียมสถานที่เรียบร้อย'),
        PromiseUpdate('PROM010', '2024-02-10', 'เริ่มเปิดตลาดนัดแล้วทุกวันอาทิตย์'),
        PromiseUpdate('PROM011', '2024-01-25', 'สร้างห้องสมุดแห่งแรกเสร็จแล้ว'),
        PromiseUpdate('PROM011', '2024-02-15', 'กำลังสร้างห้องสมุดแห่งที่ 2 และ 3'),
        PromiseUpdate('PROM012', '2024-02-01', 'กำลังปรับปรุงเส้นทางและเพิ่มรถเมล์'),
        PromiseUpdate('PROM013', '2024-02-05', 'เริ่มเปิดอบรมหลักสูตรแรกแล้ว'),
        PromiseUpdate('PROM014', '2024-02-10', 'จัดตั้งกองทุนและเริ่มรับสมัครสมาชิก'),
        PromiseUpdate('PROM015', '2024-02-20', 'กำลังก่อสร้างอาคารโรงพยาบาล'),
        PromiseUpdate('PROM016', '2024-02-25', 'ติดตั้งเสาสัญญาณในพื้นที่ห่างไกล'),
        PromiseUpdate('PROM017', '2024-03-01', 'เปิดศูนย์ดูแลเด็กเล็กแล้ว'),
        PromiseUpdate('PROM018', '2024-03-05', 'เริ่มจ่ายเงินช่วยเหลือผู้พิการแล้ว'),
        PromiseUpdate('PROM019', '2024-03-10', 'กำลังจัดหาอุปกรณ์และเตรียมสถานที่'),
        
        # Some updates for promises that later became silent
        PromiseUpdate('PROM020', '2023-11-15', 'เริ่มสำรวจพื้นที่'),
        PromiseUpdate('PROM021', '2023-11-20', 'กำลังศึกษาความเป็นไปได้'),
        PromiseUpdate('PROM022', '2023-11-25', 'เริ่มวางแผนโครงการ'),
    ]
    
    # Save updates
    from utils.csv_handler import write_csv
    update_data = [u.to_dict() for u in updates]
    write_csv('promise_updates.csv', update_data, ['promise_id', 'update_date', 'progress_details'])
    print(f"Created {len(updates)} promise updates")
    
    print("\n✅ Sample data initialized successfully!")
    print("\nข้อมูลผู้ใช้:")
    print("  - ผู้ใช้ทั่วไป: username: user, password: user123")
    print("  - ผู้ดูแลระบบ: username: admin, password: admin123")

if __name__ == '__main__':
    init_sample_data()

