from flask import Flask, make_response, request, jsonify

app = Flask(__name__)

books = []

API_KEY = "123456"

def check_api_key():
    key = request.headers.get("API-Key")
    return key == API_KEY

@app.route("/books", methods=["POST"])
def add_book():
    if not check_api_key():
        return jsonify({"error": "Invalid API key"}), 401
    data = request.json
    books.append(data)
    return jsonify(data)

@app.route("/books", methods=["GET"])
def get_books():
    if not check_api_key():
        return jsonify({"error": "Invalid API key"}), 401
    response = make_response(jsonify(books))
    response.headers["Cache-Control"] = "public, max-age=60"
    return response

@app.route("/books/<int:id>", methods=["PUT"])
def update_book(id):
    if not check_api_key():
        return jsonify({"error": "Invalid API key"}), 401
    data = request.json
    for b in books:
        if b["id"] == data["id"]:
            b.update(data)
    return jsonify(books)

@app.route("/books/<int:id>", methods=["PATCH"])
def patch_book(id):
    if not check_api_key():
        return jsonify({"error": "Invalid API key"}), 401
    data = request.json
    for b in books:
        if b["id"] == data["id"]:
            b["status"] = data["status"]
    return jsonify(books)

@app.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):
    if not check_api_key():
        return jsonify({"error": "Invalid API key"}), 401
    data = request.json
    global books
    books = [b for b in books if b["id"] != data["id"]]
    return jsonify(books)

if __name__ == "__main__":
    app.run(debug=True)