import jieba
import jieba.analyse
import requests
from bs4 import BeautifulSoup
from loguru import logger

from stopwords import get_stopwords


def get_news():
    url = "https://www.chinanews.com/cj/2023/12-08/10124985.shtml"

    r = requests.get(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
    })

    html_content = r.text.encode(r.encoding).decode(r.apparent_encoding)
    soup = BeautifulSoup(html_content, 'html.parser')

    content = ""
    el = soup.find_all('div', class_='left_zw')
    for e in el:
        content += e.text.strip()
    logger.info(f"{content}")
    return content


def clean(text):
    words = jieba.cut(text)
    logger.info(f"处理之前: {words}")

    sw = get_stopwords()

    #
    # todo x: 注意路径!
    #
    jieba.analyse.set_stop_words("dist/stopwords.txt")

    result = ""
    for word in words:
        # 清除 stop words
        if word not in sw:
            result += word + " "

    logger.info(f"处理之后: {result}")

    # return " ".join(jieba.cut(text))
    return result


def text_tags(text: str, with_weight: bool = False):
    return jieba.analyse.extract_tags(
        text,
        topK=20,
        withWeight=with_weight,
    )


if __name__ == '__main__':
    content = get_news()

    txt = clean(content)
    ret = text_tags(txt)
    logger.info(f"tags: {ret}")
    logger.info(f"tags: {text_tags(txt, True)}")
