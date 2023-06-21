import json
from kafka import KafkaConsumer
from app.config import KAFKA_HOST


def main():
    kafka_consumer = KafkaConsumer(
        "github_event", bootstrap_servers=[KAFKA_HOST]
    )
    for message in kafka_consumer:
        value = json.loads(message.value.decode())
        print(type(value), value)
