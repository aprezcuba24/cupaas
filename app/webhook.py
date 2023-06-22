import json
from fastapi import Request
from app.kafka import get_producer
from app.config import KAFKA_TOPIC_GITHUB_EVENT
from .app import app


@app.post("/github-webhook")
async def github_webhook(request: Request):
    kafka_producer = await get_producer()
    body = await request.json()
    headers = request.headers
    headers = {key: value for key, value in request.headers.items()}
    data = {
        "body": body,
        "headers": headers,
    }
    print("data =>", data)
    try:
        await kafka_producer.send_and_wait(
            KAFKA_TOPIC_GITHUB_EVENT, json.dumps(data).encode("ascii")
        )
    finally:
        await kafka_producer.stop()
    return {"message": "ok"}
