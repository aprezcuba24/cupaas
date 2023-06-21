from kafka import KafkaProducer
from app.config import KAFKA_HOST

kafka_producer = KafkaProducer(bootstrap_servers=[KAFKA_HOST])
