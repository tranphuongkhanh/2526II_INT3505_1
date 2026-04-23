from flask import Flask
from api.v1.payment_controller import payment_v1_bp
from api.v2.payment_controller import payment_v2_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(payment_v1_bp, url_prefix='/api/v1/payments')
    app.register_blueprint(payment_v2_bp, url_prefix='/api/v2/payments')

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)