import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent

IMAGE = (By.XPATH, "./img")
NAME = (By.XPATH, "./div/p")
OFFERS = (By.XPATH, "./div/span")


class CategoryComponent(BaseComponent):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self.image = None
        self.name = None
        self.offers = None

    @allure.step("Click element")
    def click(self):
        self.node.click()
        return

    @allure.step("Get image")
    def get_image(self) -> WebElement:
        if not self.image:
            self.image = self.node.find_element(*IMAGE)
        return self.image

    @allure.step("Get name")
    def get_name(self) -> str:
        if not self.name:
            self.name = self.node.find_element(*NAME)
        return self.name.text

    @allure.step("Get offers text")
    def get_offers(self) -> str:
        if not self.offers:
            self.offers = self.node.find_element(*OFFERS)
        return self.offers.text
