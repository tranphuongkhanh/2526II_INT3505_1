# app/__init__.py
from flask import Flask
from app.extensions import metrics, limiter
from app.logger import setup_logger

from app.routes.main_routes import main_bp

def create_app():
    setup_logger()
    
    app = Flask(__name__)
    
    # Gắn các Extensions vào app
    metrics.init_app(app)
    limiter.init_app(app)
    
    metrics.info('app_info', 'API Monitoring Practice', version='1.0.0')

    # Đăng ký các Routes (Blueprints)
    app.register_blueprint(main_bp)

    return app