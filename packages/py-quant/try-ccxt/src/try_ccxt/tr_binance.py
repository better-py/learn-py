import datetime
import json
import os

import ccxt
from loguru import logger
from peewee import *

db = SqliteDatabase('tmp/binance.db')


class BaseModel(Model):
    class Meta:
        database = db


class BinanceOrder(BaseModel):
    id = AutoField()
    symbol = CharField(index=True)
    order_id = CharField(unique=True)
    side = CharField(index=True)
    price = DecimalField(default=0)
    amount = DecimalField(default=0)
    cost = DecimalField(default=0)
    fee = DecimalField(default=0)
    timestamp = TimestampField(index=True)
    datetime = DateTimeField(default=datetime.datetime.now, index=True)

    class Meta:
        table_name = "binance_order"


db.connect()
db.create_tables([BinanceOrder, ])


class BinanceDao:
    def __init__(self):
        self.tb = BinanceOrder

    def save_order(self, order_id, symbol, **kwargs):
        result = self.tb.get_or_create(
            order_id=order_id,
            symbol=symbol,
            side=kwargs['side'],
            price=kwargs['price'],
            amount=kwargs['amount'],
            cost=kwargs['cost'],
            fee=kwargs['fee'],
            timestamp=kwargs['timestamp'],
            datetime=kwargs['datetime'],
        )
        logger.info(
            f"saved order: order_id={order_id}, symbol={symbol}, datetime={kwargs['datetime']}, count={len(result)}")
        return result


class BinanceTrader:
    def __init__(self, api_key: str = None, api_secret: str = None, use_proxy=True):
        ts = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d_%H%M%S')
        logger.add(f"tmp/try_ccxt_{ts}.log")  # todo x: log file

        self.api_key = api_key or os.getenv("BINANCE_API_KEY")
        self.api_secret = api_secret or os.getenv("BINANCE_SECRET_KEY")

        logger.info(f"binance api_key: {self.api_key}, api_secret: {self.api_secret}")
        if not self.api_key or not self.api_secret:
            logger.error("please set BINANCE_API_KEY and BINANCE_SECRET_KEY")
            return

        self.dao = BinanceDao()
        self.ex = ccxt.binance({
            'apiKey': self.api_key,
            'secret': self.api_secret,
            'enableRateLimit': True,
            # 'verbose': True,
            'timeout': 8000,  # 4s

            # local proxy:
            #   TODO X: 本地不要使用 HK Proxy, 用 JP/TW Proxy! 否则报 403 Forbidden
            'proxies': {
                'http': 'http://127.0.0.1:7890',
                'https': 'http://127.0.0.1:7890',
            } if use_proxy else None
        })

    def get_balance(self):
        res = self.ex.fetch_balance()
        logger.info(f"balance: {res}")
        return res

    def get_trade_history(self, symbol="DOT", since_at="2018-01-01 00:00:00"):

        since = int(datetime.datetime.strptime(since_at, "%Y-%m-%d %H:%M:%S").timestamp() * 1000)
        logger.info(f"fetching trade history since {since_at}, ts:{since}")

        now_at = datetime.datetime.now()
        now_ts = int(now_at.timestamp() * 1000)

        days_30 = 3600000 * 24 * 30  # 30 days
        days_10 = 3600000 * 24 * 10  # 10 days
        duration = days_10

        results = {}
        symbols = [
            "DOT/FDUSD",
            "DOT/USDT",
            "DOT/BUSD",
        ]

        while True:
            since_at = datetime.datetime.fromtimestamp(int(since) / 1000)
            if since >= now_ts:
                break

            for symbol in symbols:
                resp = self.ex.fetch_trades(symbol, since=since, limit=1000)
                if len(resp) == 1000:
                    logger.warning(
                        f"{symbol}, since: {since}, date:{since_at}, may be more than 1000 trades, count: {len(resp)}")

                results[symbol] = resp
                logger.info(f"{symbol} trade history since: {since}, date:{since_at} , count: {len(resp)}")

            # query step:
            since += duration  # last end ts

        return results

    def get_open_orders(self, symbol="DOT/FDUSD"):
        resp = self.ex.fetch_open_orders(symbol=symbol)
        logger.info(f"open orders: {resp}")
        return resp

    def save_orders(self):
        result = self.get_trade_history()
        logger.debug(f"all trades count: {len(result)}")

        with open("tmp/trade_history.json", "w") as f:
            json.dump(result, f)

        for k, v in result.items():
            for item in v:
                self.dao.save_order(
                    order_id=item['id'],
                    symbol=item['symbol'],
                    side=item['side'],
                    price=item['price'],
                    amount=item['amount'],
                    cost=item['cost'],
                    fee=0 if not item['fee'] else item['fee'],
                    timestamp=item['timestamp'],
                    datetime=item['datetime'],
                )


def main():
    db.drop_tables([BinanceOrder, ])
    db.create_tables([BinanceOrder, ])

    bt = BinanceTrader()
    # bt.get_balance()
    # bt.get_open_orders()
    # results = bt.get_trade_history()
    bt.save_orders()


if __name__ == '__main__':
    main()
