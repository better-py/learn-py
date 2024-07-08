import asyncio

from faststream.nats import NatsBroker
from loguru import logger


async def pub():
    host = "nats://localhost:4222"

    async with NatsBroker(host) as broker:
        msg = "Hi!"
        logger.debug(f"publish message: {msg}")

        #
        # todo x: 发布一条消息, 会重复消费
        #
        await broker.publish(
            msg,
            subject="test",
        )

        # --------------------------------------------------------------------------

        #
        # todo x: 批量发布, 防止重复消费, to one worker:
        #
        for i in range(10):
            msg = f"msg {i}"
            logger.debug(f"publish message: {msg}")
            await broker.publish(
                msg,
                subject="test-workers",
            )

        # --------------------------------------------------------------------------

        #
        # todo x: kv watch 示例
        #
        bk = "bucket"
        key = 'key1'
        kv = await broker.key_value(bucket=bk)
        for i in range(4):
            msg = f"value: {i}"
            logger.debug(f"Nats KV Store({bk}), put({key}, {msg})")
            await kv.put(key, msg.encode())


if __name__ == '__main__':
    asyncio.run(pub())
