import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_page import BasePage
from SpaceToStudy.ui.pages.categories.categories_page import CategoriesPage
from SpaceToStudy.ui.pages.explore_offers.explore_offers_page import ExploreOffersPage

TITLE = (By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div/div[1]/p")
DESCRIPTION = (By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div/div[1]/span")
SEARCH_INPUT = (By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div/div[2]/div/div/input")
FIND_STUDENT = (By.XPATH, "//a[contains(text(), 'Find student')]")
FLASHING_BTN = (By.XPATH, "//a[contains(@class, 'focusVisible')]")
GO_TO_CATEGORIES = (By.XPATH, "//button[contains(text(), 'Go to categories')]")
MUSIC = (By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div[2]/div/a[1]/div/p")


class HomePageTutor(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._title = None
        self._description = None
        self._search_input = None
        self._find_student = None
        self._go_to_categories = None
        self._music = None

    @allure.step("Get title")
    def get_title(self) -> WebElement:
        if self._title is None:
            self._title = self.driver.find_element(*TITLE)
        return self._title

    @allure.step("Get title text")
    def get_title_text(self) -> str:
        return self.get_title().text

    @allure.step("Get description element")
    def get_description(self) -> WebElement:
        if self._description is None:
            self._description = self.driver.find_element(*DESCRIPTION)
        return self._description

    @allure.step("Get description text")
    def get_description_text(self) -> str:
        return self.get_description().text

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

    @allure.step("Check if 'Find student' button is flashing")
    def check_find_student_btn_is_flashing(self) -> bool:
        found = self.get_find_student_btn().parent.find_elements(*FLASHING_BTN)
        return len(found) > 0

    @allure.step("Click on the 'Find student' button")
    def click_find_student_btn(self) -> ExploreOffersPage:
        self.get_find_student_btn().click()
        return ExploreOffersPage(self.driver)

    def get_go_to_categories_btn(self):
        if self._go_to_categories is None:
            self._go_to_categories = self.driver.find_element(*GO_TO_CATEGORIES)
        return self._go_to_categories

    @allure.step("Click on the 'Go to categories' button")
    def click_go_to_categories_btn(self):
        self.get_go_to_categories_btn().click()
        return CategoriesPage(self.driver)

    @allure.step("Get music button")
    def get_music_btn(self):
        if self._music is None:
            self._music = self.driver.find_element(*MUSIC)
        return self._music

    @allure.step("Click music button")
    def click_music_btn(self):
        self.get_music_btn().click()
        return CategoriesPage(self.driver)