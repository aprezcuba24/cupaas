import json
from app.kafka import get_producer
from app.kafka import get_consumer
from app.config import KAFKA_TOPIC_GITHUB_EVENT, KAFKA_TOPIC_GIT_CLONE


async def github_events():
    print("github_events started")
    kafka_consumer = await get_consumer(KAFKA_TOPIC_GITHUB_EVENT)
    kafka_producer = await get_producer()
    try:
        async for message in kafka_consumer:
            value = json.loads(message.value.decode())
            print(value)
            data = {
                "git_repository": "dddd"
            }
            await kafka_producer.send_and_wait(
                KAFKA_TOPIC_GIT_CLONE, json.dumps(data).encode("ascii")
            )
            print("github_events")
    finally:
        await kafka_consumer.stop()
