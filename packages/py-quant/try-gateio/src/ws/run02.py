# pip install websocket_client
import hashlib
import hmac
import json
import time
from os import getenv

from loguru import logger
from websocket import create_connection


#
# ref: https://www.gate.io/docs/developers/apiv4/ws/zh_CN/#websocket-api-%E6%A6%82%E8%BF%B0
#

def gen_sign(channel, event, timestamp):
    # GateAPIv4 key pair
    api_key = getenv("GATEIO_API_KEY")
    api_secret = getenv("GATEIO_API_SECRET")  # required

    logger.debug(f"api key: {api_key}, secret: {api_secret}")

    s = 'channel=%s&event=%s&time=%d' % (channel, event, timestamp)
    sign = hmac.new(api_secret.encode('utf-8'), s.encode('utf-8'), hashlib.sha512).hexdigest()
    return {'method': 'api_key', 'KEY': api_key, 'SIGN': sign}


def ws_api():
    ws = create_connection("wss://api.gateio.ws/ws/v4/")
    ws.send(json.dumps({
        "time": int(time.time()),
        "channel": "spot.tickers",
        "event": "subscribe",  # "unsubscribe" for unsubscription
        "payload": ["BTC_USDT"]
    }))
    print(ws.recv())


if __name__ == '__main__':
    ws_api()
