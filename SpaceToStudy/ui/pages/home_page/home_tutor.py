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
        self._find_student = None

    def get_title(self) -> WebElement:
        return self.driver.find_element(*TITLE)

    def get_search_input(self) -> WebElement:
        return self.driver.find_element(*SEARCH_INPUT)

    def get_search_field_placeholder(self) -> str:
        return self.get_search_input().get_attribute("placeholder")

    def set_search_input_text(self, text):
        self.get_search_input().send_keys(text)
        return self

    def get_find_student_btn(self) -> WebElement:
        if self._find_student is None:
            self._find_student = self.driver.find_element(*FIND_STUDENT)
        return self._find_student

    def click_find_student_btn(self) -> ExploreOffersPage:
        self.get_find_student_btn().click()
        return ExploreOffersPage(self.driver)
