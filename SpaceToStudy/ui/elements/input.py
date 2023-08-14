from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.elements.base_element import BaseElement

INPUT = (By.XPATH, "./div/input")
LABEL = (By.XPATH, "./label")
ERROR_MESSAGE = (By.XPATH, "./p/span")


class Input(BaseElement):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self.label = None

    def set_text(self, text):
        self.get_input().send_keys(text)

    def get_input(self):
        return self.node.find_element(*INPUT)

    def get_error_message(self):
        return self.node.find_element(*ERROR_MESSAGE).text

    def get_label(self) -> str:
        if not self.label:
            self.label = self.node.find_element(*LABEL)
        return self.label.text
