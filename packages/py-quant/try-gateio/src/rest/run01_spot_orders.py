# coding: utf-8
# example WebSocket signature calculation implementation in Python
import hashlib
import hmac
import time
from os import getenv

import requests
from loguru import logger


# pip install websocket_client


def gen_sign(method, url, query_string=None, payload_string=None):
    # GateAPIv4 key pair
    key = getenv("GATEIO_API_KEY")
    secret = getenv("GATEIO_API_SECRET")  # required

    logger.debug(f"api key: {key}, secret: {secret}")

    t = time.time()
    m = hashlib.sha512()
    m.update((payload_string or "").encode('utf-8'))
    hashed_payload = m.hexdigest()
    s = '%s\n%s\n%s\n%s\n%s' % (method, url, query_string or "", hashed_payload, t)
    sign = hmac.new(secret.encode('utf-8'), s.encode('utf-8'), hashlib.sha512).hexdigest()
    return {'KEY': key, 'Timestamp': str(t), 'SIGN': sign}


def restapi():
    """
    todo x: 查询订单列表
        https://www.gate.io/docs/developers/apiv4/zh_CN/#%E6%9F%A5%E8%AF%A2%E8%AE%A2%E5%8D%95%E5%88%97%E8%A1%A8

    """

    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    url = '/spot/orders'
    query_param = 'currency_pair=BTC_USDT&status=open'
    # `gen_sign` 的实现参考认证一章
    sign_headers = gen_sign('GET', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())


if __name__ == '__main__':
    restapi()
