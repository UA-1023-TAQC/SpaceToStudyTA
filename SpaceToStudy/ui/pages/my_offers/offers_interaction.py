from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent

SEARCH_INPUT = (By.XPATH, "./div[1]/div/input")
INLINE_BTN = (By.XPATH, "./div[2]/div[2]/button[1]")
GRID_BTN = (By.XPATH, "./div[2]/div[2]/button[2]")


class OffersInteraction(BaseComponent):

    def __init__(self, node: WebElement):
        super().__init__(node)
        self._search_input = None
        self._inline_btn = None
        self._grid_btn = None

    def get_search_input(self) -> WebElement:
        if not self._search_input:
            self._search_input = self.node.find_element(*SEARCH_INPUT)
        return self._search_input

    def get_inline_btn(self) -> WebElement:
        if not self._inline_btn:
            self._inline_btn = self.node.find_element(*INLINE_BTN)
        return self._inline_btn

    def get_grid_btn(self) -> WebElement:
        if not self._grid_btn:
            self._grid_btn = self.node.find_element(*GRID_BTN)
        return self._grid_btn

    def set_search(self, text):
        self.get_search_input().send_keys(text)

    def click_inline_btn(self):
        self.get_inline_btn().click()

    def click_grid_btn(self):
        self.get_grid_btn().click()
