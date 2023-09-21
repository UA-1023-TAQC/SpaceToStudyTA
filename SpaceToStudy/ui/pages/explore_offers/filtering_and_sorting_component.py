from time import sleep

import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent
from SpaceToStudy.ui.pages.explore_offers.filters_sidebar_component import FiltersSidebarComponent

FILTERS_SVG = (By.XPATH, '.div[1]/div/svg')
FILTER_TITLE = (By.XPATH, './div[1]/div/h6')
FILTER_QUANTITY = (By.XPATH, './/*[@data-testid="filters-qty"]')
TUTORS_OFFERS = (By.XPATH, './div[2]/span[1]')
STUDENTS_REQUESTS = (By.XPATH, './div[2]/span[3]')
TOGGLE = (By.XPATH, './div[2]/span[2]/span[1]/input')
SORT_TITLE = (By.XPATH, './div[1]/div/h6')
SORT_LIST = (By.XPATH, './div[3]/div[1]/div/div/div')
INLINE_CARD_BTN = (By.XPATH, './div[3]/div[2]/button[1]')
GRID_CARD_BTN = (By.XPATH, './div[3]/div[2]/button[2]')

FILTERS_SIDEBAR_COMPONENT = (By.XPATH, "/html/body/div[2]/div[3]")


class FilteringAndSortingComponent(BaseComponent):

    def __init__(self, node):
        super().__init__(node)
        self._filters_sidebar_component = None

    @allure.step("Get filters svg")
    def get_filters_svg(self) -> WebElement:
        return self.node.find_element(*FILTERS_SVG)

    @allure.step("Get filter title")
    def get_filter_title(self) -> WebElement:
        return self.node.find_element(*FILTER_TITLE)

    @allure.step("Get filter quantity")
    def get_filter_quantity(self) -> WebElement:
        return self.node.find_element(*FILTER_QUANTITY)

    @allure.step("Get number of filter's quantity ")
    def get_filter_quantity_number(self) -> int:
        return int(self.node.find_element(*FILTER_QUANTITY).text)

    @allure.step("Get tutors offers")
    def check_filter_quantity_is_visible(self):
        return len(self.node.find_elements(*FILTER_QUANTITY)) != 0

    def get_tutors_offers(self) -> WebElement:
        return self.node.find_element(*TUTORS_OFFERS)

    @allure.step("Get students' requests")
    def get_students_requests(self) -> WebElement:
        return self.node.find_element(*STUDENTS_REQUESTS)

    @allure.step("Get toggle button")
    def get_toggle(self) -> WebElement:
        return self.node.find_element(*TOGGLE)

    @allure.step("Get sort title")
    def get_sort_title(self) -> WebElement:
        return self.node.find_element(*SORT_TITLE)

    @allure.step("Get sort list")
    def get_sort_list(self) -> WebElement:
        return self.node.find_element(*SORT_LIST)

    @allure.step("Get inline card button")
    def get_inline_card_btn(self) -> WebElement:
        return self.node.find_element(*INLINE_CARD_BTN)

    @allure.step("Get grid card button")
    def get_grid_card_btn(self) -> WebElement:
        return self.node.find_element(*GRID_CARD_BTN)

    @allure.step("Click on the filter title")
    def click_filter_title(self):
        self.get_filter_title().click()
        sleep(0.5)
        return self

    @allure.step("Click on the toggle button")
    def click_toggle(self):
        return self.get_toggle().click()

    @allure.step("Click on the sort list")
    def click_sort_list(self):
        return self.get_sort_list().click()

    @allure.step("Click on the inline card button")
    def click_inline_card_btn(self):
        from SpaceToStudy.ui.pages.explore_offers.explore_offers_page import ExploreOffersPage
        self.get_inline_card_btn().click()
        return ExploreOffersPage(self.node.parent)

    @allure.step("Click on the grid card button")
    def click_grid_card_btn(self):
        from SpaceToStudy.ui.pages.explore_offers.explore_offers_page import ExploreOffersPage
        self.get_grid_card_btn().click()
        return ExploreOffersPage(self.node.parent)

    @allure.step("Scroll up the sort list")
    def navigate_sort_list_up(self):
        return self.get_sort_list().send_keys(Keys.ARROW_UP)

    @allure.step("Scroll down the sort list")
    def navigate_sort_list_down(self):
        return self.get_sort_list().send_keys(Keys.ARROW_DOWN)

    @allure.step("Get filters sidebar component")
    def get_filters_sidebar_component(self):
        new_node = self.node.find_element(*FILTERS_SIDEBAR_COMPONENT)
        if not self._filters_sidebar_component:
            self._filters_sidebar_component = FiltersSidebarComponent(new_node)
            return self._filters_sidebar_component
