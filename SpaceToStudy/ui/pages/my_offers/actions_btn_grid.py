from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

EDIT_BTN_GRID = (By.XPATH, "./button")
VIEW_DETAILS_BTN_GRID = (By.XPATH, "./a")


class ActionsBtnGrid:

    def __init__(self, node):
        self.node = node

    def get_edit_btn_grid(self) -> WebElement:
        return self.node.find_element(*EDIT_BTN_GRID)

    def get_view_details_btn_grid(self) -> WebElement:
        return self.node.find_element(*VIEW_DETAILS_BTN_GRID)

    def click_edit_btn_grid(self):
        self.get_edit_btn_grid().click()

    def click_view_details_btn_grid(self):
        self.get_view_details_btn_grid().click()
