# from selenium.webdriver.common.by import By
from pages.demoqa import DemoQa
import time


def test_icon_exist(browser):
    demo_qa_page =DemoQa(browser)
    demo_qa_page.visit()
    demo_qa_page.icon.click()
    assert demo_qa_page.equal_url()
    assert demo_qa_page.icon.exist()