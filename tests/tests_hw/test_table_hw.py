import time
from pages.web_tables import WebTables
from selenium.webdriver.common.keys import Keys

# 1. Автоматизируйте тест кейс, страница https://demoqa.com/webtables
def test_modal_tables(browser):
    table_page = WebTables(browser)
    table_page.visit()
# a. на странице имеется кнопка Add
    assert table_page.btn_add.exist()
# b. по клику на кнопку Add открывается диалоговое окно
    table_page.btn_add.click()
    time.sleep(2)
    assert table_page.registration_form.exist()
# c. в диалоге нельзя сохранить пустую форму
    table_page.btn_submit_form.click()
    assert table_page.registration_form.exist()
# d. если заполнить все поля и нажать на кнопку Submit
    table_page.first_name_form.send_keys('tester')
    table_page.last_name_form.send_keys('testerov')
    table_page.email_form.send_keys('test@er.ru')
    table_page.age_form.send_keys('25')
    table_page.salary_form.send_keys('100000')
    table_page.departament_form.send_keys('test')
    table_page.btn_submit_form.click()
    time.sleep(2)
# i. диалог закрывается
    assert not table_page.registration_form.exist()
# ii. в таблицу добавляется новая запись с введенными данными
    assert table_page.btn_delete_row.check_count_elements(4)
# e. если кликнуть на карандаш на строке записи
    table_page.btn_update_row.click()
    time.sleep(2)
# i. открывается диалог с введенными данными
    assert table_page.registration_form.exist()
# f. если изменить имя и сохранить то в таблице обновятся данные
    table_page.first_name_form.clear()
    time.sleep(2)
    table_page.first_name_form.send_keys('NewTester')
    table_page.btn_submit_form.click()
    time.sleep(2)
    assert table_page.first_name_table.get_text()=='NewTester'
# g. если нажать на корзину в строке записи - запись удаляется
    table_page.btn_delete_row.click()
    time.sleep(2)
    assert table_page.btn_delete_row.check_count_elements(3)


# 2. * Автоматизируйте тест кейс, страница https://demoqa.com/webtables
def test_scroll_table(browser):
    # a. предусловия
    # i. открыта страница
    # ii. кол-во строк в таблице установлено 5
    table_page = WebTables(browser)
    table_page.visit()
    time.sleep(2)
    table_page.btn_rows_table.scroll_to_element()
    table_page.btn_rows_table.click()
    table_page.btn_value_5.click()
    time.sleep(2)
    assert table_page.rows_table.check_count_elements(5)
# b. тест кейс
# i. кнопки Next и Previous заблокированы (по клику ничего не происходит и имеют атрибут disabled)
    assert table_page.btn_next.get_dom_attribute('disabled')
    assert table_page.btn_previous.get_dom_attribute('disabled')
# ii. если добавить в таблицу еще 3 записи то:
    for i in range(3):
        table_page.btn_add.click()
        time.sleep(2)
        table_page.first_name_form.send_keys(f'tester+{i}')
        table_page.last_name_form.send_keys('testerov')
        table_page.email_form.send_keys('test@er.ru')
        table_page.age_form.send_keys('25')
        table_page.salary_form.send_keys('100000')
        table_page.departament_form.send_keys('test')
        table_page.btn_submit_form.click()
        time.sleep(2)
# 1. появляется 2-я страница (of 2)
    assert table_page.total_page.get_text()=='2'
# 2. кнопка Next становится доступной
    assert not table_page.btn_next.get_dom_attribute('disabled')
# iii. если кликнуть по кнопке Next то открывается 2-я страница
    table_page.btn_next.click()
    time.sleep(2)
    assert table_page.number_page.get_dom_attribute('value')=='2'
# iv. если кликнуть по кнопке Previous то открывается 1-я страница
    table_page.btn_previous.click()
    time.sleep(2)
    assert table_page.number_page.get_dom_attribute('value')=='1'