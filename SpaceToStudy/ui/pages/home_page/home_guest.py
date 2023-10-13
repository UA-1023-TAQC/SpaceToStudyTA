from time import sleep

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_page import BasePage
from SpaceToStudy.ui.pages.home_page.card_component_for_guest import CardComponent
from SpaceToStudy.ui.pages.home_page.collapse_item import CollapseItem
from SpaceToStudy.ui.pages.home_page.how_it_works_component_guest import HowItWorksComponent
from SpaceToStudy.ui.pages.home_page.who_we_are_block import WhoWeAreBlock
from SpaceToStudy.ui.pages.sign_up_modal.sign_up_modal import RegistrationModal

IMG_MAP = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[1]/img")
MAIN_BANNER = (By.XPATH, "/html/body/div/div/div[2]/div/div[1]/img")
SIGN_UP_MODAL = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div")

COLLAPSE_BLOCK = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[1]/div")
COLLAPSE_BLOCK_ITEMS = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[1]/div/div")
COLLAPSE_BLOCK_ITEMS_MOBILE = (By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div[1]/div/div")

COLLAPSE_BLOCK_FLEXIBLE_LOCATION = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[1]/div/div[1]")
COLLAPSE_BLOCK_INDIVIDUAL_TIME = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[1]/div/div[2]")
COLLAPSE_BLOCK_FREE_CHOICE_OF_TUTORS = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[1]/div/div[3]")
COLLAPSE_BLOCK_DIGITAL_COMMUNICATION = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[1]/div/div[4]")

BUTTON_GET_STARTED_FOR_FREE = (By.XPATH, "//a[contains(text(), 'Get started for free')]")

WHAT_CAN_U_DO_BLOCK = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[2]")
WHAT_CAN_U_DO_BLOCK_TITLE = (By.XPATH, "//*[@id='what-сan-you-do']/div[1]/p")
WHAT_CAN_U_DO_BLOCK_DESCRIPTION = (By.XPATH, "//*[@id='what-сan-you-do']/div[1]/span")
CARD_COMPONENT_LEARN_FROM_EXPERTS = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]")
CARD_COMPONENT_SHARE_YOUR_EXPERIENCE = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]")
BECOME_A_STUDENT_BUTTON = (By.XPATH, "//*[@id='what-сan-you-do']/div[2]/div[1]/button")
BECOME_A_TUTOR_BUTTON = (By.XPATH, "//*[@id='what-сan-you-do']/div[2]/div[2]/button")

HOW_IT_WORKS_BLOCK = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[3]/div")
HOW_IT_WORKS_BLOCK_SHARE_YOUR_EXPERIENCE = (By.XPATH,
                                            "//div[@id='how-it-works']//h6[contains(text(), 'Share your Experience')]")
HOW_IT_WORKS_BLOCK_SIGN_UP = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[3]/div/div[2]")
HOW_IT_WORKS_BLOCK_SELECT_A_TUTOR = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[3]/div/div[3]")
HOW_IT_WORKS_BLOCK_SEND_REQUEST = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[3]/div/div[4]")
HOW_IT_WORKS_BLOCK_START_LEARNING = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[3]/div/div[5]")
BECOME_A_TUTOR_OR_STUDENT_BUTTON = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[3]/div/button")
BECOME_A_TUTOR_OR_STUDENT_BUTTON_SELECTED = (By.TAG_NAME, "span")
CHECKBOX_HOW_IT_WORKS_BLOCK = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[3]/div/div[1]/span/span[1]/input")

WHO_WE_ARE_BLOCK = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[4]")


