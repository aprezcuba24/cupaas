import json
from app.kafka import get_consumer
from app.config import KAFKA_TOPIC_GIT_CLONE


async def git_clone():
    print("git_clone started")
    kafka_consumer = await get_consumer(KAFKA_TOPIC_GIT_CLONE)
    try:
        async for message in kafka_consumer:
            value = json.loads(message.value.decode())
            print("git_clone", value)
    finally:
        await kafka_consumer.stop()
