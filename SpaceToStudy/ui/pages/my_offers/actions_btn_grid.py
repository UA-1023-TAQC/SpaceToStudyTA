import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

EDIT_BTN_GRID = (By.XPATH, "./button")
VIEW_DETAILS_BTN_GRID = (By.XPATH, "./a")


class ActionsBtnGrid:
    @allure.step("Init a hamburger navigation of the Actions for an offer in the my offers table")
    def __init__(self, node):
        self.node = node

    @allure.step("Get 'Edit offer' option in the offer Actions hamburger navigation in the my offers table")
    def get_edit_btn_grid(self) -> WebElement:
        return self.node.find_element(*EDIT_BTN_GRID)

    @allure.step("Get 'View details' option in the offer Actions hamburger navigation in the my offers table")
    def get_view_details_btn_grid(self) -> WebElement:
        return self.node.find_element(*VIEW_DETAILS_BTN_GRID)

    @allure.step("Click 'Edit offer' option in the offer Actions hamburger navigation in the my offers table")
    def click_edit_btn_grid(self):
        self.get_edit_btn_grid().click()

    @allure.step("Click 'View details' option in the offer Actions hamburger navigation in the my offers table")
    def click_view_details_btn_grid(self):
        self.get_view_details_btn_grid().click()
