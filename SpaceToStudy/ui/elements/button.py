from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.elements.base_element import BaseElement


class Button(BaseElement):
    def __init__(self, node: WebElement):
        super().__init__(node)

    def get_button(self):
        return self.node

    def click_button(self):
        self.get_button().click()
