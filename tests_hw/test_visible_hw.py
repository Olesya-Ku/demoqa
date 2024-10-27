import time
from pages.accordian import Accordian
from selenium.webdriver.common.by import By


def test_visible_accordian(browser):
    accordian_page = Accordian(browser)
    accordian_page.visit()
    assert accordian_page.section1_content.visible()

    accordian_page.section1_heading.click()
    time.sleep(2)
    assert accordian_page.section1_content.visible()


def test_visible_accordian_default(browser):
    accordian_page = Accordian(browser)
    accordian_page.visit()

    assert not accordian_page.section2_content_1.visible()
    assert not accordian_page.section2_content_2.visible()
    assert not accordian_page.section3_content.visible()