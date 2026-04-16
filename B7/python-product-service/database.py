import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

# Kết nối MongoDB
client = MongoClient(os.environ.get("MONGODB_URI", "mongodb://127.0.0.1:27017/"))

# Trỏ tới database tên là 'product_db'
db = client['product_db']

# Trỏ tới collection 'products'
products_collection = db['products']