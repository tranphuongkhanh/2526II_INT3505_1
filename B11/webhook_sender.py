import requests
import json
import hmac
import hashlib

# Cấu hình phải khớp với Server
WEBHOOK_URL = "http://127.0.0.1:5000/api/v1/webhooks/notifications"
WEBHOOK_SECRET = "secret_key"

# Data muốn gửi
payload_dict = {
    "id": "evt_999888",
    "type": "payment.success",
    "data": {
        "user_id": "u_123",
        "amount": 500000
    }
}

# Chuyển thành chuỗi JSON
payload_bytes = json.dumps(payload_dict).encode('utf-8')

# Ký xác thực payload
signature = hmac.new(
    key=WEBHOOK_SECRET.encode('utf-8'),
    msg=payload_bytes,
    digestmod=hashlib.sha256
).hexdigest()

# Gắn chữ ký vào Header
headers = {
    'Content-Type': 'application/json',
    'X-Signature': signature
}

# Gửi HTTP POST
response = requests.post(WEBHOOK_URL, data=payload_bytes, headers=headers)

print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")