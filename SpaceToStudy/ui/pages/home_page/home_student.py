from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.elements.home_page.categories import PopularCategories
from SpaceToStudy.ui.elements.home_page.questions import AskedQuestions
from SpaceToStudy.ui.pages.base_page import BasePage
from SpaceToStudy.ui.pages.home_page.category_component import CategoryComponent
from SpaceToStudy.ui.pages.home_page.search_tutor_input_component import SearchTutorComponent

CATEGORIES_BTN = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[2]/button")
FIND_TUTOR_BTN = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[3]/a")
QUESTIONS = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[4]/div[2]")
CATEGORIES_BLOCK = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[2]")
CATEGORIES = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[2]/div/a")

SEARCH_INPUT_BLOCK = (By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div/div[2]")


class HomePageStudent(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._questions_block = None
        self._categories = None
        self._search_tutor = None

    def get_categories(self) -> tuple[CategoryComponent]:
        if self._categories is None:
            categories = self.driver.find_elements(*CATEGORIES)
            self._categories = []
            for category in categories:
                self._categories.append(CategoryComponent(category))

        return self._categories

    def get_search_input(self) -> WebElement:
        if not self._search_tutor:
            node = self.driver.find_element(*SEARCH_INPUT_BLOCK)
            self._search_tutor = SearchTutorComponent(node)
        return self._search_tutor

    def get_categories_btn(self):
        return self.driver.find_element(*CATEGORIES_BTN)

    def click_categories_btn(self):
        self.get_categories_btn().click()

    def get_find_tutor_btn(self):
        return self.driver.find_element(*FIND_TUTOR_BTN)

    def click_find_tutor_btn(self):
        self.get_find_tutor_btn().click()

    def get_text_questions(self):
        noda = self.driver.find_element(*QUESTIONS)
        self._questions_block = AskedQuestions(noda)
        return self._questions_block

    def get_blocks_popular_categories(self):
        noda = self.driver.find_element(*CATEGORIES_BLOCK)
        self._categories_block = PopularCategories(noda)
        return self._categories_block
