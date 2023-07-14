from fastapi import Request
from app.kafka import send_message
from app.functions import github_events
from app import app


@app.post("/github-webhook")
async def github_webhook(request: Request):
    data = {
        "body": await request.json(),
        "headers": {key: value for key, value in request.headers.items()},
    }
    print("data =>", data)
    await send_message(github_events.__name__, data)
    return {"message": "ok"}
