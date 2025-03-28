# binance

- 交易所 http/ws api 验证

## usage

- 设置 api-key 到 `.env` 文件, 参见根目录的 `.env.local`

```ruby

BINANCE_API_KEY="your_binance_api_key"
BINANCE_SECRET_KEY="your_binance_secret_key"
BINANCE_TESTNET=


```

- 运行(下面的运行脚本, 会自动安装依赖包):

```ruby


# cd repo-root-dir/
# then, run:
task quant:bn:r -- ws/run02_spot_agg_trade.py

# ws + futures
task quant:bn:r -- ws/run03_futures_agg_trade.py


# restapi + spot
task quant:bn:r -- rest/run01_spot.py

# restapi + futures
task quant:bn:r -- rest/run02_futures.py

```

## 币安合约

- 币安合约提供两种类型的期货合约：币安保证金合约和美元保证金合约。
- https://www.binance.com/zh-CN/blog/futures/coinmargined-or-usd%E2%93%A2margined-what-futures-contract-suits-you-421499824684903739
- COIN-Margined or USDⓈ-Margined
- 对应 sdk 里面的 `CM-Futures` vs `UM-Futures`
- `币本位合约` vs `USDT 本位合约`

## python sdk

- https://github.com/binance/binance-signature-examples
- https://github.com/binance/binance-connector-python
- https://github.com/binance/binance-futures-connector-python

## data

- https://github.com/binance/binance-public-data

## reference

- https://github.com/binance
- https://github.com/binance/binance-futures-connector-python