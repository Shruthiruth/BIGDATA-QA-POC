from database.database import get_orders

def validate_order(order):

    errors = []

    # Mandatory Field Validation
    if not order.get("order_id"):
        errors.append("Order ID is missing")

    if not order.get("customer"):
        errors.append("Customer name is missing")

    if order.get("amount", 0) <= 0:
        errors.append("Amount should be greater than zero")

    if order.get("status") != "CREATED":
        errors.append("Invalid Status")

    # Duplicate Validation
    orders = get_orders()

    for existing_order in orders:

        if existing_order["order_id"] == order["order_id"]:
            errors.append("Duplicate Order ID")
            break

    if errors:
        return False, errors

    return True, ["Validation Passed"]