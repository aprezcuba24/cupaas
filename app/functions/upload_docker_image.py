from app.kafka import pipe
from app.config import KAFKA_TOPIC_UPLOAD_DOCKER_IMAGE


@pipe(KAFKA_TOPIC_UPLOAD_DOCKER_IMAGE)
async def upload_docker_image(data, **kwargs):
    print("===> upload_docker_image", data)
