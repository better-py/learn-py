import datetime
import os

import ccxt
from loguru import logger


def new_bn_client(api_key, api_secret, use_proxy=True):
    logger.info(f"binance api key {api_key}, secret {api_secret}")

    return ccxt.binance({
        'apiKey': api_key,
        'secret': api_secret,
        'enableRateLimit': True,
        # 'verbose': True,
        'timeout': 4000,  # 4s

        # local proxy:
        #   TODO X: 本地不要使用 HK Proxy, 用 JP/TW Proxy! 否则报 403 Forbidden
        'proxies': {
            'http': 'http://127.0.0.1:7890',
            'https': 'http://127.0.0.1:7890',
        } if use_proxy else None

    })


def try_ccxt():
    ts = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d_%H%M%S')
    logger.add(f"tmp/try_ccxt_{ts}.log")  # todo x: log file

    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_SECRET_KEY")

    logger.info(f"binance api_key: {api_key}, api_secret: {api_secret}")

    if not api_key or not api_secret:
        logger.error("please set BINANCE_API_KEY and BINANCE_SECRET_KEY")
        return

    ex = new_bn_client(api_key, api_secret)

    # get balance:
    # logger.info(f"exchange: {exchange.describe()}")
    res = ex.fetch_balance()

    # logger.info(f"balance: {res}")

    resp = ex.fetch_open_orders(symbol="DOT/FDUSD")
    logger.info(f"open orders: {resp}")

    # order books
    # for symbol in ['BTC/USDT', 'ETH/BTC', 'ETH/USDT']:
    #     ob = exchange.fetch_order_book(symbol, limit=10)
    #     logger.info(f"order book: {ob}")


if __name__ == '__main__':
    try_ccxt()
