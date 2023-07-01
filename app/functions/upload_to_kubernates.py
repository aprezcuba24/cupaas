from app import run_command
from app.kafka import pipe
from app.config import KAFKA_TOPIC_UPLOAD_TO_KUBERNATES, KAFKA_TOPIC_FINAL_URL


@pipe(KAFKA_TOPIC_UPLOAD_TO_KUBERNATES, KAFKA_TOPIC_FINAL_URL)
async def upload_to_kubernates(data, context):
    print("===> upload_to_kubernates", data)
    logging = context["logging"]
    cupaas_ks8 = data["cupaas_ks8"]
    command = f"kubectl apply -f {cupaas_ks8}"
    for item in run_command(command):
        logging(item)
    return data
