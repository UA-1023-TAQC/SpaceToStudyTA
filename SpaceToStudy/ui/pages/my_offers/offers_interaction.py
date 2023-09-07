
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent
from SpaceToStudy.ui.pages.my_offers.sort_component import SortComponent

SEARCH_INPUT = (By.XPATH, "./div[1]/div/input")
INLINE_BTN = (By.XPATH, "./div[2]/div[2]/button[1]")
GRID_BTN = (By.XPATH, "./div[2]/div/button[2]")
SORT = (By.XPATH, "./div[2]/div[1]/div/div/div")


class OffersInteraction(BaseComponent):

    def __init__(self, node):
        self.node = node

    def get_search_input(self) -> WebElement:
        return self.node.find_element(*SEARCH_INPUT)

    def get_inline_btn(self) -> WebElement:
        return self.node.find_element(*INLINE_BTN)

    def get_grid_btn(self) -> WebElement:
        return self.node.find_element(*GRID_BTN)

    def set_search(self, text):
        self.get_search_input().send_keys(text)

    def click_inline_btn(self):
        self.get_inline_btn().click()

    def click_grid_btn(self):
        self.get_grid_btn().click()
        return self
    def get_sort(self) -> WebElement:
        return self.node.find_element(*SORT)

    def click_get_sort(self):
        self.get_sort().click()
        return SortComponent(self.node.find_element(By.XPATH, "/html/body/div[2]/div[3]"))
