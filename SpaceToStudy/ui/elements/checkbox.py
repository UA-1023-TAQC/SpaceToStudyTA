from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.elements.base_element import BaseElement

NAME_OF_CHECKBOX = (By.XPATH, "./p")
CHECKBOX_INPUT = (By.XPATH, "./span/input")
CHECKBOX_SVG = (By.XPATH, "./span/svg")


class Checkbox(BaseElement):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self._name_of_checkbox = None
        self._checkbox_input = None

    def set_check(self):
        self.get_checkbox_input().click()

    def get_name_of_checkbox(self) -> str:
        if not self._name_of_checkbox:
            self._name_of_checkbox = self.node.find_element(*NAME_OF_CHECKBOX)
        return self._name_of_checkbox.text

    def get_checkbox_input(self) -> WebElement:
        if not self._checkbox_input:
            self._checkbox_input = self.node.find_element(*CHECKBOX_INPUT)
        return self._checkbox_input

    def is_checked(self) -> bool:
        if self.node.find_element(*CHECKBOX_SVG).get_attribute("data-testid") == "CheckBoxIcon":
            return True
        return False
