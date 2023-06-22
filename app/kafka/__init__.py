import json
from .producer import get_producer
from .consumer import get_consumer


async def send_message(topic, data, producer=None):
    producer = producer if producer else await get_producer()
    try:
        await producer.send_and_wait(
            topic, json.dumps(data).encode("ascii")
        )
    finally:
        await producer.stop()


def consumer(topic):
    def decorator(func):
        async def wrapper(*args, **kwargs):
            print(f"{topic} started.")
            kafka_consumer = await get_consumer(topic)
            try:
                async for message in kafka_consumer:
                    value = json.loads(message.value.decode())
                    await func(value, *args, **kwargs)
            finally:
                await kafka_consumer.stop()
        return wrapper
    return decorator
