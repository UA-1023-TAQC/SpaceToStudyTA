from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_page import BasePage

CHECKBOX = (By.XPATH, '//input[@class="PrivateSwitchBase-input css-1m9pwf3"]')


class Checkbox(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_checkbox(self) -> WebElement:
        return self.driver.find_element(*CHECKBOX)

    def click_checkbox(self):
        self.get_checkbox().click()
