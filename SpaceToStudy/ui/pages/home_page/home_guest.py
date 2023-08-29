from time import sleep

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_page import BasePage
from SpaceToStudy.ui.pages.home_page.card_component_for_guest import CardComponent
from SpaceToStudy.ui.pages.home_page.collapse_item import CollapseItem
from SpaceToStudy.ui.pages.home_page.how_it_works_component_guest import HowItWorksComponent
from SpaceToStudy.ui.pages.sign_up_modal.sign_up_modal import RegistrationModal

COLLAPSE_BLOCK_FLEXIBLE_LOCATION = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[1]/div/div[1]")
COLLAPSE_BLOCK_INDIVIDUAL_TIME = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[1]/div/div[2]")
COLLAPSE_BLOCK_FREE_CHOICE_OF_TUTORS = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[1]/div/div[3]")
COLLAPSE_BLOCK_DIGITAL_COMMUNICATION = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[1]/div/div[4]")

BUTTON_GET_STARTED_FOR_FREE = (By.XPATH, "//a[contains(text(), 'Get started for free')]")
BUTTON_BECOME_A_STUDENT = (By.XPATH, "//button[contains(text(), 'Become a student')]")

HOW_IT_WORKS_BLOCK = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[3]/div")

HOW_IT_WORKS_BLOCK_SIGN_UP = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[3]/div/div[2]")
HOW_IT_WORKS_BLOCK_SELECT_A_TUTOR = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[3]/div/div[3]")
HOW_IT_WORKS_BLOCK_SEND_REQUEST = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[3]/div/div[4]")
HOW_IT_WORKS_BLOCK_START_LEARNING = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[3]/div/div[5]")

CHECKBOX_HOW_IT_WORKS_BLOCK = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[3]/div/div[1]/span/span[1]/input")

CARD_COMPONENT_LEARN_FROM_EXPERTS = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]")
CARD_COMPONENT_SHARE_YOUR_EXPERIENCE = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]")

IMG_MAP = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[1]/img")
MAIN_BANNER = (By.XPATH, "/html/body/div/div/div[2]/div/div[1]/img")


class HomePageGuest(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._card_learn_from_experts = None
        self._card_share_your_experience = None
        self._how_it_works_block = None
        self._sign_up = None
        self._select_a_tutor = None
        self._send_request = None
        self._start_learning = None
        self._checkbox_how_it_works_block = None
        self._flexible_location = None
        self._individual_time = None
        self._digital_communication = None
        self._free_choice_of_tutors = None
        self._button_get_started_for_free = None
        self._button_become_a_student = None
        self._img_map = None
        self._main_banner = None

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
            _free_choice_of_tutors = self.driver.find_element(*COLLAPSE_BLOCK_FREE_CHOICE_OF_TUTORS)
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

    def get_sign_up_items(self) -> HowItWorksComponent:
        if not self._sign_up:
            _sign_up = self.driver.find_element(*HOW_IT_WORKS_BLOCK_SIGN_UP)
            self._sign_up = HowItWorksComponent(_sign_up)
        return self._sign_up

    def get_select_a_tutor_items(self) -> HowItWorksComponent:
        if not self._select_a_tutor:
            _select_a_tutor = self.driver.find_element(*HOW_IT_WORKS_BLOCK_SELECT_A_TUTOR)
            self._select_a_tutor = HowItWorksComponent(_select_a_tutor)
        return self._select_a_tutor

    def get_send_request_items(self) -> HowItWorksComponent:
        if not self._send_request:
            _send_request = self.driver.find_element(*HOW_IT_WORKS_BLOCK_SEND_REQUEST)
            self._send_request = HowItWorksComponent(_send_request)
        return self._send_request

    def get_start_learning_items(self) -> WebElement:
        if not self._start_learning:
            node = self.driver.find_element(*HOW_IT_WORKS_BLOCK_START_LEARNING)
            self._start_learning = HowItWorksComponent(node)
        return self._start_learning

    def get_how_it_works_block(self) -> HowItWorksComponent:
        if not self._how_it_works_block:
            _how_it_works_block = self.driver.find_element(*HOW_IT_WORKS_BLOCK)
            self._how_it_works_block = HowItWorksComponent(_how_it_works_block)
        return self._how_it_works_block

    def get_checkbox_how_it_works_block(self) -> HowItWorksComponent:
        if not self._checkbox_how_it_works_block:
            return self.driver.find_element(*CHECKBOX_HOW_IT_WORKS_BLOCK)

    def click_checkbox_how_it_works_block(self):
        self.get_checkbox_how_it_works_block().click()

    def get_card_learn_from_experts(self) -> CardComponent:
        if not self._card_learn_from_experts:
            self._card_learn_from_experts = CardComponent(self.driver.find_element(*CARD_COMPONENT_LEARN_FROM_EXPERTS))
        return self._card_learn_from_experts

    def get_card_share_your_experience(self) -> CardComponent:
        if not self._card_share_your_experience:
            self._card_share_your_experience = CardComponent(self.driver.find_element(*CARD_COMPONENT_SHARE_YOUR_EXPERIENCE))
        return self._card_share_your_experience

    def click_become_a_tutor(self) -> RegistrationModal:
        self.get_card_share_your_experience().click_btn()
        return RegistrationModal(self.driver.find_element(By.XPATH,"//div[@data-testid='popupContent']"))

    def click_become_a_tutor(self) -> RegistrationModal:
        self.get_card_share_your_experience().click_btn()
        return RegistrationModal(self.driver.find_element(By.XPATH,"//div[@data-testid='popupContent']"))
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

    def get_button_get_started_for_free(self) -> WebElement:
        if not self._button_get_started_for_free:
            self._button_get_started_for_free = self.driver.find_element(*BUTTON_GET_STARTED_FOR_FREE)
        return self._button_get_started_for_free

    def click_started_for_free(self):
        self.get_button_get_started_for_free().click()
        sleep(1)
        return self

    def get_img_map(self) -> WebElement:
        if not self._img_map:
            self._img_map = self.driver.find_element(*IMG_MAP)
        return self._img_map

    def get_main_banner(self) -> WebElement:
        if not self._main_banner:
            self._main_banner = self.driver.find_element(*MAIN_BANNER)
        return self._main_banner
