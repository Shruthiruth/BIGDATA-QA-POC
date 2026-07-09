from fastapi import FastAPI
from producer.producer import publish_message
from consumer.consumer import consume_message
from .models import Transaction

app = FastAPI()


@app.get("/")
def home():

    return {
        "message": "Big Data QA POC is Running"
    }


@app.post("/transaction")
def create_transaction(transaction: Transaction):

    transaction_data = transaction.model_dump()

    publish_message(transaction_data)

    success, result = consume_message()

    if success:
        return {
        "status": "SUCCESS",
        "message": result
        }

    return {
    "status": "FAILED",
    "errors": result
    }