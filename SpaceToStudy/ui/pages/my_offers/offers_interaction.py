import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent
from SpaceToStudy.ui.pages.my_offers.sort_component import SortComponent

SEARCH_INPUT = (By.XPATH, "./div[1]/div/input")
INLINE_BTN = (By.XPATH, "./div[2]/div[2]/button[1]")
GRID_BTN = (By.XPATH, "./div[2]/div/button[2]")
SORT = (By.XPATH, "./div[2]/div[1]/div/div/div")


class OffersInteraction(BaseComponent):
    @allure.step("Get the search input area 'Search user name or title' on the My Offers page")
    def get_search_input(self) -> WebElement:
        return self.node.find_element(*SEARCH_INPUT)

    @allure.step("Get the inline button for displaying offers in the table format on the My Offers page")
    def get_inline_btn(self) -> WebElement:
        return self.node.find_element(*INLINE_BTN)

    @allure.step("Get the grid button for displaing offers in the card format on the My Offers page")
    def get_grid_btn(self) -> WebElement:
        return self.node.find_element(*GRID_BTN)

    @allure.step("Set an input data {text} in the search area 'Search user name or title' on the My Offers page")
    def set_search(self, text):
        self.get_search_input().send_keys(text)

    @allure.step("Click the inline button to display offers in the table format on the My Offers page")
    def click_inline_btn(self):
        self.get_inline_btn().click()

    @allure.step("Get the grid button to display offers in the card format on the My Offers page")
    def click_grid_btn(self):
        self.get_grid_btn().click()
        return self
    
    @allure.step("Get the offers sorting button (dropdown menu) when offers are displayed in a card format on the My Offers page")
    def get_sort(self) -> WebElement:
        return self.node.find_element(*SORT)

    @allure.step("Click the offers sorting button (dropdown menu) when offers are displayed in a card format on the My Offers page")
    def click_get_sort(self):
        self.get_sort().click()
        return SortComponent(self.node.find_element(By.XPATH, "/html/body/div[2]/div[3]"))
