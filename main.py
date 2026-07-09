from producer.producer import publish_message
from consumer.consumer import consume_message

order = {
    "order_id":101,
    "customer":"Shruthika",
    "amount":2500,
    "status":"CREATED"
}

publish_message(order)

consume_message()