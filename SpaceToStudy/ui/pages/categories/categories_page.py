from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.elements.input_with_drop_down_list import InputDropDownList
from SpaceToStudy.ui.pages.base_page import BasePage
from SpaceToStudy.ui.pages.explore_offers.explore_offers_page import ExploreOffersPage

CATEGORIES_TITLE = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/p')
CATEGORIES_SUBTEXT = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/span')
SHOW_ALL_OFFERS_BTN = (By.XPATH, '//a[text()="Show all offers"]')
SEARCH_BTN = (By.XPATH, '//button[text()="Search"]')
SEARCH_INPUT = (By.XPATH, '//input[contains(@role, "combobox")]/../..')
SEARCH_FIELD_HELP_TEXT = (By.XPATH, '//*[@id="mui-2488-label"]')


class CategoriesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_categories_title(self) -> str:
        return self.driver.find_element(*CATEGORIES_TITLE).text

    def get_categories_subtext(self) -> str:
        return self.driver.find_element(*CATEGORIES_SUBTEXT).text

    def get_show_all_offers_btn(self) -> WebElement:
        return self.driver.find_element(*SHOW_ALL_OFFERS_BTN)

    def click_show_all_offers_btn(self):
        self.get_show_all_offers_btn().click()
        return ExploreOffersPage(self.driver)

    def get_search_btn(self) -> WebElement:
        return self.driver.find_element(*SEARCH_BTN)

    def click_search_btn(self):
        self.get_search_btn().click()

    def get_search_input(self) -> InputDropDownList:
        node = self.driver.find_element(*SEARCH_INPUT)
        return InputDropDownList(node)

    def get_search_field_help_text(self) -> str:
        return self.driver.find_element(*SEARCH_FIELD_HELP_TEXT).text
