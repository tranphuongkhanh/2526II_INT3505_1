import hmac
import hashlib
import json
import threading
from flask import Flask, request, jsonify

app = Flask(__name__)

WEBHOOK_SECRET = "secret_key"

def process_notification_async(event_data):
    """
    Hàm xử lý logic nghiệp vụ trong background.
    """
    event_id = event_data.get("id")
    event_type = event_data.get("type")
    
    print(f"[Background Task] Đang xử lý event {event_id} - Loại: {event_type}...")
    # Mô phỏng thời gian xử lý database hoặc gọi API bên thứ 3
    import time
    time.sleep(2)
    print(f"[Background Task] Hoàn tất xử lý event {event_id}.")

@app.route('/api/v1/webhooks/notifications', methods=['POST'])
def handle_notification_webhook():
    # 1. Lấy raw data để xác thực chữ ký. Bắt buộc dùng raw thay vì request.json
    payload = request.get_data()
    
    # Lấy signature từ header do hệ thống gửi Webhook cung cấp
    signature_header = request.headers.get('X-Signature')

    if not signature_header:
        return jsonify({"error": "Missing X-Signature header"}), 401

    # 2. Tạo mã băm (hash) từ payload nhận được và secret key
    expected_signature = hmac.new(
        key=WEBHOOK_SECRET.encode('utf-8'),
        msg=payload,
        digestmod=hashlib.sha256
    ).hexdigest()

    # 3. So sánh chữ ký an toàn để chống lỗi bảo mật Timing Attack
    if not hmac.compare_digest(expected_signature, signature_header):
        print("Cảnh báo: Phát hiện request Webhook giả mạo hoặc sai Secret Key!")
        return jsonify({"error": "Invalid signature"}), 403

    # 4. Chuyển đổi payload thành JSON an toàn
    try:
        event_data = json.loads(payload)
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format"}), 400

    # 5. Xử lý bất đồng bộ (Tránh Timeout)
    # Khởi tạo một thread mới để xử lý logic, giải phóng HTTP request hiện tại
    task_thread = threading.Thread(target=process_notification_async, args=(event_data,))
    task_thread.start()

    # 6. Trả về 200 OK ngay lập tức cho Provider
    return jsonify({"status": "success", "message": "Webhook received"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)