from flask import Flask, jsonify, request, make_response
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__, static_folder='../static')

SWAGGER_URL = '/docs'
API_URL = '/static/book-api.yaml'

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
    data['id'] = books[-1]['id'] + 1 if books else 1
    books.append(data)
    return jsonify(data), 201

@app.route('/books/<int:id>', methods=['GET'])
def get_book_by_id(id):
    book = next((b for b in books if b['id'] == id), None)
    if book:
        return jsonify(book), 200
    return jsonify({"error": "Không tìm thấy sách"}), 404

@app.route("/books/<int:id>", methods=["PUT"])
def update_book(id):
    book = next((b for b in books if b["id"] == id), None)
    if not book:
        return jsonify({"error": "Không tìm thấy sách"}), 404
    data = request.json
    data['id'] = id
    book.update(data)
    return jsonify(book), 200

@app.route("/books/<int:id>", methods=["PATCH"])
def patch_book(id):
    book = next((b for b in books if b["id"] == id), None)
    if not book:
        return jsonify({"error": "Không tìm thấy sách"}), 404
    data = request.json
    if "status" in data:
        book["status"] = data["status"]
    return jsonify(book), 200

@app.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):
    book = next((b for b in books if b["id"] == id), None)
    if not book:
        return jsonify({"error": "Không tìm thấy sách"}), 404
    books.remove(book)
    return jsonify({"message": "Xóa thành công"}), 204

# if __name__ == "__main__":
#     app.run(debug=True)