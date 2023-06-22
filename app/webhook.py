from fastapi import Request
from app.kafka import send_message
from app.config import KAFKA_TOPIC_GITHUB_EVENT
from app import app


@app.post("/github-webhook")
async def github_webhook(request: Request):
    data = {
        "body": await request.json(),
        "headers": {key: value for key, value in request.headers.items()},
    }
    print("data =>", data)
    await send_message(KAFKA_TOPIC_GITHUB_EVENT, data)
    return {"message": "ok"}
