# TypeSec demo
## Cách chạy
cd openapi-comparison/3_TypeSec
npm init -y
### Cài đặt trình biên dịch TypeSpec và bộ chuyển đổi OpenAPI:
npm install @typespec/compiler @typespec/http @typespec/openapi3
### biên dịch ra file OpenAPI
npx tsp compile typesec.tsp --emit @typespec/openapi3
### test file openapi.yaml trong thư mục tsp-output tương tự với openapi demo