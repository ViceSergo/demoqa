import time
from pages.text_box import TextBox

def test_placeholder(browser):
    text_box_page = TextBox(browser)
    text_box_page.visit()
    text_name='tester'
    text_adress='testovaya'

    text_box_page.name.send_keys({text_name})
    text_box_page.current_address.send_keys({text_adress})
    text_box_page.btn_submit.click_force()
    time.sleep(2)
    assert text_box_page.window_output_1.get_text()==(f"Name:{text_name}\nCurrent Address :{text_adress}")