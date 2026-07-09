from database.database import read_database


def validate_transaction(transaction):

    errors = []

    if not transaction.get("transaction_id"):
        errors.append("Transaction ID Missing")

    if not transaction.get("account_number"):
        errors.append("Account Number Missing")

    if transaction.get("amount", 0) <= 0:
        errors.append("Invalid Amount")

    if transaction.get("status") != "INITIATED":
        errors.append("Invalid Status")

    # NEW VALIDATION
    allowed_types = ["DEPOSIT", "WITHDRAW", "TRANSFER"]

    if transaction.get("transaction_type") not in allowed_types:
        errors.append("Invalid Transaction Type")

    database = read_database()

    for record in database:
        if record["transaction_id"] == transaction["transaction_id"]:
            errors.append("Duplicate Transaction")

    if errors:
        return False, errors

    return True, ["Validation Passed"]