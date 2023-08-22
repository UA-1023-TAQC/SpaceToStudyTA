from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent

CATEGORIES_INPUT = (By.XPATH, './div[1]/div/div/input')
SUBJECTS_INPUT = (By.XPATH, './div[2]/div/div/input')
SEARCH_BY_TUTOR_NAME_INPUT = (By.XPATH, './div[3]/div/div/input')
SEARCH_BTN = (By.XPATH, './div[3]/button')


class SearchByTutorNameComponent(BaseComponent):

    def __init__(self, node):
        super().__init__(node)

    def get_categories_input(self) -> WebElement:
        return self.node.find_element(*CATEGORIES_INPUT)

    def get_subjects_input(self) -> WebElement:
        return self.node.find_element(*SUBJECTS_INPUT)

    def get_search_by_tutor_name_input(self) -> WebElement:
        return self.node.find_element(*SEARCH_BY_TUTOR_NAME_INPUT)

    def get_search_btn(self) -> WebElement:
        return self.node.find_element(*SEARCH_BTN)

    def click_categories_input(self):
        return self.get_categories_input().click()

    def click_subjects_input(self):
        return self.get_subjects_input().click()

    def click_search_btn(self):
        return self.get_search_btn().click()

    def set_categories_input(self, text):
        self.get_categories_input().send_keys(text)

    def set_subjects_input(self, text):
        self.get_subjects_input().send_keys(text)

    def set_search_by_tutor_name_input(self, text):
        self.get_search_by_tutor_name_input().send_keys(text)

    def navigate_categories_input_up(self):
        return self.get_categories_input().send_keys(Keys.ARROW_UP)

    def navigate_categories_input_down(self):
        return self.get_categories_input().send_keys(Keys.ARROW_DOWN)

    def navigate_subjects_input_up(self):
        return self.get_subjects_input().send_keys(Keys.ARROW_UP)

    def navigate_subjects_input_down(self):
        return self.get_subjects_input().send_keys(Keys.ARROW_DOWN)
