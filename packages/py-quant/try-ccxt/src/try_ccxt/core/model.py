import datetime
import pathlib

from loguru import logger
from peewee import *

db_url = pathlib.Path(__file__).parent / "../tmp/binance.db"
db: SqliteDatabase = SqliteDatabase(db_url)

logger.add("../tmp/try_ccxt.log")


class BaseModel(Model):
    class Meta:
        database = db


class BinanceOrder(BaseModel):
    """
    api:
        - /api/v3/myTrades
    """
    id = AutoField()

    # order details
    symbol = CharField(index=True)  # symbol
    price = DecimalField(default=0)  # 价格
    amount = DecimalField(default=0)  # 数量
    cost = DecimalField(default=0)  # 成本
    side = CharField(index=True)  # buy/sell
    taker_or_maker = CharField(index=True)  # taker/maker
    # fee
    fees = TextField(default="[]")  # todo x: json, []

    timestamp = TimestampField(index=True)
    datetime = DateTimeField(default=datetime.datetime.now, index=True)

    # id parts
    bn_id = CharField(index=True)  # todo x: 提供此ID, 是有原因的, 因为 order_id 不唯一!
    order_id = CharField(index=True)  # todo x: 竟然有重复的 order_id!!! 需要另外设计唯一索引
    order_uid = CharField(unique=True)  # todo x: mix(bn_id, order_id) = order_uid

    #
    # all trade info
    #
    info = TextField(default="{}")  # todo x: json, all order info

    class Meta:
        table_name = "binance_order"


class BinanceDao:
    def __init__(self):
        self.tb = BinanceOrder

    def query_orders(self, symbol="DOT/USDT", side="buy"):
        return self.tb.select(
            self.tb.symbol,
            self.tb.price, self.tb.amount, self.tb.cost, self.tb.side, self.tb.datetime
        ).where(symbol == self.tb.symbol, self.tb.side == side)

    def calc_avg_price(self, coin):

        buy = self.calc_raw_avg_price(coin, side="buy")
        sell = self.calc_raw_avg_price(coin, side="sell")

        keep_total_cost = buy["all"]["total_cost"] - sell["all"]["total_cost"]
        keep_total_amount = buy["all"]["total_amount"] - sell["all"]["total_amount"]
        keep_avg_price = keep_total_cost / keep_total_amount

        # total:
        result = {
            "buy": buy,
            "sell": sell,
            "keep": {
                "total_cost": keep_total_cost,
                "total_amount": keep_total_amount,
                "avg_price": keep_avg_price,
            }
        }
        logger.info(f"{coin} keep avg calc: {result}")
        return result

    def calc_raw_avg_price(self, coin: str, side="buy"):
        result = {}
        symbols = [
            f"{coin}/USDT",
            f"{coin}/BUSD",
            f"{coin}/FDUSD",
        ]

        for symbol in symbols:
            qs = self.tb.select(
                fn.SUM(BinanceOrder.amount).alias("total_amount"),
                fn.SUM(BinanceOrder.cost).alias("total_cost"),
            ).where(BinanceOrder.side == side, BinanceOrder.symbol == symbol).get()

            total_amount = qs.total_amount
            total_cost = qs.total_cost

            avg_price = total_cost / total_amount
            result[symbol] = {
                "avg_price": avg_price,
                "total_cost": total_cost,
                "total_amount": total_amount,
            }
            logger.info(
                f"calc {symbol}  avg_price: {avg_price}, total_cost: {total_cost}, total_amount: {total_amount}")

        # calc all avg:
        all_total_cost = 0
        all_total_amount = 0
        for k, v in result.items():
            all_total_cost += v["total_cost"]
            all_total_amount += v["total_amount"]
        all_avg_price = all_total_cost / all_total_amount

        result["all"] = {
            "avg_price": all_avg_price,
            "total_cost": all_total_cost,
            "total_amount": all_total_amount,
        }

        logger.info(f"calc {coin} {side} avg price: {result}")

        return result

    def save_orders(self, orders: list | dict):
        if isinstance(orders, dict):
            for k, v in orders.items():
                logger.debug(f"save orders to db, count: {len(v)}")
                for item in v:
                    self.save_order(**item)
            return

        if isinstance(orders, list):
            logger.debug(f"save orders to db, count: {len(orders)}")
            for item in orders:
                self.save_order(**item)
            return

    def save_order(self, **kwargs):
        result = self.tb.get_or_create(
            symbol=kwargs['symbol'],
            bn_id=kwargs['id'],
            order_id=kwargs['order'],
            order_uid=f"{kwargs['symbol']}_{kwargs['id']}_{kwargs['order']}",
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
        return result


db.connect()
db.create_tables([BinanceOrder, ])
