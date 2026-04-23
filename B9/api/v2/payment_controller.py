from flask import Blueprint, request, jsonify
from services.v2.payment_service import process_payment_v2

payment_v2_bp = Blueprint('payment_v2', __name__)

@payment_v2_bp.route('', methods=['POST'])
def create_payment():
    data = request.json

    try:
        result = process_payment_v2(data)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400