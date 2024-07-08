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
    TODO X: 一条消息, 如果有多个实例, 会多次消费(重复消费)
    """
    logger.debug(f"subscriber: {body}")


@broker.subscriber("test-workers", "workers")
async def to_one(body):
    """
    TODO X: 并发多个 workers 时, 保证一条消息, 只被一个 worker 处理(防止重复消费)
    """
    logger.debug(f"handler: {body}")


@broker.subscriber("key1", kv_watch="bucket")
async def kv_watch(body):
    """
    TODO X: kv watch 示例, 监听 key1 变化, 触发 kv_watch, 会出现重复消费现象!!!
    """
    logger.debug(f"Nats KV Store watch kv(key1, {body})")


@app.after_startup
async def setup_broker():
    """
    TODO X: kv watch 示例, 预选创建 kv bucket
    """
    bk = "bucket"
    kv = await broker.key_value(bucket=bk)
    logger.debug(f"Nats startup hook: create kv bucket: {bk}, {kv}")
    # await kv.put("key1", b"Hello!")


if __name__ == '__main__':
    anyio.run(app.run)
