import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_page import BasePage


STARTING_TEXT = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/div[2]/div[1]/p[1]")
IMAGE = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/div[1]/img")
MAIN_TUTORING_CATEGORY_INPUT = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div/input")
MAIN_TUTORING_CATEGORY_LABEL = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/div[2]/div[1]/div[1]/div/label")
SUBJECT_INPUT = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div/input")
SUBJECT_LABEL = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/div[2]/div[1]/div[2]/div/label")
ADD_SUBJECT_BUTTON = (By.XPATH, "//button[@data-testid='add-subject']/span")


class InterestsPageStudent(BasePage):

    @allure.step("Get starting text")
    def get_starting_text(self) -> str:
        return self.driver.find_element(*STARTING_TEXT).text

    @allure.step("Get image")
    def get_image(self) -> WebElement:
        return self.driver.find_element(*IMAGE)

    @allure.step("Get main tutoring category input")
    def get_main_tutoring_category_input(self) -> WebElement:
        return self.driver.find_element(*MAIN_TUTORING_CATEGORY_INPUT)

    @allure.step("Set main tutoring category input")
    def set_main_tutoring_category_input(self, text):
        self.get_main_tutoring_category_input().send_keys(text)

    @allure.step("Get main tutoring category label")
    def get_main_tutoring_category_label(self) -> WebElement:
        return self.driver.find_element(*MAIN_TUTORING_CATEGORY_LABEL)

    @allure.step("Get subject input")
    def get_subject_input(self) -> WebElement:
        return self.driver.find_element(*SUBJECT_INPUT)

    @allure.step("Set subject input")
    def set_subject_input(self, text):
        self.get_subject_input().send_keys(text)

    @allure.step("Get subject label")
    def get_subject_label(self) -> WebElement:
        return self.driver.find_element(*SUBJECT_LABEL)

    @allure.step("Get add subject button")
    def get_add_subject_button(self) -> WebElement:
        return self.driver.find_element(*ADD_SUBJECT_BUTTON)

    @allure.step("Click add subject button")
    def click_add_subject_button(self):
        self.get_add_subject_button().click()
        return self


