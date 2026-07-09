from producer.producer import kafka_topic
from database.database import save_to_database
from validation.validator import validate_order
from logger.logger import write_log

def consume_message():

    if not kafka_topic.empty():

        message = kafka_topic.get()

        write_log("INFO","Consumer Consumed Message")
        
        write_log("INFO",f"Message: {message}")

        # QA Validation
        valid, result = validate_order(message)

        if valid:
            write_log("INFO","Validation Passed")
            save_to_database(message)

        else:
            write_log("ERROR","Validation Failed")

            for error in result:
                write_log("ERROR",error)

        return message

    write_log("INFO","No Messages Available")
    return None