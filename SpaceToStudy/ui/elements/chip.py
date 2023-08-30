from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.elements.base_element import BaseElement

NAME = (By.XPATH, ".//p")
CLOSE_BTN = (By.XPATH, "./button")

class Chip(BaseElement):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self._name = None
        self._close_btn = None

    def get_chip_name(self) -> str:
        if not self._name:
            self._name = self.node.find_element(*NAME)
        return self._name.text

    def get_close_btn(self) -> WebElement:
        if not self._close_btn:
            self._close_btn = self.node.find_element(*CLOSE_BTN)
        return self._close_btn

    def click_close_btn(self):
        self.get_close_btn().click()
