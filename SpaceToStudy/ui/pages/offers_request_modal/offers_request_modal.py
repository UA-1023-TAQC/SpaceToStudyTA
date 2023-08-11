from selenium.webdriver.common.by import By

from SpaceToStudy.ui.elements.input import Input
from SpaceToStudy.ui.pages.base_page import BasePage


CATEGORY_INPUT = (By.XPATH, "/html/body/div[2]/div[3]/form/div[1]/div[2]/div[1]/div[1]/div")
SUBJECT_INPUT = (By.XPATH, "/html/body/div[2]/div[3]/form/div[1]/div[2]/div[1]/div[2]/div")
CHECKBOXLEVELS = (By.XPATH, "/html/body/div[2]/div[3]/form/div[1]/div[2]/div[2]/div")


class OffersRequestModal(BasePage):
    def __init__(self, driver):
        super.__init__(driver)
        self._category_input = None
        self._subject_input = None
        self._checkbox_levels = None

    def get_category_input(self):
        node = self.driver.find_element(*CATEGORY_INPUT)
        self._category_input = Input(node)
        return self._category_input

    def get_subject_input(self):
        node = self.driver.find_element(*SUBJECT_INPUT)
        self._subject_input = Input(node)
        return self._subject_input
