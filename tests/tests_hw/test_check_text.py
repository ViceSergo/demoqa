from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_check_text_to_basement(browser):
    demo_qa_page =DemoQa(browser)
    demo_qa_page.visit()

    assert demo_qa_page.equal_url()
    assert demo_qa_page.text_basement.get_text() == "© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED."
    assert demo_qa_page.text_basement.exist()

def test_text_center_page_elements(browser):
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)
    demo_qa_page.visit()
    assert demo_qa_page.equal_url()
    demo_qa_page.btn_elements.click()
    assert elements_page.equal_url()
    assert elements_page.text_center.get_text()=='Please select an item from left to start practice.'