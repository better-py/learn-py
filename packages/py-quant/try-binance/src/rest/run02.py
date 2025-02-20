from binance.cm_futures import CMFutures
from loguru import logger
import os
import time


def get_futures_account():
    # write to log file
    logger.add(f"tmp/binance-futures-{time.strftime('%Y%m%d_%H%M%S')}.log")

    cm_futures_client = CMFutures()

    # get server time
    logger.debug(f"server time: {cm_futures_client.time()}")

    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_SECRET_KEY")

    assert api_key and api_secret

    logger.debug(f"api key: {api_key}, secret: {api_secret}")

    cm_futures_client = CMFutures(key=api_key, secret=api_secret)

    ret = cm_futures_client.account()
    for k, v in ret.items():
        logger.debug(f"\t{k}: {v}")

    logger.debug(f"account info: {ret}")

    # Post a new order
    # params = {
    #     'symbol': 'BTCUSDT',
    #     'side': 'SELL',
    #     'type': 'LIMIT',
    #     'timeInForce': 'GTC',
    #     'quantity': 0.002,
    #     'price': 59808
    # }
    #
    # response = cm_futures_client.new_order(**params)
    # print(response)


if __name__ == '__main__':
    get_futures_account()
