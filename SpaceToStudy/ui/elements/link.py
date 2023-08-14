from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.elements.base_element import BaseElement


LINK = (By.XPATH, "../div/a ")


class Link(BaseElement):

    def __init__(self, link, node: WebElement):
        super().__init__(link, node)
        self.link = None

    def get_link(self) -> str:
        if not self.link:
            self.link = self.node.find_element(*LINK).text
        return self.link

    def click_link(self):
        self.node.find_element(*LINK).click()
