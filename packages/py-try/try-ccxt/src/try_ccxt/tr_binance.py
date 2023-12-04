import ccxt
from loguru import logger


def try_ccxt():
    logger.info(f'exchanges: {ccxt.exchanges}')

    exchange = ccxt.binance(config={
        'timeout': 200000,

        # use local http proxy
        'proxies': {
            'http': 'http://127.0.0.1:7890',
            'https': 'http://127.0.0.1:7890',
        }
    })

    # logger.info(f"exchange: {exchange.describe()}")

    # order books
    for symbol in ['BTC/USDT', 'ETH/BTC', 'ETH/USDT']:
        ob = exchange.fetch_order_book(symbol, limit=10)
        logger.info(f"order book: {ob}")


if __name__ == '__main__':
    try_ccxt()
