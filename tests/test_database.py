from database.database import (
    save_transaction,
    get_transaction,
    delete_transaction
)


def test_database_insert():

    transaction = {
        "transaction_id": 9991,
        "account_number": "ACC999",
        "amount": 2500,
        "transaction_type": "DEPOSIT",
        "status": "INITIATED"
    }

    save_transaction(transaction)

    result = get_transaction(9991)

    assert result is not None
    assert result["transaction_id"] == 9991


def test_database_delete():

    deleted = delete_transaction(9991)

    assert deleted is True