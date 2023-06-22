from aiokafka import AIOKafkaProducer
from app.config import KAFKA_HOST


async def get_producer():
    producer = AIOKafkaProducer(bootstrap_servers=KAFKA_HOST)
    await producer.start()
    return producer
