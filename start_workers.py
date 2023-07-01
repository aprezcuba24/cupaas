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

workers = [
    github_events,
    download_code,
    validate_configuration,
    create_docker_image,
    upload_docker_image,
    upload_to_kubernates,
    get_final_url,
]


async def main():
    tasks = []
    mongo, mongo_client = get_client()
    context = {
        "mongo": mongo,
        "logging": logging,
    }
    try:
        async with asyncio.TaskGroup() as tg:
            for method in workers:
                t = tg.create_task(method(context=context))
                tasks.append(t)
    except asyncio.exceptions.CancelledError:
        for t in tasks:
            t.cancel()
    finally:
        mongo_client.close()

if __name__ == "__main__":
    asyncio.run(main())
