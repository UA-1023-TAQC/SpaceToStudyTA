from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_page import BasePage
from SpaceToStudy.ui.pages.explore_offers.student_private_lesson_component import StudentPrivateLessonComponent

STUDENT_FOR_PRIVATE_LESSONS_BLOCK = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[1]")
TITLE = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[2]/p")
TEXT = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[2]/span")
BACK_TO_ALL_SUBJECT = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[3]/a")
LEFT_ARROW = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[3]/a/svg")
SEARCH_BY_TUTOR_NAME_BLOCK = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[4]/div")


class ExploreOffersPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._student_for_private_lessons_block = None

    def get_student_for_private_lessons_block(self):
        node = self.driver.find_element(*STUDENT_FOR_PRIVATE_LESSONS_BLOCK)
        if not self._student_for_private_lessons_block:
            self._student_for_private_lessons_block = StudentPrivateLessonComponent(node)
            return self._student_for_private_lessons_block

    def get_title(self) -> WebElement:
        return self.driver.find_element(*TITLE)

    def get_test(self) -> WebElement:
        return self.driver.find_element(*TEXT)

    def get_back_to_all_subject(self) -> WebElement:
        return self.driver.find_element(*BACK_TO_ALL_SUBJECT)

    def get_left_arrow(self) -> WebElement:
        return self.driver.find_element(*LEFT_ARROW)

    def click_back_to_all_subject(self):
        return self.get_back_to_all_subject().click()
