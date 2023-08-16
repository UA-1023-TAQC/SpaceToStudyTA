from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_page import BasePage
from SpaceToStudy.ui.pages.home_page.category_component import CategoryComponent
from SpaceToStudy.ui.pages.home_page.how_it_works_component_student import HowItWorksComponentStudent

CATEGORIES = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[2]/div/a")
BUTTON_GO_TO_CATEGORIES = (By.XPATH, "//button[contains(text(), 'Go to categories')]")
BUTTON_FIND_TUTOR = (By.XPATH, "//a[contains(text(), 'Find tutor')]")

SEARCH_INPUT_BLOCK = (By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div/div[2]")

IMG_SEARCH_BLOCK = (By.XPATH, "/html/body/div/div/div[2]/div/div[1]/img")

HOW_IT_WORKS_BLOCK_STUDENT = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[3]/div[1]")
HOW_IT_WORKS_BLOCK_SELECT_A_TUTOR_STUDENT = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[3]/div[2]/div[1]")
HOW_IT_WORKS_BLOCK_SEND_REQUEST_STUDENT = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[3]/div[2]/div[2]")
HOW_IT_WORKS_BLOCK_START_LEARNING_STUDENT = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[3]/div[2]/div[3]")
HOW_IT_WORKS_BLOCK_WRITE_FEEDBACK_STUDENT = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[3]/div[2]/div[4]")


class HomePageStudent(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._categories = None
        self._button_go_to_categories = None
        self._button_find_tutor = None
        self._img_search_block = None
        self._how_it_works_block_student = None
        self._select_a_tutor_student = None
        self._send_request_student = None
        self._start_learning_student = None
        self._write_feedback_student = None

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

    def get_img_search_block(self) -> WebElement:
        if not self._img_search_block:
            self._img_search_block = self.driver.find_element(*IMG_SEARCH_BLOCK)
        return self._img_search_block

    def get_how_it_works_block_student(self) -> WebElement:
        if not self._how_it_works_block_student:
            node = self.driver.find_element(*HOW_IT_WORKS_BLOCK_STUDENT)
            self._how_it_works_block_student = HowItWorksComponentStudent(node)
        return self._how_it_works_block_student

    def get_select_a_tutor_items_student(self) -> WebElement:
        if not self._select_a_tutor_student:
            node = self.driver.find_element(*HOW_IT_WORKS_BLOCK_SELECT_A_TUTOR_STUDENT)
            self._select_a_tutor_student = HowItWorksComponentStudent(node)
        return self._select_a_tutor_student

    def get_send_request_items_student(self) -> WebElement:
        if not self._send_request_student:
            node = self.driver.find_element(*HOW_IT_WORKS_BLOCK_SEND_REQUEST_STUDENT)
            self._send_request_student = HowItWorksComponentStudent(node)
        return self._send_request_student

    def get_start_learning_items_student(self) -> WebElement:
        if not self._start_learning_student:
            node = self.driver.find_element(*HOW_IT_WORKS_BLOCK_START_LEARNING_STUDENT)
            self._start_learning_student = HowItWorksComponentStudent(node)
        return self._start_learning_student

    def get_write_feedback_items_student(self) -> WebElement:
        if not self._write_feedback_student:
            node = self.driver.find_element(*HOW_IT_WORKS_BLOCK_WRITE_FEEDBACK_STUDENT)
            self._write_feedback_student = HowItWorksComponentStudent(node)
        return self._write_feedback_student
