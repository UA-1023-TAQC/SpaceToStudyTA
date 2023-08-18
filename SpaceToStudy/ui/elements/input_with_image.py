from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.elements.input import Input

ICON = (By.XPATH, "./button/svg")


class InputWithImage(Input):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self.icon = None

    def get_icon(self):
        if not self.icon:
            self.icon = self.node.find_element(*ICON)
        return self.icon

    def click_icon(self):
        self.icon.click()
