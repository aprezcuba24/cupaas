from app import run_command
from app.kafka import pipe
from app.config import KAFKA_TOPIC_FINAL_URL


@pipe(KAFKA_TOPIC_FINAL_URL)
async def get_final_url(data, context):
    print("===> upload_docker_image", data)
    logging = context["logging"]
    service_name = data["service_name"]
    namespace = data["namespace"]
    command = f"minikube service {service_name} -n {namespace} --url"
    for item in run_command(command):
        logging(item)
    return data
