import asyncio
import time

from aioclock import AioClock, At, Every, Once, OnShutDown, OnStartUp
from aioclock.group import Group
from faststream.nats import NatsBroker
from loguru import logger

host = "nats://localhost:4222"
broker = NatsBroker(host)  # regular broker

# groups.py
group = Group()


@group.task(trigger=Every(seconds=5))
async def every():
    msg = f"cron one: at {int(time.time())}"
    logger.debug(f"cron one: pub msg: {msg}")

    await broker.publish(
        msg,
        subject="test-cron",
    )


@group.task(trigger=Every(seconds=5))
async def every():
    msg = f"cron batch: at {int(time.time())}"
    logger.debug(f"cron batch, pub msg: {msg}")

    await broker.publish(
        msg,
        subject="test-cron2",
    )


@group.task(trigger=Every(weeks=50))
def even_sync_works():
    logger.debug(f"synchronous task")


@group.task(trigger=At(tz="UTC", hour=0, minute=0, second=0))
async def at():
    logger.debug(f"根据时区世界, 00:00:00 触发")


# @group.task(trigger=Forever())
# async def forever(val: str = Depends(more_useless_than_me)):
#     await asyncio.sleep(2)
#     print("Heartbeat detected. Still not a zombie. Will check again in a bit.")


@group.task(trigger=Once())
async def once():
    logger.debug(f"只触发一次")


# app.py
app = AioClock()
app.include_group(group)


@app.task(trigger=OnStartUp())
async def startup():
    await broker.connect()
    logger.info("定时任务启动!")


@app.task(trigger=OnShutDown())
async def shutdown():
    await broker.close()
    logger.info("定时任务关闭!")


# main.py
if __name__ == "__main__":
    asyncio.run(app.serve())
