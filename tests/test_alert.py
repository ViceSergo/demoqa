import time

from pages.alerts import Alert

def test_alert(browser):
    page_alert = Alert(browser)
    page_alert.visit()
    assert not page_alert.alert()

    page_alert.alertButton.click()
    time.sleep(2)
    assert page_alert.alert()

def test_alert_text(browser):
    page_alert = Alert(browser)
    page_alert.visit()
    page_alert.alertButton.click()
    assert page_alert.alert().text=='You clicked a button'
    # нажали ок
    page_alert.alert().accept()
    assert not page_alert.alert()

def test_confirm(browser):
    page_alert = Alert(browser)
    page_alert.visit()
    page_alert.confirmButton.click()
    time.sleep(2)
    # нажали отмена
    page_alert.alert().dismiss()
    assert page_alert.confirmResult.get_text()=='You selected Cancel'


def test_prompt(browser):
    page_alert = Alert(browser)
    name = "Tester"
    page_alert.visit()
    page_alert.promptButton.click()
    time.sleep(2)
    page_alert.alert().send_keys(name)
    page_alert.alert().accept()
    assert page_alert.promptResult.get_text()==f'You entered {name}'