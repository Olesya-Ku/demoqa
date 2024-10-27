from components.components import WebElement
from pages.base_page import BasePage

class Accordian(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.section1_content = WebElement(driver, "#section1Content > p")
        self.section1_heading = WebElement(driver, "#section1Heading")
        self.section2_content_1 = WebElement(driver, "#section2Content > p:nth-child(1)")
        self.section2_content_2 = WebElement(driver, "#section2Content > p:nth-child(2)")
        self.section3_content = WebElement(driver, "#section3Content > p")

    def click(self, locator: tuple):
        element: WebElement = self.find_element(locator)
        element.click()