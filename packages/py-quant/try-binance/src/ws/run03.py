# WebSocket Stream Client
import time
from binance.websocket.um_futures.websocket_client import UMFuturesWebsocketClient
from loguru import logger
import json
import time


def message_handler(_, message):
    logger.debug(f"ws message: {message}")
    # msg = json.loads(message)
    # if isinstance(msg, dict):
    #     for k, v in msg.items():
    #         if isinstance(v, dict):
    #             for k1, v1 in v.items():
    #                 logger.debug(f"\t{k} -> {k1}: {v1}")
    #             continue
    #         logger.debug(f"\t{k}: {v}")


def futures_agg_trade(symbol="bnbusdt"):
    my_client = UMFuturesWebsocketClient(on_message=message_handler)
    my_client.agg_trade(symbol=symbol)
    time.sleep(5)
    logger.debug("closing ws connection")
    my_client.stop()


if __name__ == '__main__':
    futures_agg_trade()
