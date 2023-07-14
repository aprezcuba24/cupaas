from app import command
from app.kafka import pipe


@pipe
async def upload_to_kubernates(data, context):
    logging = context["logging"]
    cupaas_ks8 = data["cupaas_ks8"]
    command_text = f"kubectl apply -f {cupaas_ks8}"
    for item in command.run(command_text):
        logging(item)
    return data
