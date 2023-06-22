from app.kafka import send_message, consumer
from app.config import KAFKA_TOPIC_GITHUB_EVENT, KAFKA_TOPIC_GIT_CLONE


@consumer(KAFKA_TOPIC_GITHUB_EVENT)
async def github_events(data, context):
    mongo = context["mongo"]
    body = data["body"]
    project = mongo.get_collection("project").find_one({
        "name": body["repository"]["full_name"],
        "git_source": "github",
        "ref": body["ref"]
    })
    if not project:
        return
    url = body["repository"]["url"]
    ref = project["ref"]
    zip_url = f"{url}/archive/{ref}.zip"
    mongo.get_collection("deploy").insert_one({
        "project_id": project["_id"],
        "data": data,
    })
    project["_id"] = str(project["_id"])
    data = {
        "project": project,
        "zip_url": zip_url,
    }
    await send_message(KAFKA_TOPIC_GIT_CLONE, data)
