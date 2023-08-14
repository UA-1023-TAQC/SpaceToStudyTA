from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent

INPUT = (By.XPATH, "./div/div/input")
FIND_TUTOR_BTN = (By.XPATH, "./a")


class SearchTutorComponent(BaseComponent):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self.node = node

    def get_input(self) -> WebElement:
        return self.node.find_element(*INPUT)

    def set_text(self, text):
        self.get_input().send_keys(text)

    def get_find_tutor_btn(self) -> WebElement:
        return self.node.find_element(*FIND_TUTOR_BTN)

    def click_find_tutor_btn(self):
        self.get_find_tutor_btn().click()

    def get_text_find_tutor_btn(self) -> str:
        return self.get_find_tutor_btn().text

