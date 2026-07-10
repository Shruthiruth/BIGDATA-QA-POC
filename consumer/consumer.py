from kafka.queue_manager import kafka_topic
from validation.validator import validate_transaction
from database.database import save_transaction
from logger.logger import logger


def consume_message():
    """
    Simulates Kafka Consumer.
    Reads transaction from Queue,
    validates it and stores it.
    """

    if kafka_topic.empty():

        logger.info("No Messages Available")

        return False, "No Messages Available"

    message = kafka_topic.get()

    logger.info("Consumer Received Message")
    logger.info(f"Message : {message}")

    valid, result = validate_transaction(message)

    if valid:

        save_transaction(message)

        logger.info("Transaction Stored Successfully")

        return True, "Transaction Stored Successfully"

    else:

        logger.error(f"Validation Failed : {result}")

        return False, result