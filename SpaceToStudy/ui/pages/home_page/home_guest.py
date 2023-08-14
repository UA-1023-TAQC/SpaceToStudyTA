from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_page import BasePage
from SpaceToStudy.ui.pages.home_page.collapse_item import CollapseItem
from SpaceToStudy.ui.pages.home_page.how_it_works_component import HowItWorksComponent

COLLAPSE_BLOCK_FLEXIBLE_LOCATION = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[1]/div/div[1]")
COLLAPSE_BLOCK_INDIVIDUAL_TIME = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[1]/div/div[2]")
COLLAPSE_BLOCK_FREE_CHOICE_OF_TUTORS = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[1]/div/div[3]")
COLLAPSE_BLOCK_DIGITAL_COMMUNICATION = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[1]/div/div[4]")
BUTTON_GET_STARTED_FOR_FREE = (By.XPATH, "//a[contains(text(), 'Get started for free')]")

HOW_IT_WORKS_BLOCK = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[3]/div")

HOW_IT_WORKS_BLOCK_SIGN_UP = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[3]/div/div[2]")
HOW_IT_WORKS_BLOCK_SELECT_A_TUTOR = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[3]/div/div[3]")
HOW_IT_WORKS_BLOCK_SEND_REQUEST = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[3]/div/div[4]")
HOW_IT_WORKS_BLOCK_START_LEARNING = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[3]/div/div[5]")

CHECKBOX_HOW_IT_WORKS_BLOCK = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[3]/div/div[1]/span/span[1]/input")


class HomePageGuest(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.flexible_location = None
        self.individual_time = None
        self.button_get_started_for_free = None
        self._how_it_works_block = None
        self._sign_up = None
        self._select_a_tutor = None
        self._send_request = None
        self._start_learning = None
        self._checkbox_how_it_works_block = None

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

    def get_how_it_works_block(self) -> WebElement:
        if not self._how_it_works_block:
            node = self.driver.find_element(*HOW_IT_WORKS_BLOCK)
            self._how_it_works_block = HowItWorksComponent(node)
        return self._how_it_works_block

    def get_sign_up_items(self) -> WebElement:
        if not self._sign_up:
            node = self.driver.find_element(*HOW_IT_WORKS_BLOCK_SIGN_UP)
            self._sign_up = HowItWorksComponent(node)
        return self._sign_up

    def get_select_a_tutor_items(self) -> WebElement:
        if not self._select_a_tutor:
            node = self.driver.find_element(*HOW_IT_WORKS_BLOCK_SELECT_A_TUTOR)
            self._select_a_tutor = HowItWorksComponent(node)
        return self._select_a_tutor

    def get_send_request_items(self) -> WebElement:
        if not self._send_request:
            node = self.driver.find_element(*HOW_IT_WORKS_BLOCK_SEND_REQUEST)
            self._send_request = HowItWorksComponent(node)
        return self._send_request

    def get_start_learning_items(self) -> WebElement:
        if not self._start_learning:
            node = self.driver.find_element(*HOW_IT_WORKS_BLOCK_START_LEARNING)
            self._start_learning = HowItWorksComponent(node)
        return self._start_learning

    def get_checkbox_how_it_works_block(self) -> WebElement:
        if not self._checkbox_how_it_works_block:
            return self.driver.find_element(*CHECKBOX_HOW_IT_WORKS_BLOCK)

    def click_checkbox_how_it_works_block(self):
        self.get_checkbox_how_it_works_block().click()

