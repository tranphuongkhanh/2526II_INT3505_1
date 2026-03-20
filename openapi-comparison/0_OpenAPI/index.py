from flask import Flask, jsonify, request, make_response, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

@app.route("/openapi.yaml")
def openapi_spec():
    return send_from_directory(".", "openapi.yaml")

SWAGGER_URL = '/docs'
API_URL = '/openapi.yaml'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Book Management API"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

books = [
    {"id": 1, "title": "Clean Code",    "author": "Robert Martin", "status": "available"},
    {"id": 2, "title": "Dune",           "author": "Frank Herbert", "status": "borrowed"},
    {"id": 3, "title": "Atomic Habits",  "author": "James Clear",   "status": "available"},
]

@app.route("/books", methods=["GET"])
def get_books():
    return jsonify(books), 200

@app.route("/books", methods=["POST"])
def add_book():
    data = request.json

    errors = []
    for field in ("title", "author", "status"):
        if not data or not data.get(field):
            errors.append(f"{field} không được để trống")
    if data and data.get("status") not in ("available", "borrowed", None):
        errors.append("status phải là 'available' hoặc 'borrowed'")
    if errors:
        return jsonify({"success": False, "message": "Dữ liệu không hợp lệ", "errors": errors}), 400

    book = {
        "id": books[-1]['id'] + 1 if books else 1,
        "title": data["title"],
        "author": data["author"],
        "status": data["status"]
    }
    books.append(book)
    return jsonify(book), 201

@app.route('/books/<int:id>', methods=['GET'])
def get_book_by_id(id):
    book = next((b for b in books if b['id'] == id), None)
    if book:
        return jsonify(book), 200
    return jsonify({"success": False, "message": "Không tìm thấy sách với ID này"}), 404

@app.route("/books/<int:id>", methods=["PUT"])
def update_book(id):
    book = next((b for b in books if b["id"] == id), None)
    if not book:
        return jsonify({"success": False, "message": "Không tìm thấy sách với ID này"}), 404
    data = request.json

    errors = []
    if data and data.get("status") not in ("available", "borrowed", None):
        errors.append("status phải là 'available' hoặc 'borrowed'")
    if errors:
        return jsonify({"success": False, "message": "Dữ liệu không hợp lệ", "errors": errors}), 400
    
    book.update(data)
    return jsonify(book), 200

@app.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):
    book = next((b for b in books if b["id"] == id), None)
    if not book:
        return jsonify({"success": False, "message": "Không tìm thấy sách với ID này"}), 404
    books.remove(book)
    return jsonify({"success": True, "message": "Xóa thành công"}), 204

if __name__ == "__main__":
    app.run(debug=True)