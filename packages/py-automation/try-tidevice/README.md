# try-tidevice

- iOS 自动化控制方案

## Quickstart

### Requirements

- python3.8+
- iOS
- macOS

```bash

pip3 install -U "tidevice[openssl]"   # Recommend

# ios 17+
pip install tidevice3

```    

- 打开 iOS 开发者选项:

```ruby
iOS 16的手机需要手工开启开发者选项。 

开启方法：
  设置->隐私与安全性->开发者模式 （打开），
  然后会提示重启 （点击 重新启动） -> 
  启动后会弹窗 是否打开“开发者模式”？（点击打开）

```

## References

- https://github.com/alibaba/tidevice
    - 支持 iOS 16
- https://github.com/codeskyblue/tidevice3
    - iOS >= 17 