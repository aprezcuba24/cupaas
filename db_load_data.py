from app.db import get_client


database, client = get_client()
database.get_collection("project").insert_one({
    "name": "aprezcuba24/python-kubernates-example",
    "git_source": "github",
    "ref": "refs/heads/dev",
    "variables": {
        "some_value": "the value"
    }
})
client.close()
