from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.header.header import Header

LOGIN_BTN = (By.XPATH, "/html/body/div/div/header/div/div/button[3]")


class HeaderUnauthorized(Header):

    def __init__(self, driver):
        super().__init__(driver)

    def get_login_btn(self) -> WebElement:
        return self.driver.find_element(*LOGIN_BTN)

    def click_login_btn(self):
        self.get_login_btn().click()
