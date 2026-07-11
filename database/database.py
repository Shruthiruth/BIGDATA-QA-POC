from pymongo import MongoClient
from config import MONGO_URI, DATABASE_NAME, COLLECTION_NAME

client = MongoClient(MONGO_URI)

db = client[DATABASE_NAME]

collection = db[COLLECTION_NAME]


def save_transaction(transaction):
    result = collection.insert_one(transaction)
    return result.inserted_id


def read_database():
    return list(collection.find({}, {"_id": 0}))


def get_transaction(transaction_id):
    return collection.find_one(
        {"transaction_id": transaction_id},
        {"_id": 0}
    )


def delete_transaction(transaction_id):
    result = collection.delete_one(
        {"transaction_id": transaction_id}
    )

    return result.deleted_count > 0