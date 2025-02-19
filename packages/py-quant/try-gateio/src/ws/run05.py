# !/usr/bin/env python
# coding: utf-8

"""
Example of subscribe tickers


todo x:
    - https://github.com/gateio/gatews/blob/master/python/examples/ticker.py
    - 官方 sdk 示例
    - spot ticker
    - 无需 api-key


"""
import asyncio
from os import getenv

from gate_ws import Configuration, Connection, WebSocketResponse
from gate_ws.spot import SpotOrderChannel
from loguru import logger


async def callback(conn: Connection, response: WebSocketResponse):
    if response.error:
        conn.close()
        raise response.error

    result = response.result
    logger.debug(f"received resp: {response.__dict__}")
    logger.debug(f"received result: {result}")
    assert isinstance(result, dict)


if __name__ == "__main__":

    api_key = getenv("GATEIO_API_KEY")
    api_secret = getenv("GATEIO_API_SECRET")  # required

    logger.debug(f"api key: {api_key}, secret: {api_secret}")

    #
    # api key
    #
    cfg = Configuration(
        api_key=api_key,  # required
        api_secret=api_secret,  # required
    )

    conn = Connection(cfg)

    channel = SpotOrderChannel(conn, callback)
    # channel.subscribe(["!all"])
    channel.subscribe(["BTC_USDT"])

    loop = asyncio.get_event_loop()
    loop.create_task(conn.run())

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        tasks = asyncio.Task.all_tasks(loop)
        for task in tasks:
            task.cancel()
        group = asyncio.gather(*tasks, return_exceptions=True)
        loop.run_until_complete(group)
        loop.close()
