from selenium.webdriver import Keys

from pages.slider import Slider


def test_slider(browser):
    slider_page = Slider(browser)
    slider_page.visit()

    assert slider_page.slider.exist()
    assert slider_page.sliderValue.exist()

    while not slider_page.sliderValue.get_dom_attribute('value')=='50':
        slider_page.slider.send_keys(Keys.ARROW_RIGHT)

    assert slider_page.sliderValue.get_dom_attribute('value')=='50'