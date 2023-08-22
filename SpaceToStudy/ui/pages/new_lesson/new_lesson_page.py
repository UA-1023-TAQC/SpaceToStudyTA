from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_page import BasePage

TITLE = (By.XPATH, '//*[@id="mui-1291"]')
DESCRIPTION = (By.XPATH, '//*[@id="mui-1292"]')
BUILD_IN_APPLICATION = (By.XPATH, '//div[@role="application"]')
SAVE_BTN = (By.XPATH, '//button[text()="Save"]')
CANCEL_BTN = (By.XPATH, '//button[text()="Cancel"]')


class NewLessonPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_title_element(self) -> WebElement:
        return self.driver.find_element(*TITLE)

    def get_title_text(self) -> str:
        return self.driver.find_element(*TITLE).text

    def click_title(self):
        self.get_title_element().click()

    def set_title(self, title):
        self.get_title_element().send_keys(title)

    def get_description_element(self) -> WebElement:
        return self.driver.find_element(*DESCRIPTION)

    def get_description_text(self) -> str:
        return self.driver.find_element(*DESCRIPTION).text

    def click_description(self):
        self.get_description_element().click()

    def set_description(self, description):
        self.get_description_element().send_keys(description)

    def get_build_in_application(self) -> WebElement:
        return self.driver.find_element(*BUILD_IN_APPLICATION)

    def get_save_btn(self) -> WebElement:
        return self.driver.find_element(*SAVE_BTN)

    def get_save_btn_text(self) -> str:
        return self.driver.find_element(*SAVE_BTN).text

    def click_save_btn(self):
        self.get_save_btn().click()

    def get_cancel_btn(self) -> WebElement:
        return self.driver.find_element(*CANCEL_BTN)

    def get_cancel_btn_text(self) -> str:
        return self.driver.find_element(*CANCEL_BTN).text

    def click_cancel_btn(self):
        self.get_cancel_btn().click()

