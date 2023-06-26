from app.kafka import pipe
from app.config import KAFKA_TOPIC_VALIDATE_CONFIGURATION


@pipe(KAFKA_TOPIC_VALIDATE_CONFIGURATION)
async def validate_configuration(data, **kwargs):
    print("validate_configuration", data)
