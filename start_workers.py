import asyncio
from app.functions import github_events, git_clone

workers = [github_events, git_clone]


async def main():
    tasks = []
    try:
        async with asyncio.TaskGroup() as tg:
            for method in workers:
                t = tg.create_task(method())
                tasks.append(t)
    except asyncio.exceptions.CancelledError:
        for t in tasks:
            t.cancel()

if __name__ == "__main__":
    asyncio.run(main())
