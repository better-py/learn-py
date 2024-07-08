import asyncio

from faststream.nats import NatsBroker


async def pub():
    host = "nats://localhost:4222"

    async with NatsBroker(host) as broker:
        await broker.publish(
            "Hi!",
            subject="test",
        )


if __name__ == '__main__':
    asyncio.run(pub())
