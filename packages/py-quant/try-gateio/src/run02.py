# !/usr/bin/env python
# coding: utf-8

"""
Example of how to get spot balance


todo x:
    - https://www.gate.io/docs/developers/apiv4/ws/zh_CN/#%E7%8E%B0%E8%B4%A7%E4%BD%99%E9%A2%9D%E9%A2%91%E9%81%93
    - 现货余额查询
    - 需要 api-key 运行


"""
import asyncio
import logging

from gate_ws import Configuration, Connection, WebSocketResponse
from gate_ws.spot import SpotBalanceChannel

from os import getenv
from loguru import logger


async def callback(conn: Connection, response: WebSocketResponse):
    if response.error:
        conn.close()
        raise response.error

    result = response.result
    logger.debug(f"received balance update: {result}")
    assert isinstance(result, dict)


#
# 余额查询
#
balance_param = {}

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s: %(message)s")
    api_key = getenv("GATEIO_API_KEY")
    api_secret = getenv("GATEIO_API_SECRET")  # required

    #
    # api key
    #
    cfg = Configuration(
        api_key=api_key,  # required
        api_secret=api_secret,  # required
    )

    conn = Connection(cfg)

    logger.debug(f"exchange config: {cfg}")

    #
    #
    #
    channel = SpotBalanceChannel(conn, callback)
    channel.subscribe()
    # channel.subscribe(["spot.balances"])

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
