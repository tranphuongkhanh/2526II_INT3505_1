from flask import Flask, request, Response
from app.extensions import metrics, limiter
from app.logger import setup_logger
from loguru import logger
from app.routes.main_routes import main_bp

from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

def create_app():
    setup_logger()
    
    app = Flask(__name__)
    
    # Gắn các Extensions vào app
    metrics.init_app(app)
    limiter.init_app(app)
    
    metrics.info('app_info', 'API Monitoring Practice', version='1.0.0')

    # Đăng ký các Routes (Blueprints)
    app.register_blueprint(main_bp)

    @app.route('/metrics')
    def metrics_api():
        # Lấy toàn bộ metrics đang có và trả về dưới định dạng chuẩn của Prometheus
        return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)
    # ---------------------------------------------

    @app.after_request
    def log_response(response):
        if request.path == '/metrics':
            return response
            
        client_ip = request.remote_addr
        method = request.method
        path = request.path
        status = response.status_code
        
        logger.info(f"{client_ip} - {method} {path} - Tình trạng: {status}")
        return response

    return app