from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent

IMAGE = (By.XPATH, "./div[2]/img[1]")
TITLE = (By.XPATH, "./div[3]/p")
DESCRIPTION = (By.XPATH, "./div[3]/span")


class HowItWorksComponent(BaseComponent):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self.image = None
        self.title = None
        self.description = None

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

