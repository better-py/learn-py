# !/usr/bin/env python
# coding: utf-8

"""
Example of how to order spot


todo x:
    - https://github.com/gateio/gatews/blob/master/python/examples/order.py
    - 官方 sdk 示例
    - 下单, 需要 api-key 运行


"""
import asyncio
import logging

from gate_ws import Configuration, Connection, WebSocketResponse
from gate_ws.spot import SpotOrderCancelChannel, SpotOrderPlaceChannel

from os import getenv

logger = logging.getLogger(__name__)


async def callback(_: Connection, response: WebSocketResponse):
    if response.error:
        logger.error("failed to api_request: %s", response.error)

    if response.channel == "spot.login":
        return

    if response.channel == "spot.order_place":
        logger.info("order status: %s", response.result)

    if response.channel == "spot.order_cancel":
        logger.info("order cancel: %s", response.result)


#
# 下单接口参数
#
order_place_param = {
    "text": "t-sssd",
    "currency_pair": "BTC_USDT",
    "type": "limit",
    "account": "spot",
    "side": "buy",
    "iceberg": "0",
    "price": "0.1",  # todo x: 传入一个超低的价格, 是不可能成交的. 不会有风险
    "amount": "0.05",
    "time_in_force": "gtc",
    "auto_borrow": False,
}

#
# 订单取消
#
order_cancel_param = {"currency_pair": "BTC_USDT", "order_id": "1862000415"}

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s: %(message)s")

    api_key = getenv("")
    api_secret = getenv("")  # required

    #
    # api key
    #
    cfg = Configuration(
        api_key="{API_KEY}",  # required
        api_secret="{API_SECRET}",  # required
    )

    conn = Connection(cfg)

    logger.debug(f"exchange config: {cfg}")

    #
    #
    #
    SpotOrderPlaceChannel(conn, callback).api_request(
        order_place_param, "header", "req_id"
    )

    SpotOrderCancelChannel(conn, callback).api_request(
        order_cancel_param, "header", "req_id"
    )

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
