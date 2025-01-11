# 4. * в файле test_window_tab.py автоматизируйте тест кейс:
from pages.links_page import LinksPage
from pages.demoqa import DemoQa
import time
# a. Страница https://demoqa.com/links
def test_link(browser):
    link_page = LinksPage(browser)
    demo_qa_page = DemoQa(browser)
    link_page.visit()
# b. На странице имеется ссылка “Home”
    assert link_page.link_home.exist()
# c. текст ссылки == “Home”
    assert link_page.link_home.get_text()=='Home'
# d. href ссылки == “https://demoqa.com”
    assert link_page.link_home.get_dom_attribute('href')=='https://demoqa.com'
# e. При клике на ссылку открывается новая вкладка
    assert len(browser.window_handles) == 1
    link_page.link_home.click()
    time.sleep(2)
    assert len(browser.window_handles)==2
    # assert demo_qa_page.equal_url() - Проверка не сработает(когда мы переходим по ссылке
    # открывается новая вкладка, но чтобы с ней взаимодействовать нужно на нее переключиться
    # при помощи browser.switch_to.window(browser.window_handles[индекс вкладки])
    assert link_page.equal_url()
    # Вернемся на страницу с ссылками
    browser.switch_to.window(browser.window_handles[0])
    time.sleep(2)
    assert link_page.equal_url()