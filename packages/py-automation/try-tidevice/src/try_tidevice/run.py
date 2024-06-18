import time

import tidevice
import wda
from tidevice._perf import DataType

app_id = "cn.damai.iphone"
wda.DEBUG = True  # default False
wda.HTTP_TIMEOUT = 60.0  # default 60.0 seconds


def main():
    use_wda()
    # use_tidevice()


def cb(typ, val):
    print(f"iphone app: {typ}, {val}")


def use_wda():
    # c = wda.Client("http://localhost:8200")
    # c = wda.Client()

    #
    # todo x: 核心参数, 自定义
    #
    wda_bundle_id = "com.a24z.wda"

    c = wda.USBClient(wda_bundle_id=wda_bundle_id)
    # c = wda.USBClient(
    #     "f9d3ab4de8ffbc4b188286a9623df43726d5495c",
    #     port=8100,
    #     wda_bundle_id=wda_bundle_id,
    # )

    # 也支持通过DEVICE_URL访问
    # c = wda.Client("usbmux://{udid}:8100".format(udid="f9d3ab4de8ffbc4b188286a9623df43726d5495c"))
    print(c.window_size())

    print(f"iphone window size: {c.window_size()}")

    c.app_start(app_id)

    # s = c.session(app_id)  # 启动应用

    # open app
    # s.app_start(app_id)

    print(f"iphone :{c}, {c.__dict__}")
    # print(c.info)


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
