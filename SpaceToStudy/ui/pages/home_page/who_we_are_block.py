from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent

TITLE = (By.XPATH, "./div[1]/p")
DESC = (By.XPATH, "./div[1]/span")
VIDEO = (By.XPATH, "./div[2]")

class WhoWeAreBlock(BaseComponent):
    def __init__(self, node):
        super().__init__(node)
        self._title = None
        self._desc = None
        self._video = None

    def get_title(self) -> str:
        if not self._title:
            self._title = self.node.find_element(*TITLE)
        return self._title.text

    def get_desc(self) -> str:
        if not self._desc:
            self._desc = self.node.find_element(*DESC)
        return self._desc.text

    def get_video(self) -> WebElement:
        if not self._video:
            self._video = self.node.find_element(*VIDEO)
        return self._video