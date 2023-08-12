from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_page import BasePage
from SpaceToStudy.ui.pages.home_page.collapse_item import CollapseItem

COLLAPSE_BLOCK_FLEXIBLE_LOCATION = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[1]/div/div[1]")
COLLAPSE_BLOCK_INDIVIDUAL_TIME = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[1]/div/div[2]")
COLLAPSE_BLOCK_FREE_CHOICE_OF_TUTOR = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[1]/div/div[3]")
COLLAPSE_BLOCK_DIGITAL_COMMUNICATION = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[1]/div/div[4]")

BUTTON_GET_STARTED_FOR_FREE = (By.XPATH, "//a[contains(text(), 'Get started for free')]")


class HomePageGuest(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._flexible_location = None
        self._individual_time = None
        self._digital_communication = None
        self._free_choice_of_tutors = None
        self._button_get_started_for_free = None

    def get_flexible_location(self) -> CollapseItem:
        if not self._flexible_location:
            _flexible_location = self.driver.find_element(*COLLAPSE_BLOCK_FLEXIBLE_LOCATION)
            self._flexible_location = CollapseItem(_flexible_location)
        return self._flexible_location

    def click_flexible_location(self):
        self.get_flexible_location().click()
        return self

    def get_individual_time(self) -> CollapseItem:
        if not self._individual_time:
            _individual_time = self.driver.find_element(*COLLAPSE_BLOCK_INDIVIDUAL_TIME)
            self._individual_time = CollapseItem(_individual_time)
        return self._individual_time

    def click_individual_time(self):
        self.get_individual_time().click()
        return self

    def get_free_choice_of_tutors(self) -> CollapseItem:
        if not self._free_choice_of_tutors:
            _free_choice_of_tutors = self.driver.find_element(*COLLAPSE_BLOCK_FREE_CHOICE_OF_TUTOR)
            self._free_choice_of_tutors = CollapseItem(_free_choice_of_tutors)
        return self._free_choice_of_tutors

    def click_free_choice_of_tutors(self):
        self.get_free_choice_of_tutors().click()
        return self

    def get_digital_communication(self) -> CollapseItem:
        if not self._digital_communication:
            _digital_communication = self.driver.find_element(*COLLAPSE_BLOCK_DIGITAL_COMMUNICATION)
            self._digital_communication = CollapseItem(_digital_communication)
        return self._digital_communication

    def click_digital_communication(self):
        self.get_digital_communication().click()
        return self

    def get_button_get_started_for_free(self) -> WebElement:
        if not self._button_get_started_for_free:
            self._button_get_started_for_free = self.driver.find_element(*BUTTON_GET_STARTED_FOR_FREE)
        return self._button_get_started_for_free
