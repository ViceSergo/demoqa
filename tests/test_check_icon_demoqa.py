# from selenium.webdriver.common.by import By
from pages.demoqa import DemoQa


def test_check_icon(browser):
    # browser.get('https://demoqa.com/')
    #
    # icon = browser.find_element(By.CSS_SELECTOR, '#app>header>a')
    #
    # if icon is None:
    #     print("Не найдено")
    # else:
    #     print("Найдено")

    demoqa_page =DemoQa(browser)
    demoqa_page.visit()
    assert demoqa_page.exist_icon()