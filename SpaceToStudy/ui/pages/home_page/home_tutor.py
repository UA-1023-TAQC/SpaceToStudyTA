from selenium.webdriver.common.by import By

from SpaceToStudy.ui.pages.base_page import BasePage
from SpaceToStudy.ui.pages.explore_offers.explore_offers_page import ExploreOffersPage

FIND_STUDENT = (By.XPATH, "//a[contains(text(), 'Find student')]")


class HomePageTutor(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._find_student = None

    def get_find_student_btn(self):
        if self._find_student is None:
            self._find_student = self.driver.find_element(*FIND_STUDENT)
        return self._find_student

    def click_find_student_btn(self):
        self.get_find_student_btn().click()
        return ExploreOffersPage(self.driver)
