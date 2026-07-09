import json
import os

DB_FILE = "data/orders.json"


def get_orders():

    if not os.path.exists(DB_FILE):
        return []

    with open(DB_FILE, "r") as file:
        return json.load(file)


def save_to_database(order):

    orders = get_orders()

    orders.append(order)

    with open(DB_FILE, "w") as file:
        json.dump(orders, file, indent=4)

    print("✅ Order Stored Successfully")