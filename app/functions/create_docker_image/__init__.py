from app import run_command
from app.kafka import pipe
from app.config import (
    KAFKA_TOPIC_CREATE_DOCKER_IMAGE, KAFKA_TOPIC_UPLOAD_DOCKER_IMAGE
)
from . import runtimes


@pipe(KAFKA_TOPIC_CREATE_DOCKER_IMAGE, KAFKA_TOPIC_UPLOAD_DOCKER_IMAGE)
async def create_docker_image(data, context):
    print("create_docker_image =>", data)
    logging = context["logging"]
    yml_data = data["yml_data"]
    project_code = data["project_code"]
    runtime, version = yml_data["runtime"].split(":")
    if not hasattr(runtimes, runtime):
        raise RuntimeError(f"The runtime is not valid {runtime}")
    method = getattr(runtimes, runtime)
    template = method(
        version,
        data["docker_port"],
        yml_data,
    )
    docker_file = f"{project_code}/_cupaas_Dockerfile"
    with open(docker_file, "w") as f:
        f.write(template)
    image_name = data["image_name"]
    command = f"docker build {project_code} -t {image_name} -f {docker_file}"
    for item in run_command(command):
        logging(item)
    return data
