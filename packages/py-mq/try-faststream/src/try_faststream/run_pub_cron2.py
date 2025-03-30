import asyncio

from faststream.nats import NatsBroker
from loguru import logger
from rocketry import Rocketry
from rocketry.args import Arg

app = Rocketry(execution="async")

host = "nats://localhost:4222"
broker = NatsBroker(host)  # regular broker
app.params(broker=broker)


async def start_app():
    async with broker:  # connect broker
        await app.serve()  # run rocketry


@app.task("every 2 second", execution="async")
async def publish(br: NatsBroker = Arg("broker")):
    import time

    ts = time.time()
    logger.debug(f"cron publish: {br}, {ts}")
    await br.publish(f"Hi, Rocketry! {ts}", "test")


if __name__ == "__main__":
    asyncio.run(start_app())
