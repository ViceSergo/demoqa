from pages.base_page import BasePage
from components.components import WebElement


class ModalDialogs(BasePage):

    def __init__(self,driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver,self.base_url)

        self.icon = WebElement(driver, 'header>a>img')
        self.btn_small_modal = WebElement(driver,'#showSmallModal')
        self.closeSmallModal = WebElement(driver,'#closeSmallModal')
        self.btn_large_modal = WebElement(driver,'#showLargeModal')
        self.closeLargeModal = WebElement(driver,'#closeLargeModal')
        self.modal_form = WebElement(driver, '.modal-content')
        self.btns_third_menu = WebElement(driver, '#app > div > div > div > div:nth-child(1) > div > div > div:nth-child(3) > div > ul>li')