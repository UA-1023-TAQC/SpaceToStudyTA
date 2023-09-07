from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent

TEXT = (By.XPATH, "./span")
IMG = (By.XPATH, "./p/svg")

class Value(BaseComponent):

    def __init__(self, node):
        super().__init__(node)
        self._text = None
        self._img = None

    def get_text(self) -> str:
        if not self._text:
            self._text = self.node.find_element(*TEXT)
        return self._text.text

    def get_img(self) -> WebElement:
        if not self._img:
            self._img = self.node.find_element(*IMG)
        return self._img
