import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_page import BasePage

IMAGE = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/div[1]/img")
STARTING_TEXT = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/div[2]/div[1]/p")
NATIVE_LANGUAGE_LABEL = (By.XPATH, "//div[@data-testid='language']/label")
NATIVE_LANGUAGE_INPUT = (By.XPATH, "//div[@data-testid='language']/div/input")


class LanguagePageStudent(BasePage):
    @allure.step("Get image")
    def get_image(self) -> WebElement:
        return self.driver.find_element(*IMAGE)

    @allure.step("Get starting text")
    def get_starting_text(self) -> str:
        return self.driver.find_element(*STARTING_TEXT).text

    @allure.step("Get native language label")
    def get_native_language_label(self) -> WebElement:
        return self.driver.find_element(*NATIVE_LANGUAGE_LABEL)

    @allure.step("Get native language input")
    def get_native_language_input(self) -> WebElement:
        return self.driver.find_element(*NATIVE_LANGUAGE_INPUT)

    @allure.step("Set native language input")
    def set_native_language_input(self, text):
        self.get_native_language_input().send_keys(text)
