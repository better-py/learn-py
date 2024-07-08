import anyio
from faststream import FastStream
from faststream.nats import NatsBroker, PullSub
from faststream.nats import NatsMessage
from loguru import logger

host = "nats://localhost:4222"

broker = NatsBroker(host)

app = FastStream(broker)


@broker.subscriber("test")
async def to_batch(body: str, msg: NatsMessage):
    """
    TODO X: 一条消息, 如果有多个实例, 会多次消费(重复消费)
    """
    logger.debug(f"subscriber batch: {body}")
    logger.debug(f"subscriber batch: msg: {msg}")


@broker.subscriber("test-cron")
async def to_cron(body: str, msg: NatsMessage):
    """
    TODO X: 定时任务
    """
    logger.debug(f"subscriber batch: {body}")
    logger.debug(f"subscriber batch: msg: {msg}")


@broker.subscriber("test-workers", "workers")
async def to_one(body: str, msg: NatsMessage):
    """
    TODO X: 并发多个 workers 时, 保证一条消息, 只被一个 worker 处理(防止重复消费)
    """
    logger.warning(f"subscriber one: body: {body}")
    logger.warning(f"subscriber one: msg: {msg}")


@broker.subscriber(
    subject="test-stream",
    stream="stream",
    pull_sub=PullSub(batch_size=10),
)
async def handle(body, msg: NatsMessage):
    """
    TODO X: pull mode 示例, 批量消费, 一次获取 10条, 非实时, 提升吞吐量
    """
    logger.warning(f"subscriber[pull mode], body: {body}")
    logger.warning(f"subscriber[pull mode], msg: {msg}")


@broker.subscriber("key1", kv_watch="bucket")
async def kv_watch(body: str, msg: NatsMessage):
    """
    TODO X: kv watch 示例, 监听 key1 变化, 触发 kv_watch, 会出现重复消费现象!!!
    """
    logger.debug(f"Nats KV Store watch kv(key1, {body}), msg: {msg}")


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
