from pages.base_page import BasePage
from components.components import WebElement
from selenium.common.exceptions import NoSuchElementException


class ElementsPage(BasePage):

    def __init__(self,driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver,self.base_url)

        self.text_center = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6')
