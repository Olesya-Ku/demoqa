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

def test_page_elements(browser):
    el_page = ElementsPage(browser)
    el_page.visit()

    assert el_page.text_elements.get_text() == 'Please select an item from left to start practice.'
    assert el_page.icon.exist()
    assert el_page.btn_sidebar_first.exist()
    assert el_page.btn_sidebar_first_textbox.exist()



