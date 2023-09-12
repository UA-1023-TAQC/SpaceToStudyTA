from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_page import BasePage
from SpaceToStudy.ui.pages.categories.tutor_private_lesson_component import TutorPrivateLessonComponent
from SpaceToStudy.ui.pages.explore_offers.explore_offers_page import ExploreOffersPage


CATEGORIES_TITLE = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/p')
CATEGORIES_SUBTEXT = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/span')
SHOW_ALL_OFFERS_BTN = (By.XPATH, '//a[text()="Show all offers"]')
SEARCH_BTN = (By.XPATH, '//button[text()="Search"]')
SEARCH_INPUT = (By.XPATH, './input')
SEARCH_FIELD_HELP_TEXT = (By.XPATH, '//*[@id="mui-2488-label"]')
STUDENT_PRIVATE_LESSON_COMPONENT = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[1]")

NO_RESULT_TITLE = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[4]/div/div/p")


class CategoriesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._no_result_title = None

    def get_categories_title(self) -> str:
        return self.driver.find_element(*CATEGORIES_TITLE).text

    def get_categories_subtext(self) -> str:
        return self.driver.find_element(*CATEGORIES_SUBTEXT).text

    def get_show_all_offers_btn(self) -> WebElement:
        return self.driver.find_element(*SHOW_ALL_OFFERS_BTN)

    def click_show_all_offers_btn(self):
        self.get_show_all_offers_btn().click()
        return ExploreOffersPage(self.driver)

    def get_search_btn(self) -> WebElement:
        return self.driver.find_element(*SEARCH_BTN)

    def click_search_btn(self):
        self.get_search_btn().click()

    def get_search_input(self) -> WebElement:
        return self.driver.find_element(*SEARCH_INPUT)

    def set_search(self, text):
        self.get_search_input().send_keys(text)

    def get_search_field_help_text(self) -> str:
        return self.driver.find_element(*SEARCH_FIELD_HELP_TEXT).text

    def get_student_private_lesson_component(self) -> TutorPrivateLessonComponent:
        return TutorPrivateLessonComponent(self.driver.find_element(*STUDENT_PRIVATE_LESSON_COMPONENT))

    def get_no_result_title(self) -> str:
        if not self._no_result_title:
            self._no_result_title = self.driver.find_element(*NO_RESULT_TITLE)
        return self._no_result_title.text

