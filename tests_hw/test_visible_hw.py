import time
from pages.accordion import Accordion
from pages.elements_page import ElementsPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def test_visible_accordion(browser):
    accordion_page = Accordion(browser)
    accordion_page.visit()

    assert accordion_page.is_element_visible(accordion_page.section1_content)

    accordion_page.click(accordion_page.section1_heading)
    time.sleep(2)


    assert not accordion_page.is_element_visible(accordion_page.section1_content)


def test_visible_accordion_default(browser):
    accordion_page = Accordion(browser)
    accordion_page.visit()

    assert not accordion_page.is_element_visible(accordion_page.section2_content_1)
    assert not accordion_page.is_element_visible(accordion_page.section2_content_2)
    assert not accordion_page.is_element_visible(accordion_page.section3_content)