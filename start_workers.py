import asyncio
from app.functions import github_events, git_clone

workers = [github_events, git_clone]


async def main():
    async with asyncio.TaskGroup() as tg:
        for method in workers:
            tg.create_task(method())

if __name__ == "__main__":
    asyncio.run(main())
