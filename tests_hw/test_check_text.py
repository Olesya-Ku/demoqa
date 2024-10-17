import pytest
from selenium import webdriver
from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
from components.components import WebElement


def test_check_text(browser):
        demo_qa_page = DemoQa(browser)
        demo_qa_page.visit()

        def test_footer_text(self, setup):
            demo_page = DemoQa(self.driver)
            demo_page.visit()


            footer_text = WebElement(self.driver,"footer").get_text()
            assert footer_text == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'

        def test_center_text(self, setup):
            demo_page = DemoQa(self.driver)
            demo_page.visit()


            demo_page.btn_elements.click()

            elements_page = ElementsPage(self.driver)


            center_text = WebElement(self.driver,".has-text-align-center").get_text()
            assert center_text == 'Please select an item from left to start practice.'

