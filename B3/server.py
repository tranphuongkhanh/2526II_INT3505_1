from flask import Flask, request, jsonify

app = Flask(__name__)

books = [
    {"id": 1, "title": "Clean Code",    "author": "Robert Martin", "status": "available"},
    {"id": 2, "title": "Dune",           "author": "Frank Herbert", "status": "borrowed"},
    {"id": 3, "title": "Atomic Habits",  "author": "James Clear",   "status": "available"},
]
 
@app.get("/books") #lowercase
def get_all_books():
    return jsonify(books)
 
@app.get("/books/<int:book_id>") #lowercase
def get_book_by_id(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if not book:       
        # error message chỉ rõ lỗi ID của sách không tồn tại
        return jsonify({"error": f"Book with ID {book_id} not found"}), 404
    return jsonify(book)

@app.get("/books/borrowed-books") #hyphens
def get_borrowed():
    result = [b for b in books if b["stat"] == "borrowed"]
    return jsonify(result)
 
@app.post("/books") #lowercase, plural
def create_book():
    d = request.json or {}
    
    errors = []
    if not d.get("title"):
        errors.append("'title' is required.")
    if not d.get("author"):
        errors.append("'author' is required.")
    if errors:
        return jsonify({"error": "Validation failed.", "fields": errors}), 422
    
    book = {
        "id":   max((b["id"] for b in books), default=0) + 1,
        "title": d.get("title"),
        "author":     d.get("author"),
        "status":     d.get("status", "available"),
    }
    books.append(book)
    return jsonify(book), 201

@app.delete("/books/<int:book_id>") #plural
def delete_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if not book:
        # error message chỉ rõ lỗi ID của sách không tồn tại
        return jsonify({"error": f"Book with ID {book_id} not found"}), 404
    books.remove(book)
    return "", 204 # Xóa xong, không trả về dữ liệu nào, chỉ có status code 204 No Content

if __name__ == "__main__":
    app.run(debug=True)
