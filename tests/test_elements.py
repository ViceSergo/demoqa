from pages.elements_page import ElementsPage


def test_find_elements(browser):
    el_page=ElementsPage(browser)

    el_page.visit()
    assert el_page.btns_first_menu.check_count_elements(9)
