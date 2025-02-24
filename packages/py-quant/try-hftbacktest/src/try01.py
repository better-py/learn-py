import os

import numpy as np
from hftbacktest import BacktestAsset, HashMapMarketDepthBacktest
from hftbacktest.data.utils import mexc
from numba import njit

"""
ref: https://github.com/nkaz001/hftbacktest/blob/master/examples/example_mexc.py



"""


@njit
def market_making_algo(hbt):
    count = 1
    while hbt.elapse(2.5e8) == 0 and count < 10:
        depth = hbt.depth(0)

        # Prints the best bid and the best offer.
        print(
            'current_timestamp:', hbt.current_timestamp,
            ', best_bid:', np.round(depth.best_bid, 1),
            ', best_ask:', np.round(depth.best_ask, 1)
        )
        count += 1

    return True


if __name__ == '__main__':
    current = os.getcwd()
    print(f"Current: {current}")

    data = mexc.convert(
        input_filename="../tmp/mexc/btcusdt_20250126.gz",
    )

    asset = (
        BacktestAsset()
        .data(data)
        .linear_asset(1.0)
        .power_prob_queue_model(2.0)
        .no_partial_fill_exchange()
        .trading_value_fee_model(-0.00005, 0.0007)
        .tick_size(0.1)
        .lot_size(0.001)
    )

    hbt = HashMapMarketDepthBacktest([asset])
    ret = market_making_algo(hbt)
    print(ret)
