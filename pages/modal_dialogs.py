from pages.base_page import BasePage
from components.components import WebElement

class ModalDialogs(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        # Элемент, который соответствует всем кнопкам подменю
        self.modal_btns = WebElement(driver, 'button.modal-btn')


