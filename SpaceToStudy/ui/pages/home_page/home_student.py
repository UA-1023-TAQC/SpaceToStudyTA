from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.elements.home_page.categories import PopularCategories
from SpaceToStudy.ui.elements.home_page.questions import AskedQuestions
from SpaceToStudy.ui.pages.base_page import BasePage
from SpaceToStudy.ui.pages.home_page.category_component import CategoryComponent
from SpaceToStudy.ui.pages.home_page.search_tutor_input_component import SearchTutorComponent

CATEGORIES = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[2]/div/a")
BUTTON_GO_TO_CATEGORIES = (By.XPATH, "//button[contains(text(), 'Go to categories')]")
BUTTON_FIND_TUTOR = (By.XPATH, "//a[contains(text(), 'Find tutor')]")

SEARCH_INPUT_BLOCK = (By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div/div[2]")


class HomePageStudent(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._categories = None
        self._button_go_to_categories = None
        self._button_find_tutor = None

    def get_categories(self) -> tuple[CategoryComponent]:
        if self._categories is None:
            categories = self.driver.find_elements(*CATEGORIES)
            self._categories = []
            for category in categories:
                self._categories.append(CategoryComponent(category))

        return self._categories


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