import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent


GENERAL_STEP = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[1]/div[1]")
INTERESTS_STEP = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[1]/div[2]")
LANGUAGE_STEP = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[1]/div[3]")
PHOTO_STEP = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[1]/div[4]")
BACK_BUTTON = (By.XPATH, "//button[contains(text(), 'Back')]")
NEXT_BUTTON = (By.XPATH, "//button[contains(text(), 'Next')]")
FINISH_BUTTON = (By.XPATH, "//button[contains(text(), 'Finish')]")


class FirstLoginModal(BaseComponent):

    @allure.step("Get general step")
    def get_general_step(self) -> WebElement:
        return self.node.find_element(*GENERAL_STEP)

    @allure.step("Click general step")
    def click_general_step(self):
        self.get_general_step().click()
        from SpaceToStudy.ui.pages.first_login_student_modal.general_step import GeneralStepStudent
        return GeneralStepStudent(self.node.parent)

    @allure.step("Get interests step")
    def get_interests_step(self) -> WebElement:
        return self.node.find_element(*INTERESTS_STEP)

    @allure.step("Click interests step")
    def click_interests_step(self):
        self.get_interests_step().click()
        from SpaceToStudy.ui.pages.first_login_student_modal.interests_step import InterestsStepStudent
        return InterestsStepStudent(self.node.parent)

    @allure.step("Get language step")
    def get_language_step(self) -> WebElement:
        return self.node.find_element(*LANGUAGE_STEP)

    @allure.step("Click language step")
    def click_language_step(self):
        self.get_language_step().click()
        from SpaceToStudy.ui.pages.first_login_student_modal.language_step import LanguageStepStudent
        return LanguageStepStudent(self.node.parent)

    @allure.step("Get photo step")
    def get_photo_step(self) -> WebElement:
        return self.node.find_element(*PHOTO_STEP)

    @allure.step("Click photo step")
    def click_photo_step(self):
        self.get_photo_step().click()
        from SpaceToStudy.ui.pages.first_login_student_modal.photo_step import PhotoStepStudent
        return PhotoStepStudent(self.node.parent)
    
    @allure.step("Get back button")
    def get_back_button(self) -> WebElement:
        return self.node.find_element(*BACK_BUTTON)

    @allure.step("Click back button")
    def click_back_button(self):
        self.get_back_button().click()
        return self.node.parent

    @allure.step("Get next button")
    def get_next_button(self) -> WebElement:
        return self.node.find_element(*NEXT_BUTTON)

    @allure.step("Click next button")
    def click_next_button(self):
        self.get_next_button().click()
        return self.node.parent

    @allure.step("Get finish button")
    def get_finish_button(self) -> WebElement:
        return self.node.find_element(*FINISH_BUTTON)

    @allure.step("Click finish button")
    def click_finish_button(self):
        self.get_finish_button().click()
        return self.node.parent
