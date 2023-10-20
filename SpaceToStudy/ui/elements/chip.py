import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.elements.base_element import BaseElement

NAME = (By.XPATH, ".//p")
CLOSE_BTN = (By.XPATH, "./button")


class Chip(BaseElement):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self._name = None

    @allure.step("Get text chip element")
    def get_chip_name(self) -> str:
        if not self._name:
            self._name = self.node.find_element(*NAME)
        return self._name.text

    @allure.step("Click chip element")
    def click_close_btn(self):
        self.node.find_element(*CLOSE_BTN).click()
