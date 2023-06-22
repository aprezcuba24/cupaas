from app.kafka import send_message, consumer
from app.config import KAFKA_TOPIC_GITHUB_EVENT, KAFKA_TOPIC_GIT_CLONE


@consumer(KAFKA_TOPIC_GITHUB_EVENT)
async def github_events(data):
    print(data)
    data = {
        "git_repository": "dddd"
    }
    await send_message(KAFKA_TOPIC_GIT_CLONE, data)
