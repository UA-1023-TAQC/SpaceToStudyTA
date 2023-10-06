from time import sleep

import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from SpaceToStudy.ui.pages.base_component import BaseComponent

CATEGORIES_INPUT = (By.XPATH, './div[1]/div/div/input')
SUBJECTS_INPUT = (By.XPATH, './div[2]/div/div/input')
SEARCH_BY_TUTOR_NAME_INPUT = (By.XPATH, './div[3]/div/div/input')
SEARCH_BTN = (By.XPATH, './div[3]/button')


class SearchByTutorNameComponent(BaseComponent):

    def __init__(self, node):
        super().__init__(node)

    @allure.step("Get categories input")
    def get_categories_input(self) -> WebElement:
        return self.node.find_element(*CATEGORIES_INPUT)

    @allure.step("Get categories input as a text")
    def get_categories_input_text(self) -> str:
        return self.get_categories_input().get_attribute("value")

    @allure.step("Get subjects input")
    def get_subjects_input(self) -> WebElement:
        return self.node.find_element(*SUBJECTS_INPUT)

    @allure.step("Get subjects input as a text")
    def get_subjects_input_text(self) -> str:
        return self.get_subjects_input().get_attribute("value")

    @allure.step("Get search by tutor name input")
    def get_search_by_tutor_name_input(self) -> WebElement:
        return self.node.find_element(*SEARCH_BY_TUTOR_NAME_INPUT)

    @allure.step("Get search by tutor name input as a text")
    def get_search_by_tutor_name_input_text(self) -> str:
        return self.get_search_by_tutor_name_input().get_attribute("value")

    @allure.step("Get search button")
    def get_search_btn(self) -> WebElement:
        return self.node.find_element(*SEARCH_BTN)

    @allure.step("Click on the categories input")
    def click_categories_input(self):
        return self.get_categories_input().click()

    @allure.step("Click on the subjects input")
    def click_subjects_input(self):
        return self.get_subjects_input().click()

    @allure.step("Click on the search button")
    def click_search_btn(self):
        from SpaceToStudy.ui.pages.explore_offers.explore_offers_page import ExploreOffersPage
        self.get_search_btn().click()
        WebDriverWait(self.node.parent, 3)
        return ExploreOffersPage(self.node)

    @allure.step("Set {text} into the categories input")
    def set_categories_input(self, text):
        self.get_categories_input().send_keys(text)
        return self

    @allure.step("Set {text} into the subjects input")
    def set_subjects_input(self, text):
        self.get_subjects_input().send_keys(text)
        return self

    @allure.step("Set {text} into the search by tutor name input")
    def set_search_by_tutor_name_input(self, text):
        self.get_search_by_tutor_name_input().send_keys(text)
        return self

    @allure.step("Scroll up categories input")
    def navigate_categories_input_up(self):
        return self.get_categories_input().send_keys(Keys.ARROW_UP)

    @allure.step("Scroll down categories input")
    def navigate_categories_input_down(self):
        self.get_categories_input().send_keys(Keys.ARROW_DOWN)
        return self

    @allure.step("Scroll up subjects input")
    def navigate_subjects_input_up(self):
        return self.get_subjects_input().send_keys(Keys.ARROW_UP)

    @allure.step("Scroll down subjects input")
    def navigate_subjects_input_down(self):
        self.get_subjects_input().send_keys(Keys.ARROW_DOWN)
        return self

    @allure.step("Choose categories item")
    def choose_categories_item(self):
        self.get_categories_input().send_keys(Keys.ENTER)
        sleep(0.5)
        return self

    @allure.step("Choose subjects item")
    def choose_subjects_item(self):
        self.get_subjects_input().send_keys(Keys.ENTER)
        sleep(0.5)
        return self
