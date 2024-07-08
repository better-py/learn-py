import anyio
from faststream import FastStream
from faststream.nats import NatsBroker
from loguru import logger

host = "nats://localhost:4222"

broker = NatsBroker(host)

app = FastStream(broker)


@broker.subscriber("test")
async def to_batch(body):
    """
    一条消息, 如果有多个实例, 会多次消费(重复消费)
    """
    logger.debug(f"subscriber: {body}")


@broker.subscriber("test-workers", "workers")
async def to_one(body):
    """
    并发多个 workers 时, 保证一条消息, 只被一个 worker 处理(防止重复消费)
    """
    logger.debug(f"handler: {body}")


if __name__ == '__main__':
    anyio.run(app.run)
