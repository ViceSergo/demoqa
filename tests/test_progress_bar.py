import time
from pages.progress_bar import ProgressBar

def test_slider(browser):
    progress_bar_page = ProgressBar(browser)
    progress_bar_page.visit()
    time.sleep(2)

    assert progress_bar_page.btn_start.exist()
    assert progress_bar_page.bar.exist()
    progress_bar_page.btn_start.click()
    while True:
        if progress_bar_page.bar.get_dom_attribute('aria-valuenow')=='51':
            progress_bar_page.btn_start.click()
            break
    time.sleep(2)

    assert progress_bar_page.bar.get_dom_attribute('aria-valuenow')=='51'