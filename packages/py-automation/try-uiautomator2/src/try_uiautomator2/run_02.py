import os
import random
import time

import uiautomator2 as u2

# 调试开关:
debug = True

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

    homepage_popup_id = "cn.damai:id/homepage_popup_window_image"

    #
    #
    #
    star = "周杰伦"
    city = "南京"

    # 打开 app:
    open_damai_app(d)

    # 打开 我的页面, 检查用户是否登录
    open_me_view(d)

    # 搜索 明星 + 城市
    open_search_view(d, star=star, city=city)


def open_damai_app(d, app_package_id="cn.damai"):
    """
    打开 大麦 app
    """
    # 主窗口
    app_activity = app_package_id + ".homepage.MainActivity"
    # 首页随机弹窗页:
    homepage_popup_id = "cn.damai:id/homepage_popup_window_image"

    #
    # 启动大麦 app
    #
    d.app_start(app_package_id, app_activity)

    # 等待 app 启动完成
    d.wait_activity(app_activity, timeout=1)

    # 判断组件是否存在
    if d(resourceId=homepage_popup_id).exists:
        print(f"首页弹窗存在, 关闭掉...")
        # 组件存在，点击
        close_id = "cn.damai:id/homepage_popup_window_close_btn"
        d(resourceId=close_id).click()
    else:
        # 组件不存在，做其他处理
        print("首页弹窗不存在, 忽略...")


def open_search_view(d, star="周杰伦", city="南京"):
    """
    打开搜索页面, 执行搜索动作
    """

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


def open_me_view(d):
    """
    打开我的页面
    """
    me_id = "cn.damai:id/tab_text"
    me_text = "我的"

    # bottom_bar_id = "cn.damai:id/mine_activity_bottomsheet_container"

    # 匹配按钮
    me_btn = d(resourceId=me_id, text=me_text)

    # skip
    if not me_btn.exists:
        print(f"未找到 我的按钮, 页面不正常!!!")
        return

    # find:
    # 获取按钮边界
    bounds = me_btn.info['bounds']

    # bottom_bar = d(resourceId=bottom_bar_id)
    # bottom_bar_bounds = bottom_bar.bounds()
    # top_y = bottom_bar_bounds["top"]
    # bottom_y = bottom_bar_bounds["bottom"]

    # 获取屏幕宽度
    width = d.info["displayWidth"]
    print(f"屏幕宽度: {width}")

    # 计算目标按钮点击范围
    target_width = width / 4
    left_x = int(width - target_width)
    right_x = int(width)

    # 随机生成点击坐标
    x = random.randint(left_x, right_x)
    # y = random.randint(top_y, bottom_y)

    # 计算点击坐标
    # x = (bounds["left"] + bounds["right"]) / 2
    y = (bounds["top"] + bounds["bottom"]) / 2
    y = int(y)
    print(f"点击 我的(随机): {x}, {y}")

    # 点击按钮, 进入我的页面
    d.click(x, y)

    if debug:
        time.sleep(2)

    # 检查是否需要登录
    open_login_view(d)


def open_login_view(d):
    """
    打开登录页面
    """
    # 未登录
    un_auth_id = "cn.damai:id/mine_center_header_user_name"
    un_auth_text = "立即登录"

    it = d(resourceId=un_auth_id, text=un_auth_text)

    if not it.exists:
        print(f"未找到 {un_auth_text}, 用户已经登录!")
        d.press("back")
        return

    # do login:
    it.click()

    #
    # todo x: 暂时未实现
    #

    if debug:
        time.sleep(1)

    # 需要返回 2 次
    d.press("back")
    d.press("back")


def wait_or_buy_tickets():
    pass


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
