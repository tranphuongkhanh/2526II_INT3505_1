# RAML demo
## Cách chạy
```bash
npm install -g raml2html
raml2html openapi-comparison/2_RAML/raml.raml > openapi-comparison/2_RAML/index.html
```
* Mở file index.html

## Sinh code/test tự động
### Bước 1: Chuyển RAML sang OpenAPI
- sử dụng công cụ oas-raml-converter
```
cd openapi-comparison/2_RAML
```

```
npx -y oas-raml-converter --from RAML --to OAS30 raml.raml | Out-File -Encoding utf8 swagger.yaml
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