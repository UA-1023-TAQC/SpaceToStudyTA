from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_page import BasePage

TERMS = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/form/div[5]/label/span[2]/div/a[1]")
PRIVACY_POLICY = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/form/div[5]/label/span[2]/div/a[2]")
LOGIN = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/div/div[3]/p[2]")


class Link(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_terms(self) -> WebElement:
        return self.driver.find_element(*TERMS)

    def get_privacy_policy(self) -> WebElement:
        return self.driver.find_element(*PRIVACY_POLICY)

    def get_login(self) -> WebElement:
        return self.driver.find_element(*LOGIN)

    def click_terms(self):
        self.get_terms().click()

    def click_privacy_policy(self):
        self.get_privacy_policy().click()

    def click_login(self):
        self.get_login().click()
