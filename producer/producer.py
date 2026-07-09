from kafka.queue_manager import transaction_queue
from logger.logger import write_log


def publish_message(message):
    """
    Simulates Kafka Producer.
    Publishes the transaction into Kafka Topic (Queue).
    """

    transaction_queue.put(message)

    write_log("INFO", "Producer Published Transaction")
    write_log("INFO", f"Message : {message}")