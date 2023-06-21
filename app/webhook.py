import json
from flask import jsonify, request
from app.kafka import kafka_producer
from .app import app


@app.route("/github-webhook", methods=["POST"])
def github_webhook():
    body = request.get_json(force=True)
    headers = {key: value for key, value in request.headers.items()}
    data = {
        "body": body,
        "headers": headers,
    }
    future = kafka_producer.send(
        "github_event", json.dumps(data).encode("ascii")
    )
    record_metadata = future.get(timeout=10)
    print("record_metadata =>", record_metadata)
    print("data =>", data)
    return jsonify(message="ok")
