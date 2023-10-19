import allure
from selenium.webdriver.common.by import By

from SpaceToStudy.ui.pages.base_page import BasePage
from SpaceToStudy.ui.pages.categories.categories_page import CategoriesPage
from SpaceToStudy.ui.pages.explore_offers.explore_offers_page import ExploreOffersPage

FIND_STUDENT = (By.XPATH, "//a[contains(text(), 'Find student')]")
GO_TO_CATEGORIES = (By.XPATH, "//button[contains(text(), 'Go to categories')]")
MUSIC = (By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div[2]/div/a[1]/div/p")


class HomePageTutor(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._find_student = None
        self._go_to_categories = None
        self._music = None

    def get_find_student_btn(self):
        if self._find_student is None:
            self._find_student = self.driver.find_element(*FIND_STUDENT)
        return self._find_student

    @allure.step("Click on the 'Find student' button")
    def click_find_student_btn(self):
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