from pages.accordion import AccordionPage
import time

def test_visible_accordion(browser):
    ac_page = AccordionPage(browser)

    ac_page.visit()
    assert ac_page.section_1_Content.visible()
    ac_page.section_1_Heading.click()
    time.sleep(2)
    assert not ac_page.section_1_Content.visible()

def test_visible_accordion_default(browser):
    ac_page = AccordionPage(browser)

    ac_page.visit()
    assert not ac_page.section_2_Content_1.visible()
    assert not ac_page.section_2_Content_2.visible()
    assert not ac_page.section_3_Content.visible()

