from app import command
from app.kafka import pipe


@pipe
async def get_final_url(data, context):
    logging = context["logging"]
    service_name = data["service_name"]
    namespace = data["namespace"]
    command_text = f"minikube service {service_name} -n {namespace} --url"
    for item in command.run(command_text):
        logging(item)
    return data
