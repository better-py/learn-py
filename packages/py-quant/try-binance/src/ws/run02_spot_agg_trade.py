# WebSocket Stream Client
from binance.websocket.spot.websocket_stream import SpotWebsocketStreamClient
from loguru import logger
import json
import time


def message_handler(_, message):
    logger.debug(f"ws message: {message}")
    msg = json.loads(message)
    if isinstance(msg, dict):
        for k, v in msg.items():
            if isinstance(v, dict):
                for k1, v1 in v.items():
                    logger.debug(f"\t{k} -> {k1}: {v1}")
                continue
            logger.debug(f"\t{k}: {v}")


def spot_agg_trade():
    proxies = {'http': 'http://1.2.3.4:8080'}
    proxies = {}

    my_client = SpotWebsocketStreamClient(
        on_message=message_handler,
        # proxies=proxies,
        timeout=10)

    # Subscribe to a single symbol stream
    my_client.agg_trade(symbol="bnbusdt")

    time.sleep(10)  # 10s
    logger.info("closing ws connection")
    my_client.stop()


if __name__ == '__main__':
    # write to log file
    logger.add(f"tmp/binance-spot-ws-{time.strftime('%Y%m%d_%H%M%S')}.log")

    spot_agg_trade()
