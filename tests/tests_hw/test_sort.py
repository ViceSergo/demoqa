# 3. в файле test_sort.py автоматизируйте тест кейс:
import time
from pages.web_tables import WebTables

# a. Страница https://demoqa.com/webtables

def test_sort_table(browser):
    table_page = WebTables(browser)
    table_page.visit()
# b. при клике на каждый заголовок столбца страницы,
# происходит сортировка таблицы по этому столбцу
# (Для проверки сортировки, в данном кейсе,
# достаточно считывать соответствующий класс элемента)
    # Получаем список заголовков таблицы
    headers = table_page.headers.find_elements()
    for header in headers:
        # Получаем текущий класс перед кликом
        current_class = header.get_dom_attribute("class")
        # Кликаем на заголовок
        header.click()
        # Проверяем, что класс изменился
        new_class = header.get_dom_attribute("class")
        assert new_class != current_class