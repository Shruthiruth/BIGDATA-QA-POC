from database.database import read_database


def validate_transaction(transaction):

    errors = []

    existing_transactions = read_database()

    for item in existing_transactions:
        if item["transaction_id"] == transaction["transaction_id"]:
            errors.append("Duplicate Transaction ID")

    if transaction["amount"] <= 0:
        errors.append("Invalid Amount")

    allowed_status = [
        "INITIATED",
        "SUCCESS",
        "FAILED"
    ]

    if transaction["status"] not in allowed_status:
        errors.append("Invalid Status")

    allowed_types = [
        "DEPOSIT",
        "WITHDRAW",
        "TRANSFER"
    ]

    if transaction["transaction_type"] not in allowed_types:
        errors.append("Invalid Transaction Type")

    if errors:
        return False, errors

    return True, "Validation Passed"