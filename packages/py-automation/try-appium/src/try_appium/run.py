import time

from appium import webdriver
from appium.options.android import UiAutomator2Options


def main():
    appium_server_url = 'http://localhost:4723'

    #
    # 大麦 app
    #
    appID = "cn.damai.iphone"

    # 配置 Appium 服务器和 iOS 设备的能力
    capabilities = {
        'platformName': 'iOS',
        'platformVersion': '15.8.2',  # 你的设备的 iOS 版本
        'deviceName': 'HH-iPhone7',  # 你的设备名称
        'udid': 'f9d3ab4de8ffbc4b188286a9623df43726d5495c',  # 你的设备 UDID
        'automationName': 'XCUITest',
        'bundleId': appID,  # 大麦 app 的 bundleId
        'noReset': True,
    }

    # 创建 WebDriver 实例
    driver = webdriver.Remote(
        appium_server_url,
        options=UiAutomator2Options().load_capabilities(capabilities),
    )

    # 等待应用启动
    time.sleep(1)

    # 示例操作：打印当前应用的页面源代码
    page_source = driver.page_source
    print(page_source)

    # 等待 2 秒
    time.sleep(2)

    # 退出测试并关闭应用
    driver.quit()


if __name__ == '__main__':
    main()
