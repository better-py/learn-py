import time

from appium import webdriver
from appium.options.android import UiAutomator2Options


def main():
    appium_server_url = 'http://127.0.0.1:4723'
    # command_executor = 'http://0.0.0.0:4723/wd/hub',

    device_id = "1467B513-DCFE-4664-B2C6-6CAD39A55927"  # ios simulator

    #
    # 大麦 app
    #
    app_id = "cn.damai.iphone"
    app_id = "com.a24z.wda"
    app_id = "com.a24z.IntegrationApp"

    # 配置 Appium 服务器和 iOS 设备的能力
    capabilities = {
        'platformName': 'iOS',
        'platformVersion': '15.5',  # 你的设备的 iOS 版本
        # 'deviceName': 'iPhone7',  # 你的设备名称
        'udid': device_id,  # 你的设备 UDID
        'automationName': 'XCUITest',
        'bundleId': app_id,  # 大麦 app 的 bundleId
        'noReset': True,
        "autoAcceptAlerts": "true",
        # "xcodeSigningId": "iPhone Developer",
        # "xcodeOrgId": "your-email-address",
        "showXcodeLog": "true",
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
