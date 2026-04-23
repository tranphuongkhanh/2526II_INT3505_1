# Thông báo ngừng hỗ trợ Payments API v1 và chuyển sang v2
Kính gửi các Developers,

Chúng tôi xin thông báo rằng **Payments API v1** sẽ chính thức bước vào giai đoạn *deprecation* (ngừng hỗ trợ) nhằm nâng cấp hệ thống thanh toán với nhiều cải tiến mới. Phiên bản **Payments API v2** hiện đã sẵn sàng và được khuyến nghị sử dụng cho tất cả các tích hợp mới.

---

### Lịch trình

* **Bắt đầu Deprecation:** 01/05/2026
* **Thời điểm Sunset (ngừng hoạt động hoàn toàn v1):** 31/10/2026

Sau thời điểm này, mọi request tới `/api/v1/payments` sẽ không còn được xử lý.

---

### Những thay đổi chính

Payments API v2 mang đến cấu trúc linh hoạt hơn, hỗ trợ nhiều phương thức thanh toán.

#### Request v1

```json
{
  "amount": 100,
  "currency": "USD"
}
```

#### Request v2

```json
{
  "amount": 100,
  "currency": "USD",
  "paymentMethod": {
    "type": "credit_card"
  }
}
```

---

### Hành động cần thực hiện

* Cập nhật endpoint sang `/api/v2/payments`
* Bổ sung trường `paymentMethod` trong request
* Kiểm thử kỹ trên môi trường staging trước khi deploy production

---

### Tài liệu migration

Chi tiết hướng dẫn nâng cấp có tại:
https://api.example.com/docs/payments/v2-migration

---

### Deprecation Headers

Các response từ API v1 sẽ bao gồm:

```
Deprecation: true
Sunset: Thu, 31 Oct 2026 23:59:59 GMT
```

---

Chúng tôi khuyến nghị bạn hoàn tất việc chuyển đổi sang v2 sớm nhất có thể để đảm bảo hệ thống hoạt động ổn định và không bị gián đoạn.

Trân trọng, 
API Team
