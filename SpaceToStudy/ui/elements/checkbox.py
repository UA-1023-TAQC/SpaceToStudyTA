import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.elements.base_element import BaseElement

NAME_OF_CHECKBOX = (By.XPATH, "./p")
CHECKBOX_INPUT = (By.XPATH, "//form//input[@type='checkbox']")
CHECKBOX_SVG = (By.XPATH, "./span/svg")


class Checkbox(BaseElement):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self._name_of_checkbox = None
        self._checkbox_input = None

    @allure.step("Click the checkbox input element")
    def set_check(self):
        self.get_checkbox_input().click()

    @allure.step("Get text the checkbox input element")
    def get_name_of_checkbox(self) -> str:
        if not self._name_of_checkbox:
            self._name_of_checkbox = self.node.find_element(*NAME_OF_CHECKBOX)
        return self._name_of_checkbox.text

    @allure.step("Get the checkbox input element")
    def get_checkbox_input(self) -> WebElement:
        if not self._checkbox_input:
            self._checkbox_input = self.node.find_element(*CHECKBOX_INPUT)
        return self._checkbox_input

    @allure.step("Check if the checkbox input element is selected")
    def is_checked(self) -> bool:
        return self.node.find_element(*CHECKBOX_INPUT).get_attribute("value") == "true"
