from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def scrape_zhihu_answers(username, password):
    options = Options()
    options.add_argument("--headless")  # 无界面模式运行

    # 替换为您的 Chrome 驱动路径
    service = Service('path_to_chromedriver')

    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://www.zhihu.com/signin")

    # 等待登录页面加载完成
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="username"]')))

    # 输入用户名和密码
    driver.find_element(By.CSS_SELECTOR, 'input[name="username"]').send_keys(username)
    driver.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys(password)

    # 点击登录按钮
    driver.find_element(By.CSS_SELECTOR, 'button.SignFlow-submitButton').click()

    # 等待登录成功并跳转到个人回答页面
    WebDriverWait(driver, 10).until(EC.url_contains("https://www.zhihu.com/people"))

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
    with open("zhihu_answers.html", "w", encoding="utf-8") as file:
        file.write(html_content)

    driver.quit()


# 替换为您的知乎用户名和密码
username = "your_username"
password = "your_password"
scrape_zhihu_answers(username, password)
