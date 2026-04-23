def process_payment_v2(data):
    amount = data.get("amount")
    currency = data.get("currency")
    payment_method = data.get("paymentMethod")

    if not amount or not currency or not payment_method:
        raise ValueError("Missing required fields")

    method_type = payment_method.get("type")

    if method_type not in ["credit_card", "cash", "paypal"]:
        raise ValueError("Unsupported payment method")

    return {
        "status": "success",
        "amount": amount,
        "currency": currency,
        "paymentMethod": method_type,
        "version": "v2"
    }