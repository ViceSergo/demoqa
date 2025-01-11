import time
from pages.modal_dialogs import ModalDialogs
from pages.demoqa import DemoQa


def test_modal_page(browser):
# 1. в файле test_check_modal.py автоматизируйте тест кейс
# a. страница https://demoqa.com/modal-dialogs
    modal_dialog_page = ModalDialogs(browser)
    modal_dialog_page.visit()
# i. на странице присутствуют 2 кнопки “Small modal” и “Large modal”
    assert modal_dialog_page.btn_small_modal.exist()
    assert modal_dialog_page.btn_large_modal.exist()
# ii. при клике на каждую открывается модальное окно
    modal_dialog_page.btn_small_modal.click()
    time.sleep(2)
    assert modal_dialog_page.modal_form.exist()
    modal_dialog_page.closeSmallModal.click()
    time.sleep(2)
    assert not modal_dialog_page.modal_form.exist()
# iii. у каждого окна есть кнопка “close” по клику окно закрывается
    modal_dialog_page.btn_large_modal.click()
    time.sleep(2)
    assert modal_dialog_page.modal_form.exist()
    modal_dialog_page.closeLargeModal.click()
    time.sleep(2)
    assert not modal_dialog_page.modal_form.exist()
# iv. *** Доработайте тестовый файл так, чтоб тест пропускался если страница недоступна.
# Подумайте, как можно проверять страницу на доступность.