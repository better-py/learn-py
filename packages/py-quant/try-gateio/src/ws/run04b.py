import os
import time
import json
from os import getenv
# pip install websocket_client
from websocket import create_connection

# example WebSocket signature calculation implementation in Python
import hmac, hashlib, json, time
from loguru import logger


def gen_sign(channel, event, timestamp):
    # GateAPIv4 key pair
    api_key = getenv("GATEIO_API_KEY")
    api_secret = getenv("GATEIO_API_SECRET")  # required

    logger.debug(f"api key: {api_key}, secret: {api_secret}")

    s = 'channel=%s&event=%s&time=%d' % (channel, event, timestamp)
    sign = hmac.new(api_secret.encode('utf-8'), s.encode('utf-8'), hashlib.sha512).hexdigest()
    return {'method': 'api_key', 'KEY': api_key, 'SIGN': sign}


# request = {
#     'id': int(time.time() * 1e6),
#     'time': int(time.time()),
#     'channel': 'spot.orders',
#     'event': 'subscribe',
#     'payload': ["BTC_USDT", "GT_USDT"]
# }
# request['auth'] = gen_sign(request['channel'], request['event'], request['time'])
# print(json.dumps(request))


def get_orders():
    ws = create_connection("wss://api.gateio.ws/ws/v4/")
    request = {
        "time": int(time.time()),
        "channel": "spot.orders",
        "event": "subscribe",  # "unsubscribe" for unsubscription
        "payload": ["BTC_USDT"]
    }
    # refer to Authentication section for gen_sign implementation
    request['auth'] = gen_sign(request['channel'], request['event'], request['time'])
    ws.send(json.dumps(request))
    print(ws.recv())


if __name__ == '__main__':
    get_orders()
