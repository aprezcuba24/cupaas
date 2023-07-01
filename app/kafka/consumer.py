from aiokafka import AIOKafkaConsumer
from app.config import KAFKA_HOST


async def get_consumer(topics):
    consumer = AIOKafkaConsumer(topics, bootstrap_servers=KAFKA_HOST)
    await consumer.start()
    return consumer
