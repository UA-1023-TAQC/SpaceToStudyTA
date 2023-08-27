from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_page import BasePage
from SpaceToStudy.ui.pages.home_page.category_component import CategoryComponent
from SpaceToStudy.ui.pages.home_page.how_it_works_component_student import HowItWorksComponentStudent
from SpaceToStudy.ui.pages.home_page.questions_component import QuestionsComponent
from SpaceToStudy.ui.pages.home_page.search_tutor_input_component import SearchTutorComponent

CATEGORIES_BLOCK = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[2]")
CATEGORIES = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[2]/div/a")
BUTTON_GO_TO_CATEGORIES = (By.XPATH, "//button[contains(text(), 'Go to categories')]")
BUTTON_FIND_TUTOR = (By.XPATH, "//a[contains(text(), 'Find tutor')]")

SEARCH_INPUT_BLOCK = (By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div")

HOW_IT_WORKS_BLOCK_STUDENT = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[3]")

IMG_SEARCH_BLOCK = (By.XPATH, "/html/body/div/div/div[2]/div/div[1]/img")

QUESTIONS_BLOCK = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[4]/div[1]")
QUESTIONS_ITEMS = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[4]/div[2]/div")


class HomePageStudent(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._categories = None
        self._button_go_to_categories = None
        self._button_find_tutor = None
        self._questions_block = None
        self._questions_items = None
        self._search_tutor = None
        self._img_search_block = None
        self._how_it_works_block_student = None

    def get_categories(self) -> tuple[CategoryComponent]:
        if self._categories is None:
            categories = self.driver.find_elements(*CATEGORIES)
            self._categories = []
            for category in categories:
                self._categories.append(CategoryComponent(category))

        return self._categories

    def get_search_input(self) -> SearchTutorComponent:
        if not self._search_tutor:
            _search_tutor = self.driver.find_element(*SEARCH_INPUT_BLOCK)
            self._search_tutor = SearchTutorComponent(_search_tutor)
        return self._search_tutor

    def get_button_go_to_categories(self) -> WebElement:
        if not self._button_go_to_categories:
            self._button_go_to_categories = self.driver.find_element(*BUTTON_GO_TO_CATEGORIES)
        return self._button_go_to_categories

    def get_text_button_go_to_categories(self) -> str:
        return self.get_button_go_to_categories().text

    def click_button_go_to_categories(self):
        self.get_button_go_to_categories().click()
        return self

    def get_button_find_tutor(self) -> WebElement:
        if not self._button_find_tutor:
            self._button_find_tutor = self.driver.find_element(*BUTTON_FIND_TUTOR)
        return self._button_find_tutor

    def get_text_button_find_tutor(self) -> str:
        return self.get_button_find_tutor().text

    def click_button_find_tutor(self):
        self.get_button_find_tutor().click()
        return self

    def get_questions_block(self) -> QuestionsComponent:
        if not self._questions_block:
            _questions_block = self.driver.find_element(*QUESTIONS_BLOCK)
            self._questions_block = QuestionsComponent(_questions_block)
        return self._questions_block

    def get_questions_items(self) -> list[QuestionsComponent]:
        if self._questions_items is None:
            _questions_items = self.driver.find_elements(*QUESTIONS_ITEMS)
            self._questions_items = []
            for questions_item in _questions_items:
                self._questions_items.append(CategoryComponent(questions_item))
        return self._questions_items

    def get_img_search_block(self) -> WebElement:
        if not self._img_search_block:
            self._img_search_block = self.driver.find_element(*IMG_SEARCH_BLOCK)
        return self._img_search_block

    def get_how_it_works_block_student(self) -> HowItWorksComponentStudent:
        if not self._how_it_works_block_student:
            _how_it_works_block_student = self.driver.find_element(*HOW_IT_WORKS_BLOCK_STUDENT)
            self._how_it_works_block_student = HowItWorksComponentStudent(_how_it_works_block_student)
        return self._how_it_works_block_student
