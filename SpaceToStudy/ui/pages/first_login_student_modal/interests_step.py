import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.elements.input_with_drop_down_list import InputDropDownList
from SpaceToStudy.ui.pages.first_login_student_modal.first_login_modal import FirstLoginModal
from SpaceToStudy.ui.pages.first_login_student_modal.language_step import LanguageStepStudent

STARTING_TEXT = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/div[2]/div[1]/p[1]")
IMAGE = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/div[1]/img")
MAIN_TUTORING_CATEGORY_INPUT = (
By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/div[2]/div[1]/div[1]/div")
MAIN_TUTORING_CATEGORY_LABEL = (
By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/div[2]/div[1]/div[1]/div/label")
SUBJECT_INPUT = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/div[2]/div[1]/div[2]/div")
SUBJECT_LABEL = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/div[2]/div[1]/div[2]/div/label")
ADD_SUBJECT_BUTTON = (By.XPATH, "//button[@data-testid='add-subject']/span")
FIRST_AUTOCOMPLETE_ELEMENT = (By.XPATH, "/html/body/div[3]/div/ul/li[1]")


class InterestsStepStudent(FirstLoginModal):

    def __init__(self, node):
        super().__init__(node)
        self._main_tutoring_category_input = None
        self._subject_input = None

    @allure.step("Get starting text")
    def get_starting_text(self) -> str:
        return self.node.find_element(*STARTING_TEXT).text

    @allure.step("Get image")
    def get_image(self) -> WebElement:
        return self.node.find_element(*IMAGE)

    @allure.step("Get main tutoring category input")
    def get_main_tutoring_category_input(self) -> InputDropDownList:
        if not self._main_tutoring_category_input:
            node = self.node.find_element(*MAIN_TUTORING_CATEGORY_INPUT)
            self._main_tutoring_category_input = InputDropDownList(node)
        return self._main_tutoring_category_input

    @allure.step("Get subject input")
    def get_subject_input(self) -> InputDropDownList:
        if not self._subject_input:
            node = self.node.find_element(*SUBJECT_INPUT)
            self._subject_input = InputDropDownList(node)
        return self._subject_input

    @allure.step("Get add subject button")
    def get_add_subject_button(self) -> WebElement:
        return self.node.find_element(*ADD_SUBJECT_BUTTON)

    @allure.step("Click add subject button")
    def click_add_subject_button(self):
        self.get_add_subject_button().click()
        return self

    @allure.step("Click next button")
    def click_next_button(self):
        self.get_next_button().click()
        return LanguageStepStudent(self.node)

    @allure.step("Click back button")
    def click_back_button(self):
        from SpaceToStudy.ui.pages.first_login_student_modal.general_step import GeneralStepStudent
        self.get_back_button().click()
        return GeneralStepStudent(self.node)
