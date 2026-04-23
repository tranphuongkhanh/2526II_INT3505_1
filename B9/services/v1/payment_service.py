def process_payment_v1(data):
    amount = data.get("amount")
    currency = data.get("currency")

    if not amount or not currency:
        raise ValueError("Missing amount or currency")

    # giả lập xử lý thanh toán
    return {
        "status": "success",
        "amount": amount,
        "currency": currency,
        "version": "v1"
    }