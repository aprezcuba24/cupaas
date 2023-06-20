from flask import jsonify, request
from .app import app


@app.route("/github-webhook", methods=["POST"])
def github_webhook():
    data = request.get_json(force=True)
    print(data)
    return jsonify(message="ok")
