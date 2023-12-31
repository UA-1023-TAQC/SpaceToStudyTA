import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent
from SpaceToStudy.ui.pages.explore_offers.explore_offers_page import ExploreOffersPage

BLOCK_NAME = (By.XPATH, "./div[1]/p")
FOUR_STEPS = (By.XPATH, "./div[1]/p/span")

HOW_IT_WORKS_BLOCK_SELECT_A_TUTOR = (By.XPATH, "//div[@id='how-it-works']/div[2]/div[1]")
HOW_IT_WORKS_BLOCK_SEND_REQUEST = (By.XPATH, "//div[@id='how-it-works']/div[2]/div[2]")
HOW_IT_WORKS_BLOCK_START_LEARNING = (By.XPATH, "//div[@id='how-it-works']/div[2]/div[3]")
HOW_IT_WORKS_BLOCK_WRITE_FEEDBACK = (By.XPATH, "//div[@id='how-it-works']/div[2]/div[4]")

ITEM_SELECT_A_TUTOR_IMG = (By.XPATH, "./div[2]/div[1]/img")
ITEM_SELECT_A_TUTOR_TITLE = (By.XPATH, "./div[2]/div[1]/div/p")
ITEM_SELECT_A_TUTOR_DESCRIPTION = (By.XPATH, "./div[2]/div[1]/div/p/span")

ITEM_SEND_REQUEST_IMG = (By.XPATH, "./div[2]/div[2]/img")
ITEM_SEND_REQUEST_TITLE = (By.XPATH, "./div[2]/div[2]/div/p")
ITEM_SEND_REQUEST_DESCRIPTION = (By.XPATH, "./div[2]/div[2]/div/p/span")

ITEM_START_LEARNING_IMG = (By.XPATH, "./div[2]/div[3]/img")
ITEM_START_LEARNING_TITLE = (By.XPATH, "./div[2]/div[3]/div/p")
ITEM_START_LEARNING_DESCRIPTION = (By.XPATH, "./div[2]/div[3]/div/p/span")

ITEM_WRITE_FEEDBACK_IMG = (By.XPATH, "./div[2]/div[4]/img")
ITEM_WRITE_FEEDBACK_TITLE = (By.XPATH, "./div[2]/div[4]/div/p")
ITEM_WRITE_FEEDBACK_DESCRIPTION = (By.XPATH, "./div[2]/div[4]/div/p/span")

FIND_TUTOR_BTN = (By.XPATH, "./a")


