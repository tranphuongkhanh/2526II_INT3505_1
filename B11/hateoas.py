from flask import Flask, jsonify, request

app = Flask(__name__)

products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 1000
    },
    {
        "id": 2,
        "name": "Phone",
        "price": 500
    }
]

def build_product_response(product):

    return {
        "id": product["id"],
        "name": product["name"],
        "price": product["price"],

        "links": [

            {
                "rel": "self",
                "href": f"/products/{product['id']}",
                "method": "GET"
            },

            {
                "rel": "update",
                "href": f"/products/{product['id']}",
                "method": "PUT"
            },

            {
                "rel": "delete",
                "href": f"/products/{product['id']}",
                "method": "DELETE"
            },

            {
                "rel": "all-products",
                "href": "/products",
                "method": "GET"
            }
        ]
    }

@app.route("/products", methods=["GET"])
def get_products():

    result = []

    for product in products:
        result.append(build_product_response(product))

    return jsonify(result)

@app.route("/products/<int:id>", methods=["GET"])
def get_product(id):

    product = next(
        (p for p in products if p["id"] == id),
        None
    )

    if not product:
        return jsonify({
            "message": "Product not found"
        }), 404

    return jsonify(build_product_response(product))

@app.route("/products", methods=["POST"])
def create_product():

    data = request.json

    product = {
        "id": len(products) + 1,
        "name": data["name"],
        "price": data["price"]
    }

    products.append(product)

    return jsonify(build_product_response(product)), 201

@app.route("/products/<int:id>", methods=["PUT"])
def update_product(id):

    product = next(
        (p for p in products if p["id"] == id),
        None
    )

    if not product:
        return jsonify({
            "message": "Product not found"
        }), 404

    data = request.json

    product["name"] = data.get("name", product["name"])
    product["price"] = data.get("price", product["price"])

    return jsonify(build_product_response(product))

@app.route("/products/<int:id>", methods=["DELETE"])
def delete_product(id):

    global products

    products = [
        p for p in products if p["id"] != id
    ]

    return jsonify({
        "message": "Deleted"
    })

if __name__ == "__main__":
    app.run(debug=True)