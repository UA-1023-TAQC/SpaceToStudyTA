from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent

IMAGE = (By.XPATH, "./div/img")
TITLE = (By.XPATH, "./div/div/p")
DESCRIPTION = (By.XPATH, "./div/div/span")
BUTTON = (By.XPATH, "./button")


class CardComponent(BaseComponent):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self.image = None
        self.title = None
        self.description = None
        self.btn = None

    def get_image(self) -> WebElement:
        if not self.image:
            self.image = self.node.find_element(*IMAGE)
        return self.image

    def get_name(self) -> str:
        if not self.title:
            self.title = self.node.find_element(*TITLE)
        return self.title.text

    def get_offers(self) -> str:
        if not self.description:
            self.description = self.node.find_element(*DESCRIPTION)
        return self.description.text

    def get_btn_text(self) -> str:
        if not self.btn:
            self.btn = self.node.find_element(*BUTTON)
        return self.btn.text

    def click_btn(self):
        if not self.btn:
            self.btn = self.node.find_element(*BUTTON)
            self.btn.click()
