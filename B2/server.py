from flask import Flask, make_response, request, jsonify
import jwt
import datetime

app = Flask(__name__)

books = []

SECRET_KEY = "secret123"

users = [
    {"username":"admin","password":"123"}
]

@app.route("/login", methods=["POST"])
def login():
    data = request.json

    username = data["username"]
    password = data["password"]

    for u in users:
        if u["username"] == username and u["password"] == password:

            token = jwt.encode(
                {
                    "user": username,
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
                },
                SECRET_KEY,
                algorithm="HS256"
            )

            return jsonify({"token": token})

    return jsonify({"error":"invalid login"}),401

def verify_token():
    auth = request.headers.get("Authorization")

    if not auth:
        return None

    token = auth.split()[1]

    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return data
    except:
        return None

@app.route("/books", methods=["POST"])
def add_book():
    if not verify_token():
        return jsonify({"error":"unauthorized"}),401
    data = request.json
    books.append(data)
    return jsonify(data)

@app.route("/books", methods=["GET"])
def get_books():
    if not verify_token():
        return jsonify({"error":"unauthorized"}),401
    response = make_response(jsonify(books))
    response.headers["Cache-Control"] = "public, max-age=60"
    return response

@app.route("/books/<int:id>", methods=["PUT"])
def update_book(id):
    if not verify_token():
        return jsonify({"error":"unauthorized"}),401
    data = request.json
    for b in books:
        if b["id"] == data["id"]:
            b.update(data)
    return jsonify(books)

@app.route("/books/<int:id>", methods=["PATCH"])
def patch_book(id):
    if not verify_token():
        return jsonify({"error":"unauthorized"}),401
    data = request.json
    for b in books:
        if b["id"] == data["id"]:
            b["status"] = data["status"]
    return jsonify(books)

@app.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):
    if not verify_token():
        return jsonify({"error":"unauthorized"}),401
    data = request.json
    global books
    books = [b for b in books if b["id"] != data["id"]]
    return jsonify(books)

if __name__ == "__main__":
    app.run(debug=True)