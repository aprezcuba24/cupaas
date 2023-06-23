from app.kafka import pipe
from app.config import KAFKA_TOPIC_GIT_CLONE, KAFKA_TOPIC_CREATE_DOCKER_IMAGE


@pipe(KAFKA_TOPIC_GIT_CLONE, KAFKA_TOPIC_CREATE_DOCKER_IMAGE)
async def git_clone(data, **kwargs):
    print("git_clone", data)
    return data
