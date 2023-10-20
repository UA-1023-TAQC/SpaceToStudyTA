import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.elements.base_element import BaseElement

INPUT = (By.XPATH, "./div/input")
LABEL = (By.XPATH, "./label")
ERROR_MESSAGE = (By.XPATH, "./p/span")


class Input(BaseElement):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self._input = None
        self._label = None
        self._input_css_class = None
        self._label_location = None

    @allure.step("Get input element")
    def get_input(self):
        if not self._input:
            self._input = self.node.find_element(*INPUT)
        return self._input

    @allure.step("Set {text} text into input element")
    def set_text(self, text):
        self.get_input().send_keys(text)

    @allure.step("Get text of input element")
    def get_text(self):
        return self.get_input().get_attribute("value")

    @allure.step("Clear text in input element")
    def clear_text_input(self):
        input_element = self.get_input()
        input_element.send_keys(Keys.CONTROL + "a")
        input_element.send_keys(Keys.DELETE)

    @allure.step("Get label element")
    def get_label(self):
        if not self._label:
            self._label = self.node.find_element(*LABEL)
        return self._label

    @allure.step("Get text of label element")
    def get_label_text(self) -> str:
        if not self._label:
            self._label = self.node.find_element(*LABEL)
        return self._label.text

    @allure.step("Get location of label element")
    def get_label_location(self):
        if self._input:
            self._label_location = self._input.location
        return self._label_location

    @allure.step("Get css class of input element")
    def get_input_css_class(self):
        if self._input:
            self._input_css_class = self._input.get_attribute("class")
        return self._input_css_class

    @allure.step("Get text of error message element")
    def get_error_message(self) -> str:
        return self.node.find_element(*ERROR_MESSAGE).text


class PasswordInput(Input):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self._hidden_button = None

    @allure.step("Get hidden button element")
    def get_hidden_icon(self):
        if not self._hidden_button:
            self._hidden_button = self.node.find_elements(By.XPATH, "./span")
        return self._hidden_button

    @allure.step("Click hidden button element")
    def click_hidden_icon(self):
        self.get_hidden_icon().click()