class HowItWorksComponentStudent(BaseComponent):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self._block_name_student = None
        self._four_steps = None
        self._img_select_a_tutor_student = None
        self._title_select_a_tutor_student = None
        self._description_select_a_tutor_student = None
        self._img_send_request_student = None
        self._title_send_request_student = None
        self._description_send_request_student = None
        self._img_start_learning_student = None
        self._title_start_learning_student = None
        self._description_start_learning_student = None
        self._img_write_feedback_student = None
        self._title_write_feedback_student = None
        self._description_write_feedback_student = None

    @allure.step("Get the block name")
    def get_block_name_student(self) -> str:
        if not self._block_name_student:
            self._block_name_student = self.node.find_element(*BLOCK_NAME)
        return self._block_name_student.text

    @allure.step("Get the 'Four Steps' text")
    def get_four_steps(self) -> str:
        if not self._four_steps:
            self._four_steps = self.node.find_element(*FOUR_STEPS)
        return self._four_steps.text

    @allure.step("Get the image for 'Select a Tutor'")
    def get_image_select_a_tutor_student(self) -> WebElement:
        if not self._img_select_a_tutor_student:
            self._img_select_a_tutor_student = self.node.find_element(*ITEM_SELECT_A_TUTOR_IMG)
        return self._img_select_a_tutor_student

    @allure.step("Get title webElement of 'Select a Tutor'")
    def get_title_select_a_tutor_student_webelement(self) -> WebElement:
        return self.node.find_element(*ITEM_SELECT_A_TUTOR_TITLE)

    @allure.step("Get text from the title of 'Select a Tutor'")
    def get_title_select_a_tutor_student(self) -> str:
        if not self._title_select_a_tutor_student:
            self._title_select_a_tutor_student = self.node.find_element(*ITEM_SELECT_A_TUTOR_TITLE)
        return self._title_select_a_tutor_student.text

    @allure.step("Get text from the description of 'Select a Tutor'")
    def get_description_select_a_tutor_student(self) -> str:
        if not self._description_select_a_tutor_student:
            self._description_select_a_tutor_student = self.node.find_element(*ITEM_SELECT_A_TUTOR_DESCRIPTION)
        return self._description_select_a_tutor_student.text

    @allure.step("Get an image from 'Send Request'")
    def get_image_send_request_student(self) -> WebElement:
        if not self._img_send_request_student:
            self._img_send_request_student = self.node.find_element(*ITEM_SEND_REQUEST_IMG)
        return self._img_send_request_student

    @allure.step("Get title webElement of 'Send Request'")
    def get_title_send_request_student_webelement(self) -> WebElement:
        return self.node.find_element(*ITEM_SEND_REQUEST_TITLE)

    @allure.step("Get text the title from 'Send Request'")
    def get_title_send_request_student(self) -> str:
        if not self._title_send_request_student:
            self._title_send_request_student = self.node.find_element(*ITEM_SEND_REQUEST_TITLE)
        return self._title_send_request_student.text

    @allure.step("Get text the description from 'Send Request'")
    def get_description_send_request_student(self) -> str:
        if not self._description_send_request_student:
            self._description_send_request_student = self.node.find_element(*ITEM_SEND_REQUEST_DESCRIPTION)
        return self._description_send_request_student.text

    @allure.step("Get the image for 'Start Learning'")
    def get_image_start_learning_student(self) -> WebElement:
        if not self._img_start_learning_student:
            self._img_start_learning_student = self.node.find_element(*ITEM_START_LEARNING_IMG)
        return self._img_start_learning_student

    @allure.step("Get title webElement of 'Start Learning'")
    def get_title_start_learning_student_webelement(self) -> WebElement:
        return self.node.find_element(*ITEM_START_LEARNING_TITLE)

    @allure.step("Get text the title from 'Start Learning'")
    def get_title_start_learning_student(self) -> str:
        if not self._title_start_learning_student:
            self._title_start_learning_student = self.node.find_element(*ITEM_START_LEARNING_TITLE)
        return self._title_start_learning_student.text

    @allure.step("Get text the description from 'Start Learning'")
    def get_description_start_learning_student(self) -> str:
        if not self._description_start_learning_student:
            self._description_start_learning_student = self.node.find_element(*ITEM_START_LEARNING_DESCRIPTION)
        return self._description_start_learning_student.text

    @allure.step("Get the image from 'Write Feedback'")
    def get_image_write_feedback_student(self) -> WebElement:
        if not self._img_write_feedback_student:
            self._img_write_feedback_student = self.node.find_element(*ITEM_WRITE_FEEDBACK_IMG)
        return self._img_write_feedback_student

    @allure.step("Get title webElement of 'Write Feedback'")
    def get_title_write_feedback_student_webelement(self) -> WebElement:
        return self.node.find_element(*ITEM_WRITE_FEEDBACK_TITLE)

    @allure.step("Get text the title from 'Write Feedback'")
    def get_title_write_feedback_student(self) -> str:
        if not self._title_write_feedback_student:
            self._title_write_feedback_student = self.node.find_element(*ITEM_WRITE_FEEDBACK_TITLE)
        return self._title_write_feedback_student.text

    @allure.step("Get text the description from 'Write Feedback'")
    def get_description_write_feedback_student(self) -> str:
        if not self._description_write_feedback_student:
            self._description_write_feedback_student = self.node.find_element(*ITEM_WRITE_FEEDBACK_DESCRIPTION)
        return self._description_write_feedback_student.text

    @allure.step("Get 'Find tutor' button")
    def get_find_tutor_btn(self):
        return self.node.find_element(*FIND_TUTOR_BTN)

    @allure.step("Click 'Find tutor' button")
    def click_find_tutor_btn(self):
        self.get_find_tutor_btn().click()
        return ExploreOffersPage(self.node.parent)

    @allure.step("Get select a tutor items")
    def get_select_a_tutor_items(self) -> WebElement:
        return self.node.find_element(*HOW_IT_WORKS_BLOCK_SELECT_A_TUTOR)

    @allure.step("Get send request items")
    def get_send_request_items(self) -> WebElement:
        return self.node.find_element(*HOW_IT_WORKS_BLOCK_SEND_REQUEST)

    @allure.step("Get start learning items")
    def get_start_learning_items(self) -> WebElement:
        return self.node.find_element(*HOW_IT_WORKS_BLOCK_START_LEARNING)

    @allure.step("Get write feedback items")
    def get_write_feedback_items(self) -> WebElement:
        return self.node.find_element(*HOW_IT_WORKS_BLOCK_WRITE_FEEDBACK)
