from fastapi.testclient import TestClient
from api.app import app

client = TestClient(app)


def test_home():

    response = client.get("/")

    assert response.status_code == 200

    assert response.json()["message"] == "Big Data QA POC is Running"


def test_create_valid_transaction():

    payload = {
        "transaction_id": 3004,
        "account_number": "ACC500",
        "amount": 8000,
        "transaction_type": "DEPOSIT",
        "status": "INITIATED"
    }

    response = client.post("/transaction", json=payload)

    assert response.status_code == 201

    assert response.json()["status"] == "SUCCESS"


def test_invalid_amount():

    payload = {
        "transaction_id": 5002,
        "account_number": "ACC501",
        "amount": -500,
        "transaction_type": "DEPOSIT",
        "status": "INITIATED"
    }

    response = client.post("/transaction", json=payload)

    assert response.status_code == 201

    assert response.json()["status"] == "FAILED"


def test_invalid_transaction_type():

    payload = {
        "transaction_id": 5003,
        "account_number": "ACC502",
        "amount": 2000,
        "transaction_type": "PAYMENT",
        "status": "INITIATED"
    }

    response = client.post("/transaction", json=payload)

    assert response.json()["status"] == "FAILED"