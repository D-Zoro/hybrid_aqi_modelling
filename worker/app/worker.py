import asyncio


async def main() -> None:
    """Entry point for worker jobs.

    In production this would boot Celery/Temporal workers.
    """

    while True:
        # Placeholder: print heartbeat
        print("Worker heartbeat...")
        await asyncio.sleep(60)


if __name__ == "__main__":
    asyncio.run(main())
