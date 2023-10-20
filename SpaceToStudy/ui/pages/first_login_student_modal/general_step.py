import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.elements.input import Input
from SpaceToStudy.ui.elements.input_with_drop_down_list import InputDropDownList
from SpaceToStudy.ui.elements.textarea import Textarea
from SpaceToStudy.ui.pages.first_login_student_modal.first_login_modal import FirstLoginModal
from SpaceToStudy.ui.pages.first_login_student_modal.interests_step import InterestsStepStudent

STARTING_TEXT = (By.XPATH, "//form/div[1]")
IMAGE = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/div/img")
FIRST_NAME_INPUT = (By.XPATH, "//html/body/div[2]/div[3]/div/div/div/div/div[2]/div//form/div[1]/div[1]/div[1]")
FIRST_NAME_LABEL = (By.XPATH, "//html/body/div[2]/div[3]/div/div/div/div/div[2]/div//form/div[1]/div[1]/div[1]/label")
LAST_NAME_INPUT = (By.XPATH, "//html/body/div[2]/div[3]/div/div/div/div/div[2]/div//form/div[1]/div[1]/div[2]")
LAST_NAME_LABEL = (By.XPATH, "//html/body/div[2]/div[3]/div/div/div/div/div[2]/div//form/div[1]/div[1]/div[2]/label")
COUNTRY_INPUT = (By.XPATH, "//html/body/div[2]/div[3]/div/div/div/div/div[2]/div//form/div[1]/div[1]/div[3]/div")
COUNTRY_LABEL = (By.XPATH, "//html/body/div[2]/div[3]/div/div/div/div/div[2]/div//form/div[1]/div[1]/div[3]/div/label")
CITY_INPUT = (By.XPATH, "//html/body/div[2]/div[3]/div/div/div/div/div[2]/div//form/div[1]/div[1]/div[4]/div")
CITY_LABEL = (By.XPATH, "//html/body/div[2]/div[3]/div/div/div/div/div[2]/div//form/div[1]/div[1]/div[4]/div/label")
DESCRIPTION_TEXTAREA = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/form/div[1]/div[2]/div/div/textarea[1]")
DESCRIPTION_LABEL = (By.XPATH, "//html/body/div[2]/div[3]/div/div/div/div/div[2]/div//form/div[1]/div[2]/div/label")
SYMBOLS_COUNTER = (By.XPATH, "//html/body/div[2]/div[3]/div/div/div/div/div[2]/div//form/div[1]/div[2]/p")


class GeneralStepStudent(FirstLoginModal):

    def __init__(self, node):
        super().__init__(node)
        self._first_name_input = None
        self._last_name_input = None
        self._country_input = None
        self._city_input = None
        self._description_textarea = None

    @allure.step("Get starting text")
    def get_starting_text(self) -> str:
        return self.node.find_element(*STARTING_TEXT).text

    @allure.step("Get image")
    def get_image(self) -> WebElement:
        return self.node.find_element(*IMAGE)

    @allure.step("Get first name input")
    def get_first_name_input(self) -> Input:
        if not self._first_name_input:
            node = self.node.find_element(*FIRST_NAME_INPUT)
            self._first_name_input = Input(node)
        return self._first_name_input

    @allure.step("Get first name label")
    def get_first_name_label(self) -> WebElement:
        return self.node.find_element(*FIRST_NAME_LABEL)

    @allure.step("Get last name input")
    def get_last_name_input(self) -> Input:
        if not self._last_name_input:
            node = self.node.find_element(*LAST_NAME_INPUT)
            self._last_name_input = Input(node)
        return self._last_name_input

    @allure.step("Get last name label")
    def get_last_name_label(self) -> WebElement:
        return self.node.find_element(*LAST_NAME_LABEL)

    @allure.step("Get country input")
    def get_country_input(self) -> InputDropDownList:
        if not self._country_input:
            node = self.node.find_element(*COUNTRY_INPUT)
            self._country_input = InputDropDownList(node)
        return self._country_input

    @allure.step("Get city input")
    def get_city_input(self) -> InputDropDownList:
        if not self._city_input:
            node = self.node.find_element(*CITY_INPUT)
            self._city_input = InputDropDownList(node)
        return self._city_input

    @allure.step("Get description input")
    def get_description_textarea(self) -> Textarea:
        if not self._description_textarea:
            node = self.node.find_element(*DESCRIPTION_TEXTAREA)
            self._description_textarea = Textarea(node)
        return self._description_textarea

    @allure.step("Get symbols counter")
    def get_symbols_counter(self) -> WebElement:
        return self.node.find_element(*SYMBOLS_COUNTER)

    @allure.step("Get symbols counter text")
    def get_symbols_counter_text(self) -> str:
        return self.get_symbols_counter().text

    @allure.step("Click next button")
    def click_next_button(self):
        self.get_next_button().click()
        return InterestsStepStudent(self.node)
