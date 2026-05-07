from prometheus_flask_exporter import PrometheusMetrics
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

metrics = PrometheusMetrics.for_app_factory()

# Khởi tạo Rate Limiter
limiter = Limiter(
    key_func=get_remote_address, 
    app=None, 
    default_limits=["100 per 15 minute"],
    storage_uri="memory://"
)