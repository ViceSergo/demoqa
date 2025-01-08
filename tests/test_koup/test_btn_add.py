import time

from pages.hiroku.koup import Koup
from pages.hiroku.koup_add import KoupAdd

def test_koup_add(browser):
    koup_page=Koup(browser)
    koup_add=KoupAdd(browser)
    koup_page.visit()

    assert koup_page.link_add.get_text()=='Add/Remove Elements'
    koup_page.link_add.click()
    assert koup_add.equal_url()
    assert koup_add.btn_add.get_text()=='Add Element'
    assert koup_add.btn_add.get_dom_attribute('onclick')=='addElement()'
    # Нажать 4 раза на кнопку Add Element и проверить, что появилось 4 кнопки Delete
    for i in range(4):
        koup_add.btn_add.click()
    assert koup_add.btns_delete.check_count_elements(4)
    # проверить что все кнопки Delete имеют надпись Delete
    for element in koup_add.btns_delete.find_elements():
        assert element.text=='Delete'
    # нажать на все Delete и проверить что их не осталось
    while koup_add.btns_delete.exist():
        koup_add.btns_delete.click()
    assert not koup_add.btns_delete.exist()

    time.sleep(3)
