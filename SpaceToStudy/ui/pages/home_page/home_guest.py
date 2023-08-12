from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_page import BasePage
from SpaceToStudy.ui.pages.home_page.collapse_item import CollapseItem

COLLAPSE_BLOCK_FLEXIBLE_LOCATION = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[1]/div/div[1]")
COLLAPSE_BLOCK_INDIVIDUAL_TIME = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[1]/div/div[2]")
COLLAPSE_BLOCK_FREE_CHOICE_OF_TUTORS = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[1]/div/div[3]")
COLLAPSE_BLOCK_DIGITAL_COMMUNICATION = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[1]/div/div[4]")
BUTTON_GET_STARTED_FOR_FREE = (By.XPATH, "//a[contains(text(), 'Get started for free')]")

CARD_COMPONENT_LEARN_FROM_EXPERTS = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]")
CARD_COMPONENT_SHARE_YOUR_EXPERIENCE = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]")


class HomePageGuest(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.flexible_location = None
        self.individual_time = None
        self.button_get_started_for_free = None
        self._card_learn_from_experts = None
        self._card_share_your_experience = None

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
        if not self.button_get_started_for_free:
            self.button_get_started_for_free = self.driver.find_element(*COLLAPSE_BLOCK_INDIVIDUAL_TIME)
        return self.button_get_started_for_free

    def get_card_learn_from_experts(self) -> WebElement:
        if not self._card_learn_from_experts:
            self._card_learn_from_experts = self.driver.find_element(*COLLAPSE_BLOCK_INDIVIDUAL_TIME)
        return self._card_learn_from_experts

    def get_card_share_your_experience(self) -> WebElement:
        if not self._card_share_your_experience:
            self._card_learn_from_experts = self.driver.find_element(*CARD_COMPONENT_SHARE_YOUR_EXPERIENCE)
        return self._card_share_your_experience
