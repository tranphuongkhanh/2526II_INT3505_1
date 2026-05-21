from flask import Flask, request, jsonify

app = Flask(__name__)

# =========================
# EVENT BUS
# =========================

class EventBus:

    def __init__(self):
        self.listeners = {}

    # đăng ký listener
    def subscribe(self, event_name, listener):

        if event_name not in self.listeners:
            self.listeners[event_name] = []

        self.listeners[event_name].append(listener)

    # phát event
    def emit(self, event_name, data):

        print(f"\n[EVENT EMITTED] {event_name}")

        if event_name in self.listeners:

            for listener in self.listeners[event_name]:
                listener(data)


event_bus = EventBus()

# =========================
# LISTENERS
# =========================

def send_email(order):

    print(f"[EMAIL SERVICE]")
    print(f"Send email for order #{order['id']}")

def update_inventory(order):

    print(f"[INVENTORY SERVICE]")
    print(f"Update inventory for product: {order['product']}")

def create_invoice(order):

    print(f"[INVOICE SERVICE]")
    print(f"Create invoice for order #{order['id']}")

# đăng ký listeners
event_bus.subscribe("order.created", send_email)
event_bus.subscribe("order.created", update_inventory)
event_bus.subscribe("order.created", create_invoice)

# =========================
# API
# =========================

@app.route("/orders", methods=["POST"])
def create_order():

    data = request.json

    order = {
        "id": 101,
        "product": data["product"],
        "quantity": data["quantity"]
    }

    print("\n[ORDER SERVICE]")
    print("Create order success")

    # phát event
    event_bus.emit("order.created", order)

    return jsonify({
        "message": "Order created",
        "order": order
    })


if __name__ == "__main__":
    app.run(debug=True)