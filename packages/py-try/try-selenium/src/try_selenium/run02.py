from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def scrape_zhihu_answers(username):
    options = Options()
    options.add_argument("--headless")  # 无界面模式运行

    # mac chrome path:
    chrome_path = "/Applications/Google\ Chrome.app"

    # 替换为您的 Chrome 驱动路径
    service = Service(chrome_path)

    driver = webdriver.Chrome(service=service, options=options)

    driver.get(f"https://www.zhihu.com/people/{username}/answers")

    # 等待页面加载完成
    driver.implicitly_wait(10)

    # 获取所有回答的元素
    answer_elements = driver.find_elements(By.CSS_SELECTOR, ".ContentItem")

    # 构建 HTML 页面
    html_content = "<html><body><ul>"

    # 遍历每个回答元素并提取信息
    for element in answer_elements:
        question = element.find_element(By.CSS_SELECTOR, ".QuestionItem-title").text
        answer = element.find_element(By.CSS_SELECTOR, ".RichContent-inner").get_attribute("innerHTML")
        html_content += f"<li><h3>{question}</h3>{answer}</li>"

    html_content += "</ul></body></html>"

    # 保存为 HTML 文件
    with open("dist/zhihu_answers.html", "w", encoding="utf-8") as file:
        file.write(html_content)

    driver.quit()


# 替换为要抓取的知乎用户名
username = "your_username"
scrape_zhihu_answers(username)
