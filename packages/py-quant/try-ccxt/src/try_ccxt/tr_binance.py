import datetime
import json
import os
import time

import ccxt
from loguru import logger
from peewee import *

db = SqliteDatabase('tmp/binance.db')


class BaseModel(Model):
    class Meta:
        database = db


class BinanceOrder(BaseModel):
    """
    api:
        - /api/v3/myTrades
    """
    id = AutoField()

    # id parts
    bn_id = CharField(index=True)  # todo x: 提供此ID, 是有原因的, 因为 order_id 不唯一!
    order_id = CharField(index=True)  # todo x: 竟然有重复的 order_id!!! 需要另外设计唯一索引
    order_uid = CharField(unique=True)  # todo x: mix(bn_id, order_id) = order_uid

    # order details
    symbol = CharField(index=True)  # symbol
    price = DecimalField(default=0)  # 价格
    amount = DecimalField(default=0)  # 数量
    cost = DecimalField(default=0)  # 成本
    side = CharField(index=True)  # buy/sell
    taker_or_maker = CharField(index=True)  # taker/maker
    # fee
    fees = TextField(default="[]")  # todo x: json, []

    #
    # all trade info
    #
    info = TextField(default="{}")  # todo x: json, all order info
    timestamp = TimestampField(index=True)
    datetime = DateTimeField(default=datetime.datetime.now, index=True)

    class Meta:
        table_name = "binance_order"


db.connect()
db.create_tables([BinanceOrder, ])


class BinanceDao:
    def __init__(self):
        self.tb = BinanceOrder

    def save_order(self, **kwargs):
        result = self.tb.get_or_create(
            symbol=kwargs['symbol'],
            bn_id=kwargs['id'],
            order_id=kwargs['order'],
            order_uid=f"{kwargs['id']}_{kwargs['order']}",
            side=kwargs['side'],
            taker_or_maker=kwargs['takerOrMaker'],
            price=kwargs['price'],
            amount=kwargs['amount'],
            cost=kwargs['cost'],
            fees=kwargs['fees'],
            info=kwargs['info'],
            timestamp=kwargs['timestamp'],
            datetime=kwargs['datetime'],
        )
        logger.info(
            f"saved order item: symbol={kwargs['symbol']}, order_id={kwargs['order']}, datetime={kwargs['datetime']}")
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

    def get_open_orders(self, symbol="DOT/FDUSD"):
        resp = self.ex.fetch_open_orders(symbol=symbol)
        logger.info(f"open orders: {resp}")
        return resp

    def get_all_trades(self, symbols: list = None, since_at="2020-05-01 00:00:00"):
        symbols = symbols or [
            "DOT/USDT",
            "DOT/BUSD",
            "DOT/FDUSD",
        ]

        for symbol in symbols:
            results = self.get_trade_history(symbol, since_at)

        return

    def get_trade_history(self, symbol="DOT", start_at="2017-01-01 00:00:00"):
        since = int(datetime.datetime.strptime(start_at, "%Y-%m-%d %H:%M:%S").timestamp() * 1000)
        logger.info(f"fetching trade history since {start_at}, ts:{since}")

        now_at = datetime.datetime.now()
        now_ts = int(now_at.timestamp() * 1000)

        days_1 = 3600000 * 24 * 1  # 1 days
        duration = days_1
        until = since + duration * 40  # end time

        results = []

        while True:
            start_at = datetime.datetime.fromtimestamp(int(since) / 1000)
            end_at = datetime.datetime.fromtimestamp(int(until) / 1000)

            if since >= now_ts:
                break

            while True:
                resp = self.ex.fetch_trades(symbol, since=since, limit=1000, params={
                    'until': until,
                })
                time.sleep(0.1)  # s

                if len(resp) == 0:
                    since = until  # update end

                    logger.info(f"{symbol}, ({start_at}, {end_at}), total:{len(resp)} empty!")
                    break

                # ok!
                if 0 < len(resp) < 1000:
                    self.save_db(resp)
                    results.append(resp)
                    logger.debug(f"{symbol}, ({start_at}, {end_at}) save batch: {resp}, total: {results}")
                    break

                if until < since:
                    logger.error(f"invalid until {until} < since {since}")
                    break

                logger.warning(f"{symbol}, batch: {len(resp)},  ({start_at}, {end_at}) may be more than 1000!")

                #
                # retry!
                #
                until = int(until - duration)
                end_at = datetime.datetime.fromtimestamp(int(until) / 1000)
                logger.warning(f"{symbol}, retry batch ({start_at}, {end_at}), ({since}, {until})")

                # double check
                if since == until:
                    until = int(since + duration / 6)
                    end_at = datetime.datetime.fromtimestamp(int(until) / 1000)
                    logger.error(f"{symbol}, double check: ({start_at}, {end_at}), ({since}, {until})")

            # next step!
            since = until
            until = since + duration * 40  # 40 days
            start_at = datetime.datetime.fromtimestamp(int(since) / 1000)
            end_at = datetime.datetime.fromtimestamp(int(until) / 1000)
            logger.info(f"{symbol}, next step: ({start_at}, {end_at}), total: {len(results)}")

            #
            # double check:
            #

        return results

    def get_my_trades(self, symbol="DOT/USDT"):
        resp = self.ex.fetch_my_trades(symbol=symbol)
        logger.info(f"my trades count: {len(resp)}")
        return resp

    def get_all_my_trades(self, coin="DOT"):
        results = {}
        symbols = [
            f"{coin}/USDT",
            f"{coin}/BUSD",
            f"{coin}/FDUSD",
        ]

        # fetch all
        for symbol in symbols:
            resp = self.ex.fetch_my_trades(symbol=symbol)
            results[symbol] = resp
            logger.info(f"my trades count: {len(resp)}")
        return results

    @staticmethod
    def save_json(orders: dict):
        logger.debug(f"save my trades to json file, count: {len(orders)}")

        now_at = datetime.datetime.now()
        now_ts = int(now_at.timestamp() * 1000)
        filename = f"tmp/trade_history_{now_ts}.json"
        with open(filename, "w") as f:
            json.dump(orders, f)

    @staticmethod
    def read_json(filename):
        with open(filename, "r") as f:
            return json.load(f)

    def save_db(self, orders: list | dict):
        logger.debug(f"save my trades to db, count: {len(orders)}")

        if isinstance(orders, dict):
            for k, v in orders.items():
                self.dao.save_order(**v)
            return

        if isinstance(orders, list):
            for item in orders:
                self.dao.save_order(**item)
            return


def main():
    db.drop_tables([BinanceOrder, ])
    db.create_tables([BinanceOrder, ])

    bt = BinanceTrader()
    # bt.get_balance()
    # bt.get_open_orders()
    # results = bt.get_trade_history()
    # bt.get_all_trades()

    results = bt.get_my_trades()
    bt.save_json(results)
    bt.save_db(results)


if __name__ == '__main__':
    main()
