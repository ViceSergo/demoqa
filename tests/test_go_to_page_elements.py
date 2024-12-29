from selenium.webdriver.common.by import By
from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
import time


def test_go_to_page_elements(browser):
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)

    demo_qa_page.visit()
    assert demo_qa_page.equal_url()
    demo_qa_page.btn_elements.click()
    assert elements_page.equal_url()