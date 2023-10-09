import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_page import BasePage
from SpaceToStudy.ui.pages.explore_offers.explore_offers_page import ExploreOffersPage

TITLE = (By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div/div[1]/p")
SEARCH_INPUT = (By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div/div[2]/div/div/input")
FIND_STUDENT = (By.XPATH, "//a[contains(text(), 'Find student')]")


class HomePageTutor(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._title = None
        self._search_input = None
        self._find_student = None

    @allure.step("Get title")
    def get_title(self) -> WebElement:
        if self._title is None:
            self._title = self.driver.find_element(*TITLE)
        return self._title

    @allure.step("Get title text")
    def get_title_text(self) -> str:
        return self.get_title().text

    @allure.step("Get search input")
    def get_search_input(self) -> WebElement:
        if self._search_input is None:
            self._search_input = self.driver.find_element(*SEARCH_INPUT)
        return self._search_input

    @allure.step("Get search input placeholder")
    def get_search_input_placeholder(self) -> str:
        return self.get_search_input().get_attribute("placeholder")

    @allure.step("Set search input text '{text}'")
    def set_search_input_text(self, text):
        self.get_search_input().send_keys(text)
        return self

    @allure.step("Get find student button")
    def get_find_student_btn(self) -> WebElement:
        if self._find_student is None:
            self._find_student = self.driver.find_element(*FIND_STUDENT)
        return self._find_student

    @allure.step("Click 'Find student' button")
    def click_find_student_btn(self) -> ExploreOffersPage:
        self.get_find_student_btn().click()
        return ExploreOffersPage(self.driver)
