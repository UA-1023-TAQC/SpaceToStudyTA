from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.elements.base_element import BaseElement

LINK = (By.XPATH, "./div/a ")


class Link(BaseElement):

    def __init__(self, node: WebElement):
        super().__init__(node)

    def get_link_text(self) -> str:
        return self.node.find_element(*LINK).text

    def click_link(self):
        self.node.find_element(*LINK).click()
