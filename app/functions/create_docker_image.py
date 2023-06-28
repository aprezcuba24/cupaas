from app import run_command
from app.kafka import pipe
from app.config import KAFKA_TOPIC_CREATE_DOCKER_IMAGE


@pipe(KAFKA_TOPIC_CREATE_DOCKER_IMAGE)
async def create_docker_image(data, **kargs):
    print("create_docker_image =>", data)
    for item in run_command("node only_for_testing/command.js"):
        print(item)
