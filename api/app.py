from fastapi import FastAPI,status
from producer.producer import publish_message
from consumer.consumer import consume_message
from .models import Transaction
from database.database import (
    read_database,
    get_transaction,
    delete_transaction
)
app = FastAPI()


@app.get("/")
def home():

    return {
        "message": "Big Data QA POC is Running"
    }


@app.post("/transaction", status_code=status.HTTP_201_CREATED)
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
    
@app.get("/transactions")
def get_all_transactions():
    return read_database()

@app.get("/transaction/{transaction_id}")
def get_single_transaction(transaction_id: int):

    transaction = get_transaction(transaction_id)

    if transaction:
        return transaction

    return {"message": "Transaction Not Found"}

@app.delete("/transaction/{transaction_id}")
def remove_transaction(transaction_id: int):

    deleted = delete_transaction(transaction_id)

    if deleted:
        return {"message": "Transaction Deleted"}

    return {"message": "Transaction Not Found"}