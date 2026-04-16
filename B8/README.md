# Cách chạy newman
Cài newman
```
npm install -g newman
npm install -g newman-reporter-htmlextra
```
Chạy và xuất báo cáo trong mục newman
```
cd B8
```
```
newman run postman_collection.json -e postman_environment.json -r "cli,htmlextra"
```
Vào file .html trong newman để xem báo cáo
# Đo hiệu năng
- Dùng locust để đo hiệu năng
- Cài đặt locust
```
pip install locust
```
- Viết kịch bản test vào file locustfile.py
- Chạy ứng dụng
```
python book.py
```
- chạy locust
```
locust
```
- Xem báo cáo hiệu năng trong http://localhost:8089

