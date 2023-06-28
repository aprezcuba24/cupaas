from app.kafka import pipe
from app.config import (
    KAFKA_TOPIC_VALIDATE_CONFIGURATION, KAFKA_TOPIC_CREATE_DOCKER_IMAGE
)


@pipe(KAFKA_TOPIC_VALIDATE_CONFIGURATION, KAFKA_TOPIC_CREATE_DOCKER_IMAGE)
async def validate_configuration(data, **kwargs):
    print("validate_configuration", data)
    return data
