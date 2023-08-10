from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.elements.home_page.search_tutorinput import SearchTutor
from SpaceToStudy.ui.pages.base_page import BasePage

SEARCH_INPUT = (By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div/div[2]")


class SearchTutorBlock(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._search_tutor = None

    def get_search_input(self) -> WebElement:
        if not self._search_tutor:
            node = self.driver.find_element(*SEARCH_INPUT)
            self._search_tutor = SearchTutor(node)
        return self._search_tutor
