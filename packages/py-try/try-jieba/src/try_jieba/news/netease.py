import requests
from bs4 import BeautifulSoup
from loguru import logger

"""
网易新闻:
    - https://news.163.com/
"""


class NewsBase(object):
    def __init__(self, host=None, header=None):
        self.host = host
        self.header = header or {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/89.0.142.86 Safari/537.36",
        }

    def get_hot_news(self):
        pass

    def get_news_content(self):
        pass


class NetEase(NewsBase):
    def __init__(self):
        self.host = "https://news.163.com/"  # 网易新闻
        super().__init__(self.host)

    def get_hot_news(self):
        r = requests.get(self.host, headers=self.header)
        html_content = r.text

        # 网页本体
        soup = BeautifulSoup(html_content, 'html.parser')

        # logger.info(soup.prettify())

        # 提取热门新闻列表, 配合 css class 进行提取
        news_titles = soup.find_all('ul', class_='top_news_ul')

        news = []
        for title in news_titles:
            # 继续提取内部的 a 标签的 URL
            a_tags = title.find_all('a')
            for a_tag in a_tags:
                news.append({
                    'title': a_tag.text,
                    'url': a_tag.get('href'),
                })
                logger.info(f"🔥{a_tag.text} ➡️\t {a_tag.get('href')}")

        logger.info(f"今日热门新闻统计: {len(news)} 篇")
        return news

    def get_news_content(self):
        pass


if __name__ == '__main__':
    n = NetEase()
    n.get_hot_news()
