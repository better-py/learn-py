import os
import time

from binance.spot import Spot
from loguru import logger


def get_klines():
    client = Spot()

    # Get server timestamp
    logger.debug(f"time: {client.time()}")

    # Get klines of BTCUSDT at 1m interval
    logger.debug(f"kline(BTC/USDT): {client.klines('BTCUSDT', '1m')}")

    # Get last 10 klines of BNBUSDT at 1h interval
    print(client.klines("BNBUSDT", "1h", limit=10))


def get_account():
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET") or os.getenv("BINANCE_SECRET_KEY")

    logger.debug(f"api key: {api_key[:10] if api_key else 'not set'}****************")

    assert api_key and api_secret, "BINANCE_API_KEY and BINANCE_API_SECRET must be set"
    client = Spot(api_key=api_key, api_secret=api_secret)

    ret = client.account()
    for k, v in ret.items():
        if isinstance(v, list):
            for item in v:
                if isinstance(item, dict):
                    if item.get("free") == "0.00000000" and item.get("locked") == "0.00000000":
                        continue
                logger.debug(f"{k}: {item}, type: {type(item)}")
            continue
        logger.debug(f"account info: {k}: {v}")

    # Get account and balance information

    # Post a new order
    # params = {
    #     'symbol': 'BTCUSDT',
    #     'side': 'SELL',
    #     'type': 'LIMIT',
    #     'timeInForce': 'GTC',
    #     'quantity': 0.002,
    #     'price': 9500
    # }

    # response = client.new_order(**params)
    # print(response)


if __name__ == '__main__':
    # write to log file
    logger.add(f"tmp/binance-spot-{time.strftime('%Y%m%d_%H%M%S')}.log")

    get_account()
