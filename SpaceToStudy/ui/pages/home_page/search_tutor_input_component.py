from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent

INPUT = (By.XPATH, ".div[2]/div/div/input")
FIND_TUTOR_BTN = (By.XPATH, "./div[2]/a")
TITLE_INPUT_BLOCK = (By.XPATH, "./div[1]/p")
DESCRIPTION_INPUT_BLOCK = (By.XPATH, "./div[1]/p/span")
ICON_INPUT = (By.XPATH, "./div[2]/div/svg")


class SearchTutorComponent(BaseComponent):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self.node = node
        self._title_input_block = None
        self._description_input_block = None
        self._icon = None
        self._input = None
        self._find_tutor_btn = None

    def get_input(self) -> WebElement:
        if not self._input:
            self._input = self.node.find_element(*INPUT)
        return self._input

    def set_text(self, text):
        self.get_input().send_keys(text)

    def get_find_tutor_btn(self) -> WebElement:
        if not self._find_tutor_btn:
            self._find_tutor_btn = self.node.find_element(*FIND_TUTOR_BTN)
        return self._find_tutor_btn

    def click_find_tutor_btn(self):
        self.get_find_tutor_btn().click()

    def get_text_find_tutor_btn(self) -> str:
        return self.get_find_tutor_btn().text

    def get_title_input_block(self) -> str:
        if not self._title_input_block:
            self._title_input_block = self.node.find_element(*TITLE_INPUT_BLOCK)
        return self._title_input_block.text

    def get_description_input_block(self) -> str:
        if not self._description_input_block:
            self._description_input_block = self.node.find_element(*DESCRIPTION_INPUT_BLOCK)
        return self._description_input_block.text

    def get_icon_input(self) -> WebElement:
        if not self._icon:
            self._icon = self.node.find_element(*ICON_INPUT)
        return self._icon

