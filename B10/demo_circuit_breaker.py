import pybreaker
import requests
from flask import Flask, jsonify

app = Flask(__name__)

# Cấu hình Circuit Breaker: 
# - fail_max = 3: Nếu lỗi 3 lần liên tiếp sẽ NGẮT MẠCH (chuyển sang Open).
# - reset_timeout = 15: Chờ 15 giây sau khi ngắt mới thử kết nối lại (chuyển sang Half-Open).
api_breaker = pybreaker.CircuitBreaker(fail_max=3, reset_timeout=15)

# Hàm gọi API bên thứ 3 được bọc bởi Circuit Breaker
@api_breaker
def call_third_party_api():
    print(">>> Đang thực sự gọi ra bên ngoài (External API)...")
    
    # Dùng httpbin để giả lập một API luôn trả về lỗi 500
    response = requests.get("https://httpbin.org/status/500", timeout=3)
    response.raise_for_status() # Quăng lỗi nếu status code là 4xx, 5xx
    
    return response.json()

@app.route('/buy')
def buy_product():
    try:
        # Gọi hàm đã được bọc circuit breaker
        data = call_third_party_api()
        return jsonify({"message": "Thanh toán thành công!", "data": data})
        
    except pybreaker.CircuitBreakerError:
        # Lỗi này nhảy ra khi mạch ĐÃ BỊ NGẮT (State: OPEN)
        # Hệ thống trả về lỗi ngay lập tức mà không cần tốn thời gian gọi API bên ngoài
        print(">>> Mạch đang OPEN: Chặn request, bảo vệ hệ thống!")
        return jsonify({
            "error": "Cổng thanh toán đang bảo trì, vui lòng thử lại sau!",
            "circuit_state": "OPEN"
        }), 503
        
    except Exception as e:
        # Lỗi này nhảy ra khi API bên ngoài lỗi, nhưng mạch VẪN ĐANG ĐÓNG (State: CLOSED)
        print(">>> Lỗi từ API bên thứ 3!")
        return jsonify({
            "error": "Lỗi xử lý thanh toán từ đối tác.",
            "circuit_state": "CLOSED (Đang ghi nhận lỗi)"
        }), 500

if __name__ == '__main__':
    print("Chạy server tại http://localhost:8080")
    app.run(port=8080)