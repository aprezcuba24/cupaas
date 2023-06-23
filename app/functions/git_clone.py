from app.kafka import pipe
from app.config import KAFKA_TOPIC_GIT_CLONE


@pipe(KAFKA_TOPIC_GIT_CLONE)
async def git_clone(data, **kwargs):
    print("git_clone", data)
