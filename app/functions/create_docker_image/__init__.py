from app import command
from app.kafka import pipe
from . import runtimes


@pipe
async def create_docker_image(data, context):
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
    command_text = f"docker build {project_code} -t {image_name} -f {docker_file}"
    for item in command.run(command_text):
        logging(item)
    return data
