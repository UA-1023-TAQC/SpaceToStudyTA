from selenium.webdriver.common.by import By

from SpaceToStudy.ui.elements.input import Input
from SpaceToStudy.ui.pages.base_page import BasePage

EMAIL_INPUT = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/form/div[1]")


class LoginModal(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._email_input = None

    def get_img(self):
        pass

    def get_email_input(self):
        node = self.driver.find_element(*EMAIL_INPUT)
        self._email_input = Input(node)
        return self._email_input
