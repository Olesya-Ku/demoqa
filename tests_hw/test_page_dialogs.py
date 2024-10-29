import time
from pages.demoqa import DemoQa
from pages.modal_dialogs import ModalDialogs


def test_modal_elements(browser):
    modal_elements = ModalDialogs(browser)
    modal_elements.visit()

def get_mod_btns_count(self):
        return self.modal_btns.check_count_elements(5)



def test_navigation_modal(browser):
    page = ModalDialogs(browser)

    # Открыть страницу
    page.visit()

    # Обновить страницу
    page.refresh()

    # Перейти на главную страницу через иконку
    demo_page = DemoQa(browser)
    demo_page.icon.click()  # Нажимаем на иконку для перехода на главную страницу

    # Вернуться назад
    page.back()

    # Установить размеры экрана 900x400
    browser.set_window_size(900, 400)
    time.sleep(2)
    browser.set_window_size(1000, 1000)


    # Перейти вперед
    page.forward()

    # Проверка URL на главной странице
    assert page.get_url() == demo_page.base_url


    # Проверка title на главной странице
    assert browser.title == "DEMOQA"


