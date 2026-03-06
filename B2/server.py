from flask import Flask, request, jsonify

app = Flask(__name__)

books = []

@app.route("/books", methods=["POST"])
def add_book():
    data = request.json
    books.append(data)
    return jsonify(data)

@app.route("/books", methods=["GET"])
def get_books():
    return jsonify(books)

@app.route("/books/<int:id>", methods=["PUT"])
def update_book(id):
    data = request.json
    for b in books:
        if b["id"] == data["id"]:
            b.update(data)
    return jsonify(books)

@app.route("/books/<int:id>", methods=["PATCH"])
def patch_book(id):
    data = request.json
    for b in books:
        if b["id"] == data["id"]:
            b["status"] = data["status"]
    return jsonify(books)

@app.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):
    data = request.json
    global books
    books = [b for b in books if b["id"] != data["id"]]
    return jsonify(books)

if __name__ == "__main__":
    app.run(debug=True)