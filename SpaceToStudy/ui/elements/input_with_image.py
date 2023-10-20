import os
import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.elements.base_element import BaseElement


ICON = (By.XPATH, "./following-sibling::div/div/button/svg")


class InputWithImage(BaseElement):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self._icon = None

    @allure.step("Set photo")
    def set_photo(self, path):
        self.node.send_keys(os.getcwd() + path)
        print(os.getcwd() + path)

    @allure.step("Get icon element")
    def get_icon(self):
        if not self._icon:
            self._icon = self.node.find_element(*ICON)
        return self._icon

    @allure.step("Click icon element")
    def click_icon(self):
        self.get_icon().click()
