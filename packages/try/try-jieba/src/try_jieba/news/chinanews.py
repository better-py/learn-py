import requests
from bs4 import BeautifulSoup
from loguru import logger


class ChinaNews(object):
    """
    中国新闻网:
        - 财经: https://www.chinanews.com/finance/
        - 搜索: https://sou.chinanews.com.cn/search.do
    """

    def __init__(self):
        self.host = "https://www.chinanews.com"
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
        }

    def get_top_news(self):
        r = requests.get(self.host + "/finance/", headers=self.header)
        logger.info(f"page encoding: {r.encoding}, {r.apparent_encoding}")
        # html_content = r.text
        html_content = r.text.encode(r.encoding).decode(r.apparent_encoding)  # todo x: 修复中文编码问题!
        soup = BeautifulSoup(html_content, 'html.parser')

        news = []
        el = soup.find_all('div', class_='jxnews')
        for e in el:
            # 继续提取内部的 a 标签的 URL
            url = e.find('a').get('href')
            # title = e.find('a').text
            title = e.find('div', class_='title').text
            time = e.find('div', class_='info').text.split("|")[-1].strip()
            item = {
                'title': title,
                'url': url,
                'time': time
            }

            logger.info(f"🔥 {item}")
            news.append(item)
        return news


if __name__ == '__main__':
    n = ChinaNews()
    n.get_top_news()
