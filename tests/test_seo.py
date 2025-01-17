import time

from pages.demoqa import DemoQa
import pytest
from pages.alerts import Alert
from pages.browser_tab import BrowserTab
from pages.accordion import AccordionPage

def test_check_title_demo(browser):
    demo_qa_page=DemoQa(browser)

    demo_qa_page.visit()
    assert browser.title=='DEMOQA'


@pytest.mark.parametrize('pages',[AccordionPage,Alert,BrowserTab,DemoQa])
def test_check_title_all_page(browser,pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)
    assert page.get_title()=='DEMOQA'
