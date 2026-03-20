# So Sánh Các Chuẩn Tài Liệu Hóa API (API Documentation Standards)

## Bảng So Sánh Tổng Quan

| Tiêu chí | OpenAPI (Swagger) | API Blueprint | RAML | TypeSpec |
| :--- | :--- | :--- | :--- | :--- |
| **Định dạng** | JSON / YAML | Markdown (MSON) | YAML | Cú pháp giống TypeScript |
| **Triết lý** | Toàn diện & Phổ biến | Design-first (Human-centric) | Tái sử dụng & Mô hình hóa | Architecture-as-code |
| **Độ phổ biến** | Rất cao (Industry Standard) | Trung bình | Trung bình (MuleSoft ecosystem) | Đang tăng trưởng mạnh |
| **Khả năng mở rộng** | Rất tốt qua các (Extensions `x-`) | Tốt thông qua các công cụ của bên thứ ba | Rất tốt với Resource Types và Traits | Cực kỳ mạnh mẽ nhờ tính module và trình biên dịch |
| **Đường cong học tập**| Trung bình | Thấp (Dễ học nhất) | Trung bình | Trung bình (Cần biết TypeScript) |

---

## Chi Tiết Từng Công Cụ

### 1. OpenAPI Specification (OAS)
Được biết đến rộng rãi với tên gọi cũ là **Swagger**, đây là tiêu chuẩn vàng trong ngành công nghiệp phần mềm.
* **Ưu điểm:** Hệ sinh thái khổng lồ (Swagger UI, Postman, Insomnia, Code Generators). Hầu hết mọi nền tảng Cloud (AWS, Azure, GCP) đều hỗ trợ mặc định.
* **Nhược điểm:** Cấu trúc YAML/JSON có thể trở nên cực kỳ cồng kềnh và khó quản lý thủ công khi API có hàng trăm endpoint.

### 2. API Blueprint
Sử dụng ngôn ngữ **Markdown** để định nghĩa API, tập trung vào khả năng đọc hiểu của con người.
* **Ưu điểm:** Rất thân thiện với các thành viên phi kỹ thuật (PM, BA). Viết tài liệu giống như viết một bài blog.
* **Nhược điểm:** Công cụ hỗ trợ không còn đa dạng như trước; phụ thuộc nhiều vào hệ sinh thái của Apiary (Oracle).

### 3. RAML (RESTful API Modeling Language)
Được thiết kế dựa trên YAML với mục tiêu tối ưu hóa việc tái sử dụng các thành phần dữ liệu.
* **Ưu điểm:** Mạnh về tính module hóa. Bạn có thể định nghĩa các "Traits" (ví dụ: phân trang, bảo mật) và áp dụng cho nhiều endpoint mà không cần viết lại.
* **Nhược điểm:** Cộng đồng nhỏ hẹp hơn, chủ yếu xoay quanh các doanh nghiệp sử dụng giải pháp của MuleSoft.

### 4. TypeSpec
Một ngôn ngữ mới từ **Microsoft**, cho phép định nghĩa API bằng mã nguồn tương tự như TypeScript, sau đó biên dịch ra OpenAPI hoặc các định dạng khác.
* **Ưu điểm:** Khắc phục nhược điểm "dài dòng" của OpenAPI. Viết ít hơn nhưng tạo ra được nhiều hơn. Kiểm tra lỗi (Validation) ngay khi đang viết.
* **Nhược điểm:** Cần cài đặt trình biên dịch và yêu cầu tư duy lập trình cơ bản.