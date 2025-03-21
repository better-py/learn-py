# vnpy

- 量化交易框架
- https://github.com/vnpy/vnpy

## 策略模块

- 价差交易: https://github.com/vnpy/vnpy_spreadtrading
- 期权波动率交易: https://github.com/vnpy/vnpy_optionmaster
- https://github.com/vnpy/vnpy_portfoliostrategy
- https://github.com/vnpy/vnpy_algotrading
- https://github.com/vnpy/vnpy_scripttrader
- https://github.com/vnpy/vnpy_riskmanager

## Development

### Requirements

- vnpy 包很大, 基于 PyQt(pyside6==6.8.2.1) 实现了 GUI 的策略开发环境.

```ruby
# 安装依赖
brew install ta-lib 

# 安装包依赖
uv add ta-lib numpy
uv add vnpy vnpy_ctastrategy vnpy_ctabacktester vnpy_datamanager vnpy_sqlite vnpy_rqdata   

```

### Run

- 运行示例, 会显示 vnpy 的图形化界面(基于 Qt(pyside6) 实现)

```ruby

cd git-repo-root-dir/
  
# run 
task quant:vn:r -- try01.py

   
 ```

## References

> docs

- https://www.vnpy.com/docs/cn/index.html
- [vnpy - 社区版](https://www.vnpy.com/docs/cn/community/index.html)

> install

- [vnpy - macos install](https://www.vnpy.com/docs/cn/community/install/mac_install.html)
- [vnpy - ubuntu install](https://www.vnpy.com/docs/cn/community/install/ubuntu_install.html)
- [vnpy - windows install](https://www.vnpy.com/docs/cn/community/install/windows_install.html)