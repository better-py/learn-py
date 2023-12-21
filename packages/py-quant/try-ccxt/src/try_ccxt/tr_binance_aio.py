import asyncio

import ccxt.async_support as ccxt  # link against the asynchronous version of ccxt
from loguru import logger


async def try_ccxt():
    logger.info(f'aio exchanges: {ccxt.exchanges}')
    # logger.info(f"exchange: {exchange.describe()}")
    symbols = ['BTC/USDT', 'ETH/BTC', 'ETH/USDT']

    exchange = ccxt.binance(config={
        'timeout': 200000,

        # use local http proxy
        'proxies': {
            'http': 'http://127.0.0.1:7890',
            'https': 'http://127.0.0.1:7890',
        },

        # fuck! proxy 参数非常混乱
        'aiohttp_proxy': 'http://127.0.0.1:7890',

    })
    # markets = await exchange.load_markets()

    for symbol in symbols:
        ob = await exchange.fetch_order_book(symbol, limit=10)
        logger.info(f"order book: {ob}")

    await exchange.close()


if __name__ == '__main__':
    asyncio.run(try_ccxt(), debug=True)
