from flask import Flask, request, jsonify

app = Flask(__name__)

books = [
    {"bookId": 1, "bookName": "Clean Code",    "auth": "Robert Martin", "stat": "available"},
    {"bookId": 2, "bookName": "Dune",           "auth": "Frank Herbert", "stat": "borrowed"},
    {"bookId": 3, "bookName": "Atomic Habits",  "auth": "James Clear",   "stat": "available"},
]
 
@app.get("/getBooks")
def get_all_books():
    return jsonify(books)
 
@app.get("/GetBookById")
def get_book_by_id():
    book_id = request.args.get("bookId", type=int)
    if book_id is None:
        return jsonify({"err": "bookId is required"}), 400
    book = next((b for b in books if b["bookId"] == book_id), None)
    if not book:       
        return jsonify({"err": "not found"}), 404
    return jsonify(book)

@app.get("/books/borrowed_books")
def get_borrowed():
    result = [b for b in books if b["stat"] == "borrowed"]
    return jsonify(result)
 
@app.post("/createNewBook")
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

@app.delete("/book/<int:book_id>")
def delete_book(book_id):
    book = next((b for b in books if b["bookId"] == book_id), None)
    if not book:
        return jsonify({"err": "not found"}), 404
    books.remove(book)
    return jsonify({"msg": "deleted"})

if __name__ == "__main__":
    app.run(debug=True)
