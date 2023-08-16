from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

SEARCH_INPUT = (By.XPATH, "./div[1]/div/input")
INLINE_BTN = (By.XPATH, "./div[2]/div[2]/button[1]")
GRID_BTN = (By.XPATH, "./div[2]/div[2]/button[2]")


class OffersInteraction:

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
