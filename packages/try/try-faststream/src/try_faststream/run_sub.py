import anyio
from faststream import FastStream
from faststream.nats import NatsBroker
from loguru import logger

host = "nats://localhost:4222"

broker = NatsBroker(host)

app = FastStream(broker)


@broker.subscriber("test")
async def base_handler(body):
    logger.debug(f"subscriber:  {body}")


if __name__ == '__main__':
    anyio.run(app.run)
