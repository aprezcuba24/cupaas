import asyncio
from app.functions import github_events, git_clone
from app.db import startup_db_client, shutdown_db_client

workers = [github_events, git_clone]


async def main():
    tasks = []
    mongo = startup_db_client()
    context = {
        "mongo": mongo
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
        shutdown_db_client(mongo)

if __name__ == "__main__":
    asyncio.run(main())
