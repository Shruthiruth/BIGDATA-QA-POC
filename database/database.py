import json
import os

DATABASE = "data/transactions.json"

os.makedirs("data", exist_ok=True)

if not os.path.exists(DATABASE):
    with open(DATABASE, "w") as file:
        json.dump([], file)


def read_database():

    with open(DATABASE, "r") as file:
        return json.load(file)


def save_transaction(transaction):

    transactions = read_database()

    transactions.append(transaction)

    with open(DATABASE, "w") as file:
        json.dump(transactions, file, indent=4)