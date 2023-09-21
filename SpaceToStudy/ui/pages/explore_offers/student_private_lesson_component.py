import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent

TITLE = (By.XPATH, './div/div[1]/p')
TEXT = (By.XPATH, './div/div[1]/span')
CREATE_REQUEST_BTN = (By.XPATH, './div/div[2]/button')
IMAGE = (By.XPATH, './img')


class StudentPrivateLessonComponent(BaseComponent):

    def __init__(self, node):
        super().__init__(node)

    @allure.step("Get title")
    def get_title(self) -> WebElement:
        return self.node.find_element(*TITLE)

    @allure.step("Get description")
    def get_text(self) -> WebElement:
        return self.node.find_element(*TEXT)

    @allure.step("Get create request button")
    def get_create_request_btn(self) -> WebElement:
        return self.node.find_element(*CREATE_REQUEST_BTN)

    @allure.step("Get image")
    def get_image(self) -> WebElement:
        return self.node.find_element(*IMAGE)

    @allure.step("Click on the create request button")
    def click_create_request_btn(self):
        return self.get_create_request_btn().click()
