from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_page import BasePage
from SpaceToStudy.ui.pages.home_page.collapse_item import CollapseItem

COLLAPSE_BLOCK_FLEXIBLE_LOCATION = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[1]/div/div[1]")
COLLAPSE_BLOCK_INDIVIDUAL_TIME = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[1]/div/div[2]")
COLLAPSE_BLOCK_FREE_CHOICE_OF_TUTORS = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[1]/div/div[3]")
COLLAPSE_BLOCK_DIGITAL_COMMUNICATION = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[1]/div/div[4]")
BUTTON_GET_STARTED_FOR_FREE = (By.XPATH, "//a[contains(text(), 'Get started for free')]")
BUTTON_BECOME_A_STUDENT = (By.XPATH, "//button[contains(text(), 'Become a student')]")


class HomePageGuest(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.flexible_location = None
        self.individual_time = None
        self._button_get_started_for_free = None
        self._button_become_a_student = None

    def get_flexible_location(self) -> CollapseItem:
        if not self.flexible_location:
            flexible_location = self.driver.find_element(*COLLAPSE_BLOCK_FLEXIBLE_LOCATION)
            self.flexible_location = CollapseItem(flexible_location)
        return self.flexible_location

    def click_flexible_location(self):
        self.get_flexible_location().click()
        return self

    def get_individual_time(self) -> CollapseItem:
        if not self.individual_time:
            individual_time = self.driver.find_element(*COLLAPSE_BLOCK_INDIVIDUAL_TIME)
            self.individual_time = CollapseItem(individual_time)
        return self.individual_time

    def click_individual_time(self):
        self.get_individual_time().click()
        return self

    def get_button_get_started_for_free(self) -> WebElement:
        if not self._button_get_started_for_free:
            self._button_get_started_for_free = self.driver.find_element(*BUTTON_GET_STARTED_FOR_FREE)
        return self._button_get_started_for_free

    def get_text_button_get_started_for_free(self) -> str:
        return self.get_button_get_started_for_free().text

    def click_button_get_started_for_free(self):
        self.get_button_get_started_for_free().click()
        return self

    def get_button_become_a_student(self) -> WebElement:
        if not self._button_become_a_student:
            self._button_become_a_student = self.driver.find_element(*BUTTON_BECOME_A_STUDENT)
        return self._button_become_a_student

    def get_text_button_become_a_student(self) -> str:
        return self.get_button_become_a_student().text

    def click_button_become_a_student(self):
        self.get_button_become_a_student().click()
        return self

