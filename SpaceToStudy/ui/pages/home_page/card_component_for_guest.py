import allure
from time import sleep

from selenium.common import NoSuchElementException
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

    @allure.step("Get image")
    def get_image(self) -> WebElement:
        if not self.image:
            self.image = self.node.find_element(*IMAGE)
        return self.image

    @allure.step("Get a 'name' element")
    def get_name_element(self) -> WebElement:
        if not self.title:
            self.title = self.node.find_element(*TITLE)
        return self.title

    @allure.step("Get a 'name' element title")
    def get_name(self) -> str:
        return self.get_name_element().text

    @allure.step("Get a card description element")
    def get_offers_element(self) -> str:
        if not self.description:
            self.description = self.node.find_element(*DESCRIPTION)
        return self.description

    @allure.step("Get a card description text")
    def get_offers(self) -> str:
        return self.get_offers_element().text

    @allure.step("Get button")
    def get_btn(self) -> WebElement:
        if not self.btn:
            self.btn = self.node.find_element(*BUTTON)
        return self.btn

    @allure.step("Get button text")
    def get_btn_text(self) -> str:
        return self.get_btn().text

    @allure.step("Click button")
    def click_btn(self):
        from SpaceToStudy.ui.pages.sign_up_modal.sign_up_modal import RegistrationModal
        self.get_btn().click()
        sleep(1)
        return RegistrationModal(self.node)