class HomePageGuest(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._what_can_u_do_title = None
        self._what_can_u_do_descripton = None
        self._card_learn_from_experts = None
        self._card_share_your_experience = None
        self._become_a_student_btn = None
        self._become_a_tutor_btn = None
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
        self._img_map = None
        self._main_banner = None
        self._collapse_items = None
        self._collapse_block = None
        self._collapse_items_mobile = None
        self._who_we_are_block = None
        

    @allure.step("Get map image")
    def get_img_map(self) -> WebElement:
        if not self._img_map:
            self._img_map = self.driver.find_element(*IMG_MAP)
        return self._img_map

    @allure.step("Get main banner")
    def get_main_banner(self) -> WebElement:
        if not self._main_banner:
            self._main_banner = self.driver.find_element(*MAIN_BANNER)
        return self._main_banner

    @allure.step("Get collapse block")
    def get_collapse_block(self) -> WebElement:
        if not self._collapse_block:
            self._collapse_block = self.driver.find_element(*COLLAPSE_BLOCK)
        return self._collapse_block

    @allure.step("Get list items in collapse block")
    def get_collapse_list_items_block(self) -> list[CollapseItem]:
        if self._collapse_items is None:
            _collapse_items = self.driver.find_elements(*COLLAPSE_BLOCK_ITEMS)
            self._collapse_items = []
            for collapse_item in _collapse_items:
                self._collapse_items.append(CollapseItem(collapse_item))
        return self._collapse_items

    @allure.step("Get list items in collapse block mobile_size_screen")
    def get_collapse_list_items_block_mobile_size_screen(self) -> list[CollapseItem]:
        if self._collapse_items_mobile is None:
            _collapse_items_mobile = self.driver.find_elements(*COLLAPSE_BLOCK_ITEMS_MOBILE)
            self._collapse_items_mobile = []
            for collapse_item in _collapse_items_mobile:
                self._collapse_items_mobile.append(CollapseItem(collapse_item))
        return self._collapse_items_mobile

    @allure.step("Get flexible location")
    def get_flexible_location(self) -> CollapseItem:
        if not self._flexible_location:
            _flexible_location = self.driver.find_element(*COLLAPSE_BLOCK_FLEXIBLE_LOCATION)
            self._flexible_location = CollapseItem(_flexible_location)
        return self._flexible_location

    @allure.step("Click flexible location")
    def click_flexible_location(self):
        self.get_flexible_location().click()
        return self

    @allure.step("Get individual time")
    def get_individual_time(self) -> CollapseItem:
        if not self._individual_time:
            _individual_time = self.driver.find_element(*COLLAPSE_BLOCK_INDIVIDUAL_TIME)
            self._individual_time = CollapseItem(_individual_time)
        return self._individual_time

    @allure.step("Click individual time")
    def click_individual_time(self):
        self.get_individual_time().click()
        return self

    @allure.step("Get free choice of tutors")
    def get_free_choice_of_tutors(self) -> CollapseItem:
        if not self._free_choice_of_tutors:
            _free_choice_of_tutors = self.driver.find_element(*COLLAPSE_BLOCK_FREE_CHOICE_OF_TUTORS)
            self._free_choice_of_tutors = CollapseItem(_free_choice_of_tutors)
        return self._free_choice_of_tutors

    @allure.step("Click free choice of tutors")
    def click_free_choice_of_tutors(self):
        self.get_free_choice_of_tutors().click()
        return self

    @allure.step("Get digital communication")
    def get_digital_communication(self) -> CollapseItem:
        if not self._digital_communication:
            _digital_communication = self.driver.find_element(*COLLAPSE_BLOCK_DIGITAL_COMMUNICATION)
            self._digital_communication = CollapseItem(_digital_communication)
        return self._digital_communication

    @allure.step("Click digital communication")
    def click_digital_communication(self):
        self.get_digital_communication().click()
        return self

    @allure.step("Get button \"get started for free\"")
    def get_button_get_started_for_free(self) -> WebElement:
        if not self._button_get_started_for_free:
            self._button_get_started_for_free = self.driver.find_element(*BUTTON_GET_STARTED_FOR_FREE)
        return self._button_get_started_for_free

    @allure.step("Get text in button \"get started for free\"")
    def get_text_button_get_started_for_free(self) -> str:
        return self.get_button_get_started_for_free().text

    @allure.step("Click button \"get started for free\"")
    def click_button_get_started_for_free(self):
        self.get_button_get_started_for_free().click()
        return self.driver.find_element(*WHAT_CAN_U_DO_BLOCK)

    @allure.step('Click button "Get started for free"')
    def click_started_for_free(self):
        self.get_button_get_started_for_free().click()
        sleep(1)
        return self

    @allure.step("Get the 'What can you do' block")
    def get_what_can_u_do_block(self):
        return self.driver.find_element(*WHAT_CAN_U_DO_BLOCK)

    @allure.step("Get a 'What can you do' block title")
    def get_what_can_u_do_title(self) -> WebElement:
        if not self._what_can_u_do_title:
            self._what_can_u_do_title = self.driver.find_element(*WHAT_CAN_U_DO_BLOCK_TITLE)
        return self._what_can_u_do_title

    @allure.step("Get a 'What can you do' block description")
    def get_what_can_u_do_description(self) -> WebElement:
        if not self._what_can_u_do_descripton:
            self._what_can_u_do_descripton = self.driver.find_element(*WHAT_CAN_U_DO_BLOCK_DESCRIPTION)
        return self._what_can_u_do_descripton

    @allure.step("Get card learn from experts")
    def get_card_learn_from_experts(self) -> CardComponent:
        if not self._card_learn_from_experts:
            self._card_learn_from_experts = CardComponent(self.driver.find_element(*CARD_COMPONENT_LEARN_FROM_EXPERTS))
        return self._card_learn_from_experts

    @allure.step("Get become a student button")
    def get_become_a_student_btn(self) -> WebElement:
        if not self._become_a_student_btn:
            self._become_a_student_btn = self.driver.find_element(*BECOME_A_STUDENT_BUTTON)
        return self._become_a_student_btn

    @allure.step("Click become a student ")
    def click_become_a_student(self) -> RegistrationModal:
        self.get_card_learn_from_experts().click_btn()
        return RegistrationModal(self.driver.find_element(By.XPATH, "//div[@data-testid='popupContent']"))

    @allure.step("Get card share your experience")
    def get_card_share_your_experience(self) -> CardComponent:
        if not self._card_share_your_experience:
            self._card_share_your_experience = CardComponent(self.driver.find_element(*CARD_COMPONENT_SHARE_YOUR_EXPERIENCE))
        return self._card_share_your_experience

    @allure.step("Get become a tutor button")
    def get_become_a_tutor_btn(self) -> WebElement:
        if not self._become_a_tutor_btn:
            self._become_a_tutor_btn = self.driver.find_element(*BECOME_A_TUTOR_BUTTON)
        return self._become_a_tutor_btn

    @allure.step("Click become a tutor")
    def click_become_a_tutor(self) -> RegistrationModal:
        self.get_card_share_your_experience().click_btn()
        return RegistrationModal(self.driver.find_element(By.XPATH,"//div[@data-testid='popupContent']"))

    @allure.step("Get the list of web elements for 'What can you do' block")
    def get_what_can_u_do_elements(self) -> dict:
        return {"title": self.get_what_can_u_do_title(),
                "description": self.get_what_can_u_do_description(),
                "the_learn_card_img": self.get_card_learn_from_experts().get_image(),
                "the_learn_card_title": self.get_card_learn_from_experts().get_name_element(),
                "the_learn_card_description": self.get_card_learn_from_experts().get_offers_element(),
                "become_student_btn": self.get_card_learn_from_experts().get_btn(),
                "the_teach_card_img": self.get_card_share_your_experience().get_image(),
                "the_teach_card_title": self.get_card_share_your_experience().get_name_element(),
                "the_teach_card_description": self.get_card_share_your_experience().get_offers_element(),
                "become_a_tutor_btn": self.get_card_share_your_experience().get_btn()}

    @allure.step("Get how it works block")
    def get_how_it_works_block(self) -> HowItWorksComponent:
        if not self._how_it_works_block:
            _how_it_works_block = self.driver.find_element(*HOW_IT_WORKS_BLOCK)
            self._how_it_works_block = HowItWorksComponent(_how_it_works_block)
        return self._how_it_works_block

    @allure.step("Get checkbox how it works block")
    def get_checkbox_how_it_works_block(self) -> WebElement:
        if not self._checkbox_how_it_works_block:
            return self.driver.find_element(*CHECKBOX_HOW_IT_WORKS_BLOCK)

    @allure.step("Click checkbox how it works block")
    def click_checkbox_how_it_works_block(self):
        self.get_checkbox_how_it_works_block().click()
        return self

    @allure.step("Get sign up items")
    def get_sign_up_items(self) -> HowItWorksComponent:
        _sign_up = self.driver.find_element(*HOW_IT_WORKS_BLOCK_SIGN_UP)
        return HowItWorksComponent(_sign_up)


    @allure.step("Get select a tutor items")
    def get_select_a_tutor_items(self) -> HowItWorksComponent:
        _select_a_tutor = self.driver.find_element(*HOW_IT_WORKS_BLOCK_SELECT_A_TUTOR)
        return HowItWorksComponent(_select_a_tutor)


    @allure.step("Get send request items")
    def get_send_request_items(self) -> HowItWorksComponent:
        _send_request = self.driver.find_element(*HOW_IT_WORKS_BLOCK_SEND_REQUEST)
        return HowItWorksComponent(_send_request)


    @allure.step("Get start learning items")
    def get_start_learning_items(self) -> HowItWorksComponent:
        node = self.driver.find_element(*HOW_IT_WORKS_BLOCK_START_LEARNING)
        return HowItWorksComponent(node)


    @allure.step("Get how it works block")
    def get_how_it_works_block(self) -> HowItWorksComponent:
        if not self._how_it_works_block:
            _how_it_works_block = self.driver.find_element(*HOW_IT_WORKS_BLOCK)
            self._how_it_works_block = HowItWorksComponent(_how_it_works_block)
        return self._how_it_works_block

    @allure.step("Get checkbox how it works block")
    def get_checkbox_how_it_works_block(self) -> HowItWorksComponent:
        if not self._checkbox_how_it_works_block:
            return self.driver.find_element(*CHECKBOX_HOW_IT_WORKS_BLOCK)

    @allure.step("Get checkbox switch WebElement in 'How it works' block")
    def get_checkbox_switch_how_it_works_block(self) -> WebElement:
        if not self._checkbox_how_it_works_block:
            return self.driver.find_element(*CHECKBOX_HOW_IT_WORKS_BLOCK)

    @allure.step("Click checkbox how it works block")
    def click_checkbox_switch_how_it_works_block(self):
        self.get_checkbox_switch_how_it_works_block().click()
        return self

    @allure.step("Get 'Share your experience' WebElement in 'How it works' block")
    def get_share_your_experience_how_it_works_block(self) -> WebElement:
        return self.driver.find_element(*HOW_IT_WORKS_BLOCK_SHARE_YOUR_EXPERIENCE)

    @allure.step("Get card learn from experts")
    def get_card_learn_from_experts(self) -> CardComponent:
        if not self._card_learn_from_experts:
            self._card_learn_from_experts = CardComponent(self.driver.find_element(*CARD_COMPONENT_LEARN_FROM_EXPERTS))
        return self._card_learn_from_experts

    @allure.step("Click become a student ")
    def click_become_a_student(self) -> RegistrationModal:
        self.get_card_learn_from_experts().click_btn()
        return RegistrationModal(self.driver.find_element(By.XPATH, "//div[@data-testid='popupContent']"))

    @allure.step("Get card share your experience")
    def get_card_share_your_experience(self) -> CardComponent:
        if not self._card_share_your_experience:
            self._card_share_your_experience = CardComponent(
                self.driver.find_element(*CARD_COMPONENT_SHARE_YOUR_EXPERIENCE))
        return self._card_share_your_experience

    @allure.step("Click become a tutor")
    def click_become_a_tutor(self) -> RegistrationModal:
        self.get_card_share_your_experience().click_btn()
        return RegistrationModal(self.driver.find_element(By.XPATH, "//div[@data-testid='popupContent']"))

    @allure.step("Get text in button \"get started for free\"")
    def get_text_button_get_started_for_free(self) -> str:
        return self.get_button_get_started_for_free().text

    @allure.step("Click button get started for free")
    def click_button_get_started_for_free(self):
        self.get_button_get_started_for_free().click()
        return self.driver.find_element(*WHAT_CAN_U_DO_BLOCK)

    @allure.step("Get button become a student or tutor")
    def get_button_become_a_student_tutor(self) -> WebElement:
        return self.driver.find_element(*BECOME_A_TUTOR_OR_STUDENT_BUTTON)

    @allure.step("Get button become a student or tutor text")
    def get_button_become_a_student_tutor_text(self) -> str:
        return self.get_button_become_a_student_tutor().text

    @allure.step("Check button become a student or tutor is selected")
    def is_button_become_a_student_tutor_selected(self) -> bool:
        # when u press tab until button is selected
        count_of_span_elements = self.get_button_become_a_student_tutor().find_elements(*BECOME_A_TUTOR_OR_STUDENT_BUTTON_SELECTED)
        if len(count_of_span_elements) == 1:
            return False
        elif len(count_of_span_elements) == 3:
            return True
        else:
            raise AssertionError(f"The logic for the '{self.get_button_become_a_student_tutor_text}' has been changed. Please review and update the code accordingly to handle this change.")

    @allure.step("Get text in button \"become a student or tutor\"")
    def get_text_button_become_a_student_tutor(self) -> str:
        return self.get_button_become_a_student_tutor().text

    @allure.step("Click on button \"become a student or tutor\"")
    def click_button_become_a_student_tutor(self):
        self.get_button_become_a_student_tutor().click()
        node = self.driver.find_element(*SIGN_UP_MODAL)
        sleep(1)
        return RegistrationModal(node)

    @allure.step("Get who we are block")
    def get_who_we_are_block(self) -> WhoWeAreBlock:
        if not self._who_we_are_block:
            node = self.driver.find_element(*WHO_WE_ARE_BLOCK)
            self._who_we_are_block = WhoWeAreBlock(node)
        return self._who_we_are_block


