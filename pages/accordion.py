from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement

class Accordion(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordion'
        super().__init__(driver, self.base_url)

        self.section1_content = (By.CSS_SELECTOR, "#section1Content > p")
        self.section1_heading = (By.CSS_SELECTOR, "#section1Heading")
        self.section2_content_1 = (By.CSS_SELECTOR, "#section2Content > p:nth-child(1)")
        self.section2_content_2 = (By.CSS_SELECTOR, "#section2Content > p:nth-child(2)")
        self.section3_content = (By.CSS_SELECTOR, "#section3Content > p")

    def visit(self):
        self.driver.get(self.base_url)

    def is_element_visible(self, locator: tuple) -> bool:
        element: WebElement = self.find_element(locator)
        return element.is_displayed()

    def click(self, locator: tuple):
        element: WebElement = self.find_element(locator)
        element.click()