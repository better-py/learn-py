# gateio

## usage

- ws api 监听 spot ticker

```ruby

# .env file, set api-key
GATEIO_API_KEY=
GATEIO_API_SECRET=
GATEIO_TESTNET=

# install requirements
uv sync 
  
# run:  
task quant:gate:r -- ws/run02_spot_ticker.py
    
```

## reference

- https://github.com/gateio/gateapi-python