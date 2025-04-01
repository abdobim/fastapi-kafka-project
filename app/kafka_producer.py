from kafka import KafkaProducer
from app.config import KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC
import json

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def send_message_to_kafka(message: dict):
    producer.send(KAFKA_TOPIC, message)
    producer.flush()
