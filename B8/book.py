import math

from flask import Flask, request, jsonify

app = Flask(__name__)

books = [
    {"id": 1, "title": "Clean Code",    "author": "Robert Martin", "status": "available"},
    {"id": 2, "title": "Dune",           "author": "Frank Herbert", "status": "borrowed"},
    {"id": 3, "title": "Atomic Habits",  "author": "James Clear",   "status": "available"},
]

@app.route("/books", methods=["GET"])
def get_books():
    # return jsonify(books), 200
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    start = (page - 1) * per_page
    end = start + per_page
    paginated_books = books[start:end]

    response = {
        "metadata": {
            "total_records": len(books),
            "current_page": page,
            "per_page": per_page,
            "total_pages": math.ceil(len(books) / per_page)
        },
        "data": paginated_books
    }
    return jsonify(response), 200

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

if __name__ == "__main__":
    app.run(debug=True)