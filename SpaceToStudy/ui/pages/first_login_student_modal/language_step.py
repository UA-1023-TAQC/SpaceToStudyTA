import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.elements.input_with_drop_down_list import InputDropDownList
from SpaceToStudy.ui.pages.first_login_student_modal.first_login_modal import FirstLoginModal
from SpaceToStudy.ui.pages.first_login_student_modal.photo_step import PhotoStepStudent

IMAGE = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/div[1]/img")
STARTING_TEXT = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/div[2]/div[1]/p")
NATIVE_LANGUAGE_LABEL = (By.XPATH, "//div[@data-testid='language']/label")
NATIVE_LANGUAGE_INPUT = (By.XPATH, "//div[@data-testid='language']")
FIRST_AUTOCOMPLETE_ELEMENT = (By.XPATH, "/html/body/div[3]/div/ul/li[1]")


class LanguageStepStudent(FirstLoginModal):

    def __init__(self, node):
        super().__init__(node)
        self._native_language = None

    @allure.step("Get image")
    def get_image(self) -> WebElement:
        return self.node.find_element(*IMAGE)

    @allure.step("Get starting text")
    def get_starting_text(self) -> str:
        return self.node.find_element(*STARTING_TEXT).text

    @allure.step("Get native language input")
    def get_native_language_input(self) -> InputDropDownList:
        if not self._native_language:
            node = self.node.find_element(*NATIVE_LANGUAGE_INPUT)
            self._native_language = InputDropDownList(node)
        return self._native_language

    @allure.step("Click next button")
    def click_next_button(self):
        self.get_next_button().click()
        return PhotoStepStudent(self.node)

    @allure.step("Click back button")
    def click_back_button(self):
        from SpaceToStudy.ui.pages.first_login_student_modal.interests_step import InterestsStepStudent
        self.get_back_button().click()
        return InterestsStepStudent(self.node)
