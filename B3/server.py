from flask import Flask, request, jsonify

app = Flask(__name__)

books = [
    {"bookId": 1, "bookName": "Clean Code",    "auth": "Robert Martin", "stat": "available"},
    {"bookId": 2, "bookName": "Dune",           "auth": "Frank Herbert", "stat": "borrowed"},
    {"bookId": 3, "bookName": "Atomic Habits",  "auth": "James Clear",   "stat": "available"},
]
 
@app.get("/books") #lowercase
def get_all_books():
    return jsonify(books)
 
@app.get("/books/<int:book_id>") #lowercase
def get_book_by_id(book_id):
    book = next((b for b in books if b["bookId"] == book_id), None)
    if not book:       
        return jsonify({"err": "not found"}), 404
    return jsonify(book)

@app.get("/books/borrowed-books") #hyphens
def get_borrowed():
    result = [b for b in books if b["stat"] == "borrowed"]
    return jsonify(result)
 
@app.post("/books") #lowercase, plural
def create_book():
    d = request.json or {}
    book = {
        "bookId":   max((b["bookId"] for b in books), default=0) + 1,
        "bookName": d.get("bookName"),
        "auth":     d.get("auth"),
        "stat":     d.get("stat", "available"),
    }
    books.append(book)
    return jsonify(book), 201

@app.delete("/books/<int:book_id>") #plural
def delete_book(book_id):
    book = next((b for b in books if b["bookId"] == book_id), None)
    if not book:
        return jsonify({"err": "not found"}), 404
    books.remove(book)
    return jsonify({"msg": "deleted"})

if __name__ == "__main__":
    app.run(debug=True)
