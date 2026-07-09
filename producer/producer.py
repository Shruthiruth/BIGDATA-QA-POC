from queue import Queue
from logger.logger import write_log

# Simulating Kafka Topic
kafka_topic = Queue()

def publish_message(message):
    kafka_topic.put(message)
    write_log("INFO","Producer Published Message")
    write_log("INFO",f"Message: {message}")