from faststream import FastStream
from faststream.nats import NatsBroker
from loguru import logger
from taskiq.schedule_sources import LabelScheduleSource
from taskiq_faststream import AppWrapper
from taskiq_faststream import StreamScheduler

host = "nats://localhost:4222"
broker = NatsBroker(host)
app = FastStream(broker)


@app.on_startup
async def on_startup():
    logger.debug("on_startup: connecting broker")
    await broker.connect()


@app.on_shutdown
async def on_shutdown():
    logger.debug("on_shutdown: closing broker")
    await broker.close()


# taskiq_broker = BrokerWrapper(broker)
taskiq_broker = AppWrapper(app)


async def gen_cron_data() -> str:
    for i in range(10):
        yield f"cron data {i}"


#
# todo x: 定时任务
#
taskiq_broker.task(
    message=gen_cron_data,
    subject="test-cron",
    schedule=[{
        "cron": "*/2 * * * * *",  # TODO X: 每2秒执行一次
    }],
)

scheduler = StreamScheduler(
    broker=taskiq_broker,
    sources=[LabelScheduleSource(taskiq_broker)],
)
