import time

from pages.web_tables import WebTables

def test_tables(browser):
    page_tables = WebTables(browser)
    page_tables.visit()
    # проверка блока No rows found
    assert not page_tables.no_data.exist()
    # Удаляем все строки
    while page_tables.btn_delete_row.exist():
        page_tables.btn_delete_row.click()

    time.sleep(5)
    assert page_tables.no_data.exist()

