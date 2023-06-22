from app.kafka import consumer
from app.config import KAFKA_TOPIC_GIT_CLONE


@consumer(KAFKA_TOPIC_GIT_CLONE)
async def git_clone(data, **kwargs):
    print("git_clone", data)
