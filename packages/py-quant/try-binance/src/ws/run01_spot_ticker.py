# WebSocket API Client
from binance.websocket.spot.websocket_api import SpotWebsocketAPIClient
from loguru import logger
import time
import json


def message_handler(_, message):
    logger.debug(f"ws message: {message}")
    msg = json.loads(message)
    if isinstance(msg, dict):
        for k, v in msg.items():
            if isinstance(v, dict):
                for k1, v1 in v.items():
                    logger.debug(f"\t{k} -> {k1}: {v1}")
                continue
            logger.debug(f"{k}: {v}")


def spot_ticker():
    my_client = SpotWebsocketAPIClient(on_message=message_handler)

    # bnb+USDT:
    my_client.ticker(symbol="BNBUSDT", type="FULL")

    time.sleep(5)
    logger.info("closing ws connection")
    my_client.stop()


if __name__ == '__main__':
    spot_ticker()
