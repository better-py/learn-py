import os

import requests
from loguru import logger


def get_stopwords():
    base_url = 'https://raw.githubusercontent.com/goto456/stopwords/master/'

    # stopwords = set()
    stopwords = []

    for url in [
        base_url + 'baidu_stopwords.txt',
        base_url + 'cn_stopwords.txt',
        base_url + 'hit_stopwords.txt',
        base_url + 'scu_stopwords.txt',
    ]:
        r = requests.get(url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
        })
        if r.status_code == 200:
            content = r.text
            # txt 文本根据换行, 切分成数组
            words = content.split('\n')
            # logger.info(f"🔥 {words}")
            stopwords += words
    return stopwords


def save_stopwords(stopwords):
    # 创建 dist 目录
    if not os.path.exists('dist'):
        os.mkdir('dist')

    with open('dist/stopwords.txt', 'w', encoding='utf-8') as f:
        for word in stopwords:
            f.write(word + '\n')


if __name__ == '__main__':
    ret = get_stopwords()
    save_stopwords(ret)
    logger.info(f"🔥sum: {len(ret)}")
