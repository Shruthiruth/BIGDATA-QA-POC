from consumer.consumer import consume_message
import time

print("Consumer Started...\n")

while True:

    consume_message()

    time.sleep(2)