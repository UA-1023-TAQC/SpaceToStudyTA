from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent

NEWEST = (By.XPATH, "./li[1]")
LOW_HIGH = (By.XPATH, "./li[2]")
HIGH_LOW = (By.XPATH, "./li[3]")


class DropdownMenu(BaseComponent):

    def __init__(self, node: WebElement):
        super().__init__(node)
        self._newest = None
        self._low_high = None
        self._high_low = None

    def get_newest(self) -> WebElement:
        if not self._newest:
            self._newest = self.node.find_element(*NEWEST)
        return self._newest

    def get_low_high(self) -> WebElement:
        if not self._low_high:
            self._low_high = self.node.find_element(*LOW_HIGH)
        return self._low_high

    def get_high_low(self) -> WebElement:
        if not self._high_low:
            self._high_low = self.node.find_element(*HIGH_LOW)
        return self._high_low

    def click_newest(self):
        self.get_newest().click()

    def click_low_high(self):
        self.get_low_high().click()

    def click_high_low(self):
        self.get_high_low().click()
