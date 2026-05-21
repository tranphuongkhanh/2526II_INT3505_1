import time
from flask import Flask, jsonify

# Import OpenTelemetry
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor

# --- 1. CẤU HÌNH OPENTELEMETRY ---
# Tạo Provider và yêu cầu in kết quả Trace ra thẳng màn hình (Console)
provider = TracerProvider()
processor = BatchSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

# Lấy một `tracer` để có thể tự đánh dấu vết thủ công (custom span)
tracer = trace.get_tracer(__name__)

# --- 2. KHỞI TẠO FLASK ---
app = Flask(__name__)

# Tự động gắn Tracing vào Flask (Nó sẽ tự tạo Trace ID cho mọi request gửi đến)
FlaskInstrumentor().instrument_app(app)


# --- 3. CÁC HÀM XỬ LÝ (MÔ PHỎNG) ---
def check_inventory():
    # Bọc hàm này vào một Span con có tên là "db_check_inventory"
    with tracer.start_as_current_span("db_check_inventory"):
        print("Đang kiểm tra kho hàng...")
        time.sleep(0.5) # Giả lập query Database tốn 0.5 giây
        return True

def process_payment():
    # Bọc hàm này vào một Span con có tên là "api_process_payment"
    with tracer.start_as_current_span("api_process_payment"):
        print("Đang xử lý thanh toán...")
        time.sleep(0.8) # Giả lập gọi API ngân hàng tốn 0.8 giây
        return "Success"


# --- 4. API ENDPOINT ---
@app.route('/checkout')
def checkout():
    # Bước 1: Kiểm tra kho (Mất 0.5s)
    if check_inventory():
        # Bước 2: Thanh toán (Mất 0.8s)
        status = process_payment()
        return jsonify({"message": "Đặt hàng thành công!", "payment": status})
        
    return jsonify({"error": "Hết hàng"}), 400


if __name__ == '__main__':
    print("Chạy server Tracing tại http://localhost:8081")
    app.run(port=8081)