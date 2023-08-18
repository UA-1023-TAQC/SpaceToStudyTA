from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent

EDIT_BTN_GRID = (By.XPATH, "./button")
VIEW_DETAILS_BTN_GRID = (By.XPATH, "./a")


class ActionsBtnGrid(BaseComponent):

    def __init__(self, node: WebElement):
        super().__init__(node)
        self._edit_btn_grid = None
        self._view_details_btn_grid = None

    def get_edit_btn_grid(self) -> WebElement:
        if not self._edit_btn_grid:
            self._edit_btn_grid = self.node.find_element(*EDIT_BTN_GRID)
        return self._edit_btn_grid

    def get_view_details_btn_grid(self) -> WebElement:
        if not self._view_details_btn_grid:
            self._view_details_btn_grid = self.node.find_element(*VIEW_DETAILS_BTN_GRID)
        return self._view_details_btn_grid

    def click_edit_btn_grid(self):
        self.get_edit_btn_grid().click()

    def click_view_details_btn_grid(self):
        self.get_view_details_btn_grid().click()
