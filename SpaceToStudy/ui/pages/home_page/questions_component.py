from time import sleep

import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent

NAME_QUESTIONS_BLOCK = (By.XPATH, "./p")
DESCRIPTION_QUESTIONS_BLOCK = (By.XPATH, "./span")
HOW_TO_FIND_A_TUTOR_ITEM_TITLE = (By.XPATH, "./div[1]/div[1]/h6")
HOW_TO_FIND_A_TUTOR_ITEM_DESCRIPTION = (By.XPATH, "./div[2]/div/div/div/div/p")
ITEM_BLOCK = (By.XPATH, "./div[1]")


class QuestionsComponent(BaseComponent):

    def __init__(self, node: WebElement):
        super().__init__(node)
        self._name_questions_block = None
        self._description_questions_block = None
        self._description_items = None
        self._title_items = None

    @allure.step("Get the item block")
    def get_item_block(self) -> WebElement:
        return self.node.find_element(*ITEM_BLOCK)

    @allure.step("Get the background color of item block")
    def get_background_color_of_item_block(self) -> str:
        return self.get_item_block().value_of_css_property("background-color")

    @allure.step("Go to item N={item_sequence_number} by pressing tab")
    def go_to_item_by_pressing_tab(self, item_sequence_number=1):
        from SpaceToStudy.ui.pages.home_page.home_student import HomePageStudent
        home = HomePageStudent(self.node.parent)
        number_of_tabs_from_input_field_till_first_item = 9
        home.get_search_input().get_input() \
            .send_keys(Keys.TAB * (number_of_tabs_from_input_field_till_first_item + item_sequence_number))
        sleep(0.5)

    @allure.step("Get the name of questions block")
    def get_name_questions_block(self) -> str:
        if not self._name_questions_block:
            self._name_questions_block = self.node.find_element(*NAME_QUESTIONS_BLOCK)
        return self._name_questions_block.text

    @allure.step("Get text from the description of questions block")
    def get_description_questions_block(self) -> str:
        if not self._description_questions_block:
            self._description_questions_block = self.node.find_element(*DESCRIPTION_QUESTIONS_BLOCK)
        return self._description_questions_block.text

    @allure.step("Get the title of items")
    def get_title_items(self) -> WebElement:
        if not self._title_items:
            self._title_items = self.node.find_element(*HOW_TO_FIND_A_TUTOR_ITEM_TITLE)
        return self._title_items

    @allure.step("Get the text of title items")
    def get_text_title_items(self) -> str:
        return self.get_title_items().text

    @allure.step("Click on title items")
    def click_title_items(self):
        return self.get_title_items().click()

    @allure.step("Get the description of items")
    def get_description_items(self) -> str:
        if not self._description_items:
            self._description_items = self.node.find_element(*HOW_TO_FIND_A_TUTOR_ITEM_DESCRIPTION)
        return self._description_items.text
