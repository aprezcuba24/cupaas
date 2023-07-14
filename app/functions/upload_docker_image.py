from app import command
from app.kafka import pipe


@pipe
async def upload_docker_image(data, context):
    logging = context["logging"]
    image_name = data["image_name"]
    command_text = f"minikube image load  {image_name}"
    for item in command.run(command_text):
        logging(item)
    return data
