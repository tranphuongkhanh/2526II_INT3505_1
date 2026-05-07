# app/logger.py
import sys
from loguru import logger

def setup_logger():
    # Xóa cấu hình mặc định của loguru để tránh bị in trùng lặp
    logger.remove()
    
    # Cấu hình in log ra Terminal (có màu sắc cho dễ nhìn)
    logger.add(
        sys.stdout, 
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <level>{message}</level>",
        level="INFO"
    )
    
    # Cấu hình ghi log vào file (Lưu tối đa 10MB mỗi file, giữ lại trong 10 ngày)
    logger.add("logs/combined.log", rotation="10 MB", retention="10 days", level="INFO")
    logger.add("logs/error.log", rotation="10 MB", retention="10 days", level="ERROR")