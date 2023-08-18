from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent


FILTERS_SVG = (By.XPATH, '.div[1]/div/svg')
FILTER_TITLE = (By.XPATH, './div[1]/div/h6')
TUTORS_OFFERS = (By.XPATH, './div[2]/span[1]')
STUDENTS_REQUESTS = (By.XPATH, './div[2]/span[3]')
TOGGLE = (By.XPATH, './div[2]/span[2]/span[1]/input')
SORT_TITLE = (By.XPATH, './div[1]/div/h6')
SORT_LIST = (By.XPATH, '/div[3]/div[1]/div/div/div')
INLINE_CARD_BTN = (By.XPATH, '/div[3]/div[2]/button[1]')
GRID_CARD_BTN = (By.XPATH, '/div[3]/div[2]/button[2]')


class FilteringAndSortingComponent(BaseComponent):

    def __init__(self, node):
        super().__init__(node)

    def get_filters_svg(self) -> WebElement:
        return self.node.find_element(*FILTERS_SVG)

    def get_filter_title(self) -> WebElement:
        return self.node.find_element(*FILTER_TITLE)

    def get_tutors_offers(self) -> WebElement:
        return self.node.find_element(*TUTORS_OFFERS)

    def get_students_requests(self) -> WebElement:
        return self.node.find_element(*STUDENTS_REQUESTS)

    def get_toggle(self) -> WebElement:
        return self.node.find_element(*TOGGLE)

    def get_sort_title(self) -> WebElement:
        return self.node.find_element(*SORT_TITLE)

    def get_sort_list(self) -> WebElement:
        return self.node.find_element(*SORT_LIST)

    def get_inline_card_btn(self) -> WebElement:
        return self.node.find_element(*INLINE_CARD_BTN)

    def get_grid_card_btn(self) -> WebElement:
        return self.node.find_element(*GRID_CARD_BTN)

    def click_filter_title(self):
        return self.get_filter_title().click()

    def click_toggle(self):
        return self.get_toggle().click()

    def click_sort_list(self):
        return self.get_sort_list().click()

    def click_inline_card_btn(self):
        return self.get_inline_card_btn().click()

    def click_grid_card_btn(self):
        return self.get_grid_card_btn().click()

    def navigate_sort_list_up(self):
        return self.get_sort_list().send_keys(Keys.ARROW_UP)

    def navigate_sort_list_down(self):
        return self.get_sort_list().send_keys(Keys.ARROW_DOWN)
