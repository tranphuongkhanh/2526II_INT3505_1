# APIBlueprint demo
## Cách chạy
```bash
npm install -g aglio
cd openapi-comparison/1_APIBlueprint
aglio -i apiblueprint.apib -s -o
```

## Sinh code/test tự động
### Bước 1: Chuyển đổi API Blueprint sang OpenAPI
- sử dụng công cụ CLI có tên là apib2swagger
- cài đặt
```
npm install -g apib2swagger
```
- chuyển đổi
```
apib2swagger -i apiblueprint.apib -o swagger.yaml
```
### Bước 2: Sinh Code Backend từ file OpenAPI
Làm tương tự openapi
```
npx @openapitools/openapi-generator-cli generate -i swagger.yaml -g python-flask -o server
```

```
cd server
pip install -r requirements.txt
```

```
python -m openapi_server
```

Truy cập giao diện: http://127.0.0.1:8080/ui/

## Chạy test
- Cài đặt thư viện hỗ trợ:
```bash
pip install -r test-requirements.txt
```
- Chạy test tự động:
```bash
pytest
```