import asyncio
from app.functions import (
    github_events,
    download_code,
    validate_configuration,
    create_docker_image,
    upload_docker_image,
    upload_to_kubernates,
    get_final_url,
)
from app.db import get_client
from app.logging import logging

pipeline = [
    github_events,
    download_code,
    validate_configuration,
    create_docker_image,
    upload_docker_image,
    upload_to_kubernates,
    get_final_url,
]


def _get_topics(index):
    topic_input = pipeline[index].__name__
    topic_output = (
        pipeline[index + 1].__name__ if index + 1 < len(pipeline) else None
    )
    return topic_input, topic_output


async def main():
    tasks = []
    mongo, mongo_client = get_client()
    context = {
        "mongo": mongo,
        "logging": logging,
    }
    try:
        async with asyncio.TaskGroup() as tg:
            for index, method in enumerate(pipeline):
                topic_input, topic_output = _get_topics(index)
                t = tg.create_task(method(
                    topic_input=topic_input,
                    topic_output=topic_output,
                    context=context,
                ))
                tasks.append(t)
    except asyncio.exceptions.CancelledError:
        for t in tasks:
            t.cancel()
    finally:
        mongo_client.close()

if __name__ == "__main__":
    asyncio.run(main())
