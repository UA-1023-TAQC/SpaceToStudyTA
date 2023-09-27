from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_page import BasePage

STARTING_TEXT = (By.XPATH, "//form/div[1]/p")
IMAGE = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/div/img")
FIRST_NAME_INPUT = (By.XPATH, "//form/div[1]/div[1]/div[1]/div/input")
FIRST_NAME_LABEL = (By.XPATH, "//form/div[1]/div[1]/div[1]/label")
LAST_NAME_INPUT = (By.XPATH, "//form/div[1]/div[1]/div[2]/div/input")
LAST_NAME_LABEL = (By.XPATH, "//form/div[1]/div[1]/div[2]/label")
COUNTRY_INPUT = (By.XPATH, "//form/div[1]/div[1]/div[3]/div/div/input")
COUNTRY_LABEL = (By.XPATH, "//form/div[1]/div[1]/div[3]/div/label")
CITY_INPUT = (By.XPATH, "//form/div[1]/div[1]/div[4]/div/div/input")
CITY_LABEL = (By.XPATH, "//form/div[1]/div[1]/div[4]/div/label")
DESCRIPTION_INPUT = (By.XPATH, "//form/div[1]/div[2]/div/div/textarea[1]")
DESCRIPTION_LABEL = (By.XPATH, "//form/div[1]/div[2]/div/label")
SYMBOLS_COUNTER = (By.XPATH, "//form/div[1]/div[2]/p")


class GeneralPageStudent(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_starting_text(self) -> str:
        return self.driver.find_element(*STARTING_TEXT).text

    def get_image(self) -> WebElement:
        return self.driver.find_element(*IMAGE)

    def get_first_name_input(self) -> WebElement:
        return self.driver.find_element(*FIRST_NAME_INPUT)

    def set_first_name_input(self, text):
        self.get_first_name_input().send_keys(text)

    def get_first_name_label(self) -> WebElement:
        return self.driver.find_element(*FIRST_NAME_LABEL)

    def get_last_name_input(self) -> WebElement:
        return self.driver.find_element(*LAST_NAME_INPUT)

    def set_last_name_input(self, text):
        self.get_last_name_input().send_keys(text)

    def get_last_name_label(self) -> WebElement:
        return self.driver.find_element(*LAST_NAME_LABEL)

    def get_country_input(self) -> WebElement:
        return self.driver.find_element(*COUNTRY_INPUT)

    def set_country_input(self, text):
        self.get_country_input().send_keys(text)

    def get_country_label(self) -> WebElement:
        return self.driver.find_element(*COUNTRY_LABEL)

    def get_city_input(self) -> WebElement:
        return self.driver.find_element(*CITY_INPUT)

    def set_city_input(self, text):
        self.get_city_input().send_keys(text)

    def get_city_label(self) -> WebElement:
        return self.driver.find_element(*CITY_LABEL)

    def get_description_input(self) -> WebElement:
        return self.driver.find_element(*DESCRIPTION_INPUT)

    def set_description_input(self, text):
        self.get_description_input().send_keys(text)

    def get_description_label(self) -> WebElement:
        return self.driver.find_element(*DESCRIPTION_LABEL)

    def get_symbols_counter(self) -> WebElement:
        return self.driver.find_element(*SYMBOLS_COUNTER)

    def get_symbols_counter_text(self) -> str:
        return self.get_symbols_counter().text
