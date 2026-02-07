# ระบบติดตามการสัญญาของนักการเมืองช่วงหาเสียงเลือกตั้ง

ระบบ MVC สำหรับบันทึกและติดตามคำสัญญาของนักการเมือง

## การติดตั้ง

1. Clone repository หรือดาวน์โหลดโปรเจกต์
2. ติดตั้ง dependencies:

```bash
pip install -r requirements.txt
```

3. สร้างข้อมูลตัวอย่าง (ถ้ายังไม่มี):

```bash
python init_data.py
```

## การรันโปรแกรม

```bash
python app.py
```



## โครงสร้างโปรเจกต์

```
MVC_2_68/
├── app.py                 # ไฟล์หลักของแอปพลิเคชัน
├── models/                # Model classes
│   ├── __init__.py
│   ├── politician.py
│   ├── campaign.py
│   ├── promise.py
│   └── promise_update.py
├── views/                 # View templates (HTML files)
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── all_promises.html
│   ├── promise_detail.html
│   ├── update_progress.html
│   ├── politicians_list.html
│   └── politician.html
├── controllers/           # Controller classes
│   ├── __init__.py
│   └── promise_controller.py
├── data/                  # CSV data files
│   ├── politicians.csv
│   ├── campaigns.csv
│   ├── promises.csv
│   └── promise_updates.csv
└── utils/                 # Utility functions
    ├── __init__.py
    ├── csv_handler.py
    └── constants.py
```

## ข้อมูลผู้ใช้

- **ผู้ใช้ทั่วไป**: username: `user`, password: `user123`
  - ดูข้อมูลได้อย่างเดียว (ไม่สามารถอัปเดตความคืบหน้า)
- **ผู้ดูแลระบบ**: username: `admin`, password: `admin123`
  - ใช้งานได้ทุกอย่าง รวมถึงอัปเดตความคืบหน้า

## ฟีเจอร์หลัก

- ✅ ระบบ Authentication (Login/Logout)
- ✅ แยกสิทธิ์การใช้งาน (User/Admin)
- ✅ ดูคำสัญญาทั้งหมดพร้อมการเรียงลำดับ (ล่าสุด/เก่าสุด)
- ✅ ดูรายละเอียดคำสัญญาพร้อมประวัติการอัปเดต
- ✅ อัปเดตความคืบหน้าคำสัญญา (Admin only)
- ✅ ดูคำสัญญาของนักการเมืองแต่ละคน
- ✅ Business Rules:
  - คำสัญญาสถานะ "เงียบหาย" ไม่สามารถอัปเดตได้
  - คำสัญญา "ยังไม่เริ่ม" จะเปลี่ยนเป็น "กำลังดำเนินการ" อัตโนมัติเมื่อมีการอัปเดต

## เทคโนโลยีที่ใช้

- **Backend**: Python 3.x, Flask
- **Frontend**: HTML, CSS, Jinja2 Templates
- **Database**: CSV Files (simulated database)
- **Architecture**: MVC Pattern

