# ccxt

- 数字货币 + 量化交易策略

## Guide:

### run

```ruby

# .env file, set api-key 
BINANCE_API_KEY=
BINANCE_SECRET_KEY=
   
# install
uv sync     

# then, run
task quant:ccxt:run -- tr_binance.py
 
# or 
cd this-dir/
task run -- tr_binance.py
 
       
```

## FAQ:

### 请求超时问题:

- ask: 本地测试,频繁出现请求超时.
- ans: 需要设置 HTTP 代理.

### proxy + 403 Forbidden:

- ask: 本地测试, 403 Forbidden
- ans: VPN 不要使用 HK 节点, 改为 JP, TW 节点.