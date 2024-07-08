import asyncio

from faststream.nats import NatsBroker
from loguru import logger


async def pub():
    host = "nats://localhost:4222"

    async with NatsBroker(host) as broker:
        msg = "Hi!"
        logger.debug(f"publish message: {msg}")
        await broker.publish(
            msg,
            subject="test",
        )

        #
        # to one worker:
        #
        for i in range(10):
            msg = f"msg {i}"
            logger.debug(f"publish message: {msg}")
            await broker.publish(
                msg,
                subject="test-workers",
            )


if __name__ == '__main__':
    asyncio.run(pub())
