# try-tidevice

- iOS 自动化控制方案

## Quickstart

- setup:

```bash

task auto:td:setup


```

### Requirements

- python3.8+
- iOS
- macOS

```bash

pip3 install -U "tidevice[openssl]"   # Recommend

# ios 17+
pip install tidevice3


pip install facebook-wda
```    

- 打开 iOS 开发者选项:

```ruby
iOS 16的手机需要手工开启开发者选项。 

开启方法：
  设置->隐私与安全性->开发者模式 （打开），
  然后会提示重启 （点击 重新启动） -> 
  启动后会弹窗 是否打开“开发者模式”？（点击打开）

```

- 安装 WebDriverAgent
    - https://github.com/appium/WebDriverAgent

## References

> projects:

- https://github.com/alibaba/tidevice
    - 支持 iOS 16
- https://github.com/codeskyblue/tidevice3
    - iOS >= 17
- https://github.com/openatx
- https://github.com/openatx/facebook-wda
    - https://pypi.org/project/facebook-wda/

> docs:

- https://appium.io/docs/en/latest/quickstart/install/
    - [安装 driver](https://appium.io/docs/en/latest/ecosystem/drivers/)
- [iOS 真机如何安装 WebDriverAgent](https://testerhome.com/topics/7220)

> appium drivers:

- https://github.com/appium/appium-mac2-driver
- https://github.com/appium/appium-xcuitest-driver

## fix errors

### tidevice pair

- https://github.com/JinjunHan/iOSDeviceSupport/issues/14
- https://github.com/iGhibli/iOS-DeviceSupport


