from flask import Blueprint
from app.extensions import metrics, limiter
from loguru import logger

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return "API is running!"

@main_bp.route('/health')
@metrics.do_not_track()
def health_check():
    return "OK"