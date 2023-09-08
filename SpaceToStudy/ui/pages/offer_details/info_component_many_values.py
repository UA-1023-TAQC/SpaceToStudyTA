from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent
from SpaceToStudy.ui.pages.offer_details.value import Value

TITLE = (By.XPATH, "./div[2]/p")
IMG = (By.XPATH, "./div[1]/svg")
VALUES = (By.XPATH, "./div[2]/span/div")


class InfoComponentManyValues(BaseComponent):

    def __init__(self, node):
        super().__init__(node)
        self._title = None
        self._img = None
        self._values = None

    def get_title(self) -> str:
        if not self._title:
            self._title = self.node.find_element(*TITLE)
        return self._title.text

    def get_img(self) -> WebElement:
        if not self._img:
            self._img = self.node.find_element(*IMG)
        return self._img

    def get_values(self) -> list[Value]:
        if not self._values:
            value = self.node.find_elements(*VALUES)
            self._values = [Value(val) for val in value]
        return self._values