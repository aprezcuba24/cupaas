from app.kafka import pipe
from app.config import KAFKA_TOPIC_CREATE_DOCKER_IMAGE


@pipe(KAFKA_TOPIC_CREATE_DOCKER_IMAGE)
async def create_docker_image(data, **kwargs):
    print("create_docker_image", data)
