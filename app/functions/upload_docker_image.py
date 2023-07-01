from app import run_command
from app.kafka import pipe
from app.config import (
    KAFKA_TOPIC_UPLOAD_DOCKER_IMAGE, KAFKA_TOPIC_UPLOAD_TO_KUBERNATES
)


@pipe(KAFKA_TOPIC_UPLOAD_DOCKER_IMAGE, KAFKA_TOPIC_UPLOAD_TO_KUBERNATES)
async def upload_docker_image(data, context):
    print("===> upload_docker_image", data)
    logging = context["logging"]
    image_name = data["image_name"]
    command = f"minikube image load  {image_name}"
    for item in run_command(command):
        logging(item)
    return data
