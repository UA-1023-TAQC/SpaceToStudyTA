from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent

NAME = (By.XPATH, "./a")


class NavigateComponent(BaseComponent):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self.name = None

    def click(self):
        self.node.click()
        return

    def get_name(self) -> WebElement:
        if not self.name:
            self.name = self.node.find_element(*NAME)
            return self.name
