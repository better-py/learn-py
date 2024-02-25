import os

import requests
from bs4 import BeautifulSoup
from loguru import logger
from requests.utils import dict_from_cookiejar

LOGIN_URL = ""
LOGIN_CA_URL = "https://ais.usvisa-info.com/en-ca/niv/users/sign_in"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"


def get_schedule_home(country_id: str, schedule_id: str):
    return f"https://ais.usvisa-info.com/en-{country_id or 'ca'}/niv/schedule/{schedule_id}/appointment"


def get_schedule_api(country_id: str, schedule_id: str, location_id: str):
    # ca = canada, gb = england
    # 95 = vancouver

    json_api = "https://ais.usvisa-info.com/en-ca/niv/schedule/53081715/appointment/days/94.json?appointments[expedite]=false"

    return f"https://ais.usvisa-info.com/en-{country_id or 'ca'}/niv/schedule/{schedule_id}/appointment/days/{location_id or 95}.json?appointments[expedite]=false"


def pre_login(lang_code, country_code):
    host = f"https://ais.usvisa-info.com/{lang_code or 'en'}-{country_code or 'ca'}/niv/users/sign_in"
    headers = {
        'User-Agent': USER_AGENT,
    }

    logger.info(f"login url: {host}")

    session = requests.Session()
    r = session.get(host, headers=headers)
    resp = r.text

    pre_session = session.cookies

    for cookie in session.cookies:
        logger.info(f"http cookie: {cookie.name}={cookie.value}")

    soup = BeautifulSoup(resp, 'lxml')

    csrf_token = soup.find("meta", {"name": "csrf-token"})['content']

    logger.info(f"http header csrf-token: {csrf_token}")
    logger.info(f"http url csrf-token: {r.url}, {r.status_code}")

    # do login

    return host, pre_session, csrf_token


def login(email, password, schedule_id, location_id):
    lang_code = 'en'
    country_code = 'ca'

    # prepare for login
    host, cookies, csrf_token = pre_login(lang_code, country_code)

    # 请请求头尽可能模拟浏览器
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'ais.usvisa-info.com',
        'Origin': 'https://ais.usvisa-info.com',
        'Referer': host,
        'Update-Insecure-Requests': '1',
        'User-Agent': USER_AGENT,
        # 'Cookie': cookie,

        #
        #
        #
        'Dnt': '1',
        'Sec-Ch-Ua-Platform': '"macOS"',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'X-Csrf-Token': csrf_token,
        'X-Requested-With': 'XMLHttpRequest',
    }

    payload = {
        'user[email]': email,
        'user[password]': password,
        'policy_confirmed': '1',
        'commit': 'Sign In',
    }

    session = requests.Session()

    resp = session.request(
        'POST',
        host,
        headers=headers,
        cookies=cookies,
        data=payload
    )

    for cookie in session.cookies:
        logger.info(f"http login cookie: {cookie.name}={cookie.value}")

    auth_cookies = dict_from_cookiejar(session.cookies)
    logger.info(f"login resp cookies: {auth_cookies}")

    logger.info(f"login resp: {resp.status_code}, url: {resp.url} ")

    def parse_xsrf_token(html):
        soup = BeautifulSoup(html, 'lxml')
        return soup.find("meta", {"name": "csrf-token"})['content']

    #
    # check schedule
    #
    check_url = get_schedule_api(country_code, schedule_id, location_id)
    home_url = get_schedule_home(country_code, schedule_id)

    logger.info(f"check url: {check_url}")

    r = session.get(home_url, headers=headers)

    x_csrf_token = parse_xsrf_token(r.text)
    check_headers = headers.copy()
    check_headers['X-Xsrf-Token'] = x_csrf_token

    logger.info(f"login x_csrf_token: {x_csrf_token}, url: {resp.url}")

    logger.info(f"check resp: {r.status_code}, {r.text}")
    logger.info(f"check resp: {r.status_code}, {r.url}")

    r2 = requests.request(
        "GET",
        check_url,
        headers=check_headers,
        cookies=session.cookies,
    )

    logger.info(f"check resp: {r2.status_code}, {r2.url}, {r2.json()}")
    logger.info(f"check resp: {r2.status_code}, {r2.url}")


def main():
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")
    schedule_id = os.getenv("SCHEDULE_ID")
    location_id = os.getenv("LOCATION_ID") or "95"  # vancouver

    if not email or not password:
        print("Please set EMAIL and PASSWORD environment variables")
        return

    logger.info(f"email: {email}, password: {password}, schedule_id: {schedule_id}")

    login(email, password, schedule_id, location_id)


if __name__ == '__main__':
    main()
