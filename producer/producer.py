from kafka.queue_manager import kafka_topic
from logger.logger import logger


def publish_message(message):
    """
    Simulates Kafka Producer.
    Publishes the transaction into Kafka Topic (Queue).
    """

    kafka_topic.put(message)

    logger.info("Producer Published Transaction")
    logger.info(f"Message : {message}")