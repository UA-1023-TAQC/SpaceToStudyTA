from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent

TITLE = (By.XPATH, "./div[2]/p")
IMG = (By.XPATH, "./div[1]/svg")
VALUE = (By.XPATH, "./div[2]/span")

class InfoComponentOneValue(BaseComponent):

    def __init__(self, node):
        super().__init__(node)
        self._title = None
        self._img = None
        self._value = None

    def get_title(self) -> str:
        if not self._title:
            self._title = self.node.find_element(*TITLE)
        return self._title.text

    def get_img(self) -> WebElement:
        if not self._img:
            self._img = self.node.find_element(*IMG)
        return self._img

    def get_value(self) -> str:
        if not self._value:
            self._value = self.node.find_element(*VALUE)
        return self._value.text