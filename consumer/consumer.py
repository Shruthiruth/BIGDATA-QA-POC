from kafka.queue_manager import transaction_queue
from validation.validator import validate_transaction
from database.database import save_transaction
from logger.logger import write_log


def consume_message():
    """
    Simulates Kafka Consumer.
    Reads transaction from Queue,
    validates it and stores it.
    """

    if transaction_queue.empty():

        write_log("INFO", "No Messages Available")
        return

    message = transaction_queue.get()

    write_log("INFO", "Consumer Received Message")
    write_log("INFO", f"Message : {message}")

    valid, result = validate_transaction(message)

    if valid:

        save_transaction(message)

        write_log("PASS", "Transaction Stored Successfully")

        return True, "Transaction Stored Successfully"

    else:

        write_log("FAIL", f"Validation Failed : {result}")

        return False, result