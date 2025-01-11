import time
from pages.alerts import Alert


# 2. в файле test_check_alert.py автоматизируйте тест кейс:
# a. Страница https://demoqa.com/alerts
def test_alert(browser):
    page_alert = Alert(browser)
    page_alert.visit()
# i. на странице присутствует кнопка “#timerAlertButton”
    assert page_alert.timerAlertButton.exist()
# ii. через 5 сек после клика на кнопку всплывает алерт
    page_alert.timerAlertButton.click()
    time.sleep(2)
    assert not page_alert.alert()
    time.sleep(3)
    assert page_alert.alert()
