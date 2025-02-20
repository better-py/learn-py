# binance

- 交易所 http/ws api 验证

## usage


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

## python sdk

- https://github.com/binance/binance-signature-examples
- https://github.com/binance/binance-connector-python
- https://github.com/binance/binance-futures-connector-python

## data

- https://github.com/binance/binance-public-data

## reference

- https://github.com/binance
- https://github.com/binance/binance-futures-connector-python