from flask import Blueprint, request, jsonify
from services.v1.payment_service import process_payment_v1

payment_v1_bp = Blueprint('payment_v1', __name__)

@payment_v1_bp.route('', methods=['POST'])
def create_payment():
    data = request.json

    try:
        result = process_payment_v1(data)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400