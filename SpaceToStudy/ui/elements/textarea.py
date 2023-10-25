import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.elements.base_element import BaseElement

DESCRIPTION = (By.XPATH, "./p")
# TEXTAREA = (By.XPATH, "./div/div/div/textarea[1]")
TEXTAREA = (By.XPATH, "./div/textarea[1]")
LABEL = (By.XPATH, "./div/div/label")
ERROR_MESSAGE = (By.XPATH, "./div/div/p/span")
LETTER_COUNTER = (By.XPATH, "./div/p")


class Textarea(BaseElement):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self._description = None
        self._textarea = None
        self._label = None
        self._error_message = None
        self._letter_counter = None

    @allure.step("Get textarea")
    def get_textarea(self) -> WebElement:
        if not self._textarea:
            self._textarea = self.node.find_element(*TEXTAREA)
        return self._textarea

    @allure.step("Set {text} text")
    def set_text(self, text):
        self.node.send_keys(text)

    @allure.step("Get text")
    def get_text(self):
        return self.node.text

    @allure.step("Get description")
    def get_description(self) -> str:
        if not self._description:
            self._description = self.node.find_element(*DESCRIPTION)
        return self._description.text

    @allure.step("Get label")
    def get_label(self) -> str:
        if not self._label:
            self._label = self.node.find_element(*LABEL)
        return self._label.text

    @allure.step("Get error message")
    def get_error_message(self) -> str:
        if not self._error_message:
            self._error_message = self.node.find_element(*ERROR_MESSAGE)
        return self._error_message.text

    @allure.step("Is label shrink")
    def is_label_shrink(self) -> bool:
        if self._label.get_attribute("data-shrink"):
            return True
        else:
            return False
