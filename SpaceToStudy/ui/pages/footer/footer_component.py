from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_page import BasePage

PRIVACY_POLICY = (By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div/div[2]")
TERM_OF_USE = (By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div/div[2]")
class Footer(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_privacy_policy(self) -> WebElement:
        return self.driver.find_element(*PRIVACY_POLICY)

    def click_privacy_policy(self):
        self.get_privacy_policy().click()

    def get_term_of_use(self) -> WebElement:
        return self.driver.find_element(*TERM_OF_USE)

    def click_term_of_use(self):
        self.get_term_of_use().click()

