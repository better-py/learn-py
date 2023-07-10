from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.webkit.launch(headless=False)
    context = browser.new_context(**playwright.devices["iPhone 11"],
                                  geolocation={"latitude": 31.224361, "longitude": 121.46917},
                                  permissions=["geolocation"], viewport={"width": 1280, "height": 720})
    page = context.new_page()
    page.goto("https://twitter.com/i/flow/login?redirect_after_login=%2F")
    page.locator("label div").nth(4).click()
    page.get_by_label("手机号码、邮件地址或用户名").fill("######")
    page.get_by_role("button", name="下一步").click()
    page.get_by_label("密码", exact=True).click()
    page.get_by_label("密码", exact=True).fill("######")
    page.get_by_test_id("LoginForm_Login_Button").click()
    page.get_by_test_id("ocfEnterTextTextInput").fill("######")
    page.get_by_test_id("ocfEnterTextNextButton").click()
    page.get_by_test_id("ocfEnterTextTextInput").fill("######")
    page.get_by_test_id("ocfEnterTextNextButton").click()
    page.get_by_test_id("DashButton_ProfileIcon_Link").click()
    page.get_by_role("link", name="个人资料").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
