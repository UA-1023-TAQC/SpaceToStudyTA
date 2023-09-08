from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent

LOW_HIGH = (By.XPATH, "./ul/li[2]")
HIGH_LOW = (By.XPATH, "./ul/li[3]")


class SortComponent(BaseComponent):

    def __init__(self, node: WebElement):
        super().__init__(node)
        self._low_high = None
        self._high_low = None

    def get_low_high(self) -> WebElement:
        if not self._low_high:
            self._low_high = self.node.find_element(*LOW_HIGH)
        return self._low_high

    def click_low_high(self):
        self.get_low_high().click()

    def get_high_low(self) -> WebElement:
        if not self._high_low:
            self._high_low = self.node.find_element(*HIGH_LOW)
        return self._high_low

    def click_high_low(self):
        self.get_high_low().click()

