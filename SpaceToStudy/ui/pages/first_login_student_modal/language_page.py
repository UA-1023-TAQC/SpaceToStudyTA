from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_page import BasePage

IMAGE = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/div[1]/img")
STARTING_TEXT = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/div[2]/div[1]/p")
NATIVE_LANGUAGE_LABEL = (By.XPATH, "//div[@data-testid='language']/label")
NATIVE_LANGUAGE_INPUT = (By.XPATH, "//div[@data-testid='language']/div/input")


class LanguagePageStudent(BasePage):
    def get_image(self) -> WebElement:
        return self.driver.find_element(*IMAGE)

    def get_starting_text(self) -> str:
        return self.driver.find_element(*STARTING_TEXT).text

    def get_native_language_label(self) -> WebElement:
        return self.driver.find_element(*NATIVE_LANGUAGE_LABEL)

    def get_native_language_input(self) -> WebElement:
        return self.driver.find_element(*NATIVE_LANGUAGE_INPUT)

    def set_native_language_input(self, text):
        self.get_native_language_input().send_keys(text)