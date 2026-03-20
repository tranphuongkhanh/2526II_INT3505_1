# OpenAPI demo
## Cách chạy
* Mở https://editor.swagger.io/
* Paste file openapi.yaml
## Sinh code/test tự động
- Bước 1: đưa bạn vào thư mục chứa file thiết kế API (openapi.yaml): 
`cd openapi-comparison/0_OpenAPI`
- Bước 2: Sinh mã nguồn tự động vào thư mục server: 
`npx @openapitools/openapi-generator-cli generate -i openapi.yaml -g python-flask -o server`
- Bước 3: Cài đặt môi trường:
```cd server
pip install -r requirements.txt
```
- Bước 4: Khởi chạy Server: 
`python -m openapi_server`
- Bước 5: Truy cập giao diện: http://127.0.0.1:8080/ui/
## Chạy test
- Cài đặt thư viện hỗ trợ:
`pip install -r test-requirements.txt`
- Chạy test tự động:
`pytest`
