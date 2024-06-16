import os
import random
import time

import uiautomator2 as u2

#
#
#
deviceID = "127.0.0.1:16416"  # android device id
appID = "cn.damai"  # 应用 id


def task(appName):
    device = "127.0.0.1:16416"  # todo x: input your real device
    # set env
    os.environ["ANDROID_SERIAL"] = device

    # d = u2.connect("--serial-here--")  # 只有一个设备也可以省略参数
    d = u2.connect(serial=device)  # 一个设备时, read env-var ANDROID_SERIAL

    print(f"adb connected, device info: {d.device_info}")

    ret = d.app_current()  # 获取前台应用 packageName, activity
    print(f"current: {ret}")


def buy_damai_ticket(d):
    #
    #
    #
    app_package = 'cn.damai'
    app_activity = app_package + ".homepage.MainActivity"
    search_editId = "cn.damai:id/channel_search_text"
    search_btnId = "cn.damai:id/homepage_header_search_btn"
    search_inputId = "cn.damai:id/header_search_v2_input"
    search_resultId = "cn.damai:id/tv_word"

    #
    #
    #
    star = "周杰伦"
    city = "南京"

    # 打开 app:
    open_damai(d)

    # 搜索 明星 + 城市
    search_star(d, star=star, city=city)


def open_damai(d):
    app_package = 'cn.damai'
    app_activity = app_package + ".homepage.MainActivity"

    # 启动大麦 app
    d.app_start(app_package, app_activity)

    # 等待 app 启动完成
    d.wait_activity(app_activity, timeout=1)


def search_star(d, star="周杰伦", city="南京"):
    search_editId = "cn.damai:id/channel_search_text"
    search_btnId = "cn.damai:id/homepage_header_search_btn"
    search_inputId = "cn.damai:id/header_search_v2_input"
    search_keywordId = "cn.damai:id/tv_word"  # 搜索关键词
    search_resultId = "cn.damai:id/tv_project_name"  # 搜索匹配结果列表

    # open search view
    d(resourceId=search_btnId).click()
    # 等待搜索框出现
    d(resourceId=search_inputId).wait(timeout=1)  # todo x: 必须加等待

    # 输入搜索关键词“周杰伦”
    search_input = d(resourceId=search_inputId)
    search_input.send_keys(star)

    time.sleep(1)  # wait 1s

    # 遍历搜索结果列表
    ret_keyword = d(resourceId=search_keywordId)
    print(f"Search keyword count: {ret_keyword.count}")
    for item in ret_keyword:
        # print(f"search result: {item}, {item.info}")
        if item.info['text'] == star:
            item.click()
            break

    #
    # 匹配演唱会结果: (明星+城市)
    #
    d(resourceId=search_resultId).wait(timeout=1)  # todo x: 必须加等待
    ret = d(resourceId=search_resultId)
    print(f"Search result count: {ret.count}")
    for item in ret:
        print(f"search result: {item.info['text']}")
        if star in item.info['text'] and city in item.info['text']:
            print(f"匹配到演唱会: {item.info['text']}, bounds: {item.info['bounds']}")

            # 获取目标组件的父组件
            # p = item.parent()
            p = item

            # 获取父组件的 bounds
            bounds = p.info['bounds']
            left = bounds['left']
            top = bounds['top']
            right = bounds['right']
            bottom = bounds['bottom']
            x_half = (left - right) / 2  # 增加一点偏移, 避开左边的场地信息, 防止误触

            # 计算随机点击位置
            random_x = random.randint(left, right)
            random_y = random.randint(top, bottom)

            print(f"演唱会随机点击坐标: {random_x}, {random_y}")
            # 在随机位置点击
            d.click(random_x, random_y)
            break


def main():
    # set env
    os.environ["ANDROID_SERIAL"] = deviceID

    # d = u2.connect("--serial-here--")  # 只有一个设备也可以省略参数
    d = u2.connect(serial=deviceID)  # 一个设备时, read env-var ANDROID_SERIAL
    print(f"adb connected, device info: {d.device_info}")

    ret = d.app_current()  # 获取前台应用 packageName, activity
    print(f"current: {ret}")

    # app start
    # d.app_start(package_name=appID)
    # app = d.session(package_name=appID)
    # print(f"start app: {appID}, {app.app_info(appID)}")

    #
    # do task:
    #
    buy_damai_ticket(d)

    # 等待搜索结果加载
    time.sleep(5)

    # 关闭大麦 app
    # d.app_stop(app_package)


if __name__ == '__main__':
    main()
