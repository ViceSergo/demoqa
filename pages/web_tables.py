from pages.base_page import BasePage
from components.components import WebElement

class WebTables(BasePage):

    def __init__(self,driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver,self.base_url)
        #Поле, что строки отсутствуют
        self.no_data = WebElement(driver,'div.rt-noData')
        # объекты таблицы
        self.btn_delete_row = WebElement(driver,'.rt-tbody div div div div span:nth-child(2)')
        self.btn_update_row = WebElement(driver,'.rt-tbody div div div div span:nth-child(1)')
        self.first_name_table = WebElement(driver,'div.rt-td:nth-child(1)')
        self.btn_add = WebElement(driver,'#addNewRecordButton')
        self.btn_next = WebElement(driver,'.-next > button')
        self.btn_previous = WebElement(driver,'.-previous > button')
        self.rows_table = WebElement(driver,'.rt-tr-group')
        self.btn_rows_table = WebElement(driver, 'span.select-wrap.-pageSizeOptions > select')
        self.btn_value_5 = WebElement(driver,"//*[contains(text(),'5 rows')]",'xpath')
        self.number_page=WebElement(driver,'.-center > span.-pageInfo > div > input')
        self.total_page=WebElement(driver,'.-totalPages')
        # объекты формы регестрации
        self.registration_form = WebElement(driver,'.modal-content')
        self.first_name_form = WebElement(driver,'#firstName')
        self.last_name_form = WebElement(driver,'#lastName')
        self.email_form = WebElement(driver,'#userEmail')
        self.age_form = WebElement(driver,'#age')
        self.salary_form = WebElement(driver,'#salary')
        self.departament_form = WebElement(driver,'#department')
        self.btn_submit_form = WebElement(driver,'#submit')


