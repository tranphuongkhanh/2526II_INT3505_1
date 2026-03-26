from app import app, db
import os

if __name__ == '__main__':
    # Tạo thư mục instance nếu chưa có
    if not os.path.exists('instance'):
        os.makedirs('instance')
        
    # Tạo các bảng trong database dựa trên models.py
    with app.app_context():
        db.create_all()
        
    # Chạy server ở chế độ debug
    app.run(debug=True)