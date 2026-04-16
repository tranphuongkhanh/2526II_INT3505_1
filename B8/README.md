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
