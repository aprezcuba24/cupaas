import yaml
import os
from app.kafka import pipe
from app.config import (
    KAFKA_TOPIC_VALIDATE_CONFIGURATION, KAFKA_TOPIC_CREATE_DOCKER_IMAGE
)
from .get_namespace import get_namespace
from .get_docker_configuration import get_docker_configuration
from . import services


def _get_yml_data(data):
    project_code = data["project_code"]
    yml_file = f"{project_code}/.cupaas.yml"
    if not os.path.isfile(yml_file):
        raise RuntimeError("The project does not have .cupaas.yml file.")
    with open(yml_file, "r") as stream:
        return yaml.safe_load(stream)


def _get_configuration(data, yml_data):
    project_name = data["project"]["name"]
    namespace_config, namespace = get_namespace(project_name)
    kubernamtes_config = namespace_config
    environments = {}
    for service in yml_data["services"]:
        key = list(service.keys())[0]
        version = service[key]
        if not hasattr(services, key):
            raise RuntimeError(f"The {service} does not exists.")
        method = getattr(services, key)
        config, env = method(namespace, version)
        environments = {**environments, **env}
        kubernamtes_config += f"\n---\n{config}"
    docker_config, image_name, docker_port = get_docker_configuration(
        namespace,
        project_name,
        data["commit_hash"],
        environments,
    )
    kubernamtes_config += f"\n---\n{docker_config}"
    return kubernamtes_config, image_name, docker_port


def _create_kubernate_file(data, config):
    project_code = data["project_code"]
    cupaas_folder = f"{project_code}/_cupaas"
    os.mkdir(cupaas_folder)
    with open(f"{cupaas_folder}/app.yml", "w") as f:
        f.write(config)
    return cupaas_folder


@pipe(KAFKA_TOPIC_VALIDATE_CONFIGURATION, KAFKA_TOPIC_CREATE_DOCKER_IMAGE)
async def validate_configuration(data, **kwargs):
    print("validate_configuration", data)
    yml_data = _get_yml_data(data)
    config, image_name, docker_port = _get_configuration(data, yml_data)
    cupaas_folder = _create_kubernate_file(data, config)
    return {**data, **{
        "image_name": image_name,
        "docker_port": docker_port,
        "yml_data": yml_data,
        "cupaas_folder": cupaas_folder,
    }}
