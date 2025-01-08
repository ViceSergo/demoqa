import time
import logging
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self,driver,base_url):
        self.driver = driver
        self.base_url = base_url

    def equal_url(self):
        if self.get_url()==self.base_url:
            return True
        else:
            return False

    # get - перейти по урлу
    def visit(self):
        return self.driver.get(self.base_url)

    # Стрелка назад в браузере
    def back(self):
        self.driver.back()
    # Стрелка вперед в браузере
    def forward(self):
        self.driver.forward()
    # обновить страницу
    def refresh(self):
        self.driver.refresh()
    # получить title страницы
    def get_title(self):
        return self.driver.title
    # Получить текущий урл
    def get_url(self):
        return self.driver.current_url
    #выводит сообщение
    def alert(self):
        try:
            return self.driver.switch_to.alert
        except Exception as ex:
            logging.log(1,ex)
            return False

    # выводит сообщение и ждет пока пользователь введет текст и потом возвращает его
    def prompt(self):
        try:
            return self.driver.switch_to.alert
        except Exception as ex:
            logging.log(1, ex)
            return False

        # выводит сообщение и ждет пока пользователь нажмет ок или закрыть
    def confirm(self):
        try:
            return self.driver.switch_to.alert
        except Exception as ex:
            logging.log(1, ex)
            return False
    # set_window_size() - устанавливает размеры страницы