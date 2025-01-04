from pages.base_page import BasePage
from components.components import WebElement

class AccordionPage(BasePage):

    def __init__(self,driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver,self.base_url)

        self.section_1_Content = WebElement(driver, '#section1Content > p')
        self.section_2_Content_1 = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.section_2_Content_2 = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.section_3_Content = WebElement(driver, '#section3Content > p')
        self.section_1_Heading = WebElement(driver, '#section1Heading')