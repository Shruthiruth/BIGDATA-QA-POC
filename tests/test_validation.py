import pytest
from validation.validator import validate_transaction


def test_valid_transaction():

    transaction = {
        "transaction_id": 9001,
        "account_number": "ACC001",
        "amount": 5000,
        "transaction_type": "DEPOSIT",
        "status": "INITIATED"
    }

    valid, result = validate_transaction(transaction)

    assert valid is True


def test_negative_amount():

    transaction = {
        "transaction_id": 9002,
        "account_number": "ACC002",
        "amount": -100,
        "transaction_type": "DEPOSIT",
        "status": "INITIATED"
    }

    valid, result = validate_transaction(transaction)

    assert valid is False
    assert "Invalid Amount" in result


def test_invalid_status():

    transaction = {
        "transaction_id": 9003,
        "account_number": "ACC003",
        "amount": 500,
        "transaction_type": "DEPOSIT",
        "status": "PROCESSING"
    }

    valid, result = validate_transaction(transaction)

    assert valid is False
    assert "Invalid Status" in result


@pytest.mark.parametrize(
    "status",
    [
        "DONE",
        "PENDING",
        "ERROR"
    ]
)
def test_multiple_invalid_status(status):

    transaction = {
        "transaction_id": 9004,
        "account_number": "ACC004",
        "amount": 1000,
        "transaction_type": "DEPOSIT",
        "status": status
    }

    valid, result = validate_transaction(transaction)

    assert valid is False