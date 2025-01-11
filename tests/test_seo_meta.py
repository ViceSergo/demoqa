import time

from pages.demoqa import DemoQa
import pytest
from pages.alerts import Alert
from pages.browser_tab import BrowserTab
from pages.accordion import AccordionPage

@pytest.mark.parametrize('pages',[AccordionPage,Alert,BrowserTab,DemoQa])
def test_check_title_all_page(browser,pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)

    assert page.viewport.exist()
    assert page.viewport.get_dom_attribute('name')=='viewport'
    assert page.viewport.get_dom_attribute('content')=='width=device-width,initial-scale=1'