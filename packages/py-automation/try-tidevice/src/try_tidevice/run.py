import time

import tidevice
import wda
from tidevice._perf import DataType

app_id = "cn.damai.iphone"


def main():
    use_tidevice()


def cb(typ, val):
    print(f"iphone app: {typ}, {val}")


def use_wda():
    c = wda.Client("http://localhost:8200")

    print(f"iphone :{c}, {c.__dict__}")
    print(c.info)


def pref_info(d):
    # 性能分析
    pref = tidevice.Performance(d, DataType.MEMORY)

    pref.start(app_id, callback=cb)

    time.sleep(10)
    pref.stop()


def use_tidevice():
    d = tidevice.Device()

    print(f"device info: {d.info}, {d.product_type}")

    # pref_info(d)

    d.app_start(app_id)

    time.sleep(10)


if __name__ == '__main__':
    main()
