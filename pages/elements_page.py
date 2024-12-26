from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException


class ElementsPage(BasePage):

    def __init__(self,driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver,self.base_url)

