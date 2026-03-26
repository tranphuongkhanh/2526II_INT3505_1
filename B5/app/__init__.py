from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 2. Nạp cấu hình từ file config.py
app.config.from_pyfile('../config.py')

# 3. Khởi tạo Database
db = SQLAlchemy(app)

# 4. Import routes và models
from app import routes, models