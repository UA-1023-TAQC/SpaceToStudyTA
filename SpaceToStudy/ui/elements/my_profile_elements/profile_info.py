import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

AVATAR = (By.XPATH, "./div[1]/div[1]/div")
NAME_SURNAME = (By.XPATH, "./div[1]/div[2]/div[1]/p")
DAYS_IN_SPASE_TO_STUDY = (By.XPATH, "./div[1]/div[2]/div[3]/div[1]/p")
TEXT_UNDER_DAYS_IN_SPASE_TO_STUDY = (By.XPATH, "./div[1]/div[2]/div[3]/div[1]/span")
REVIEW_COUNTER = (By.XPATH, "./div[1]/div[2]/div[3]/div[2]/span/div/a")
EDIT_PROFILE_BUTTON = (By.XPATH, "./div[1]/a")

PROFILE_RATING_CONTAINER = (By.XPATH, "./div[1]/div[2]/div[3]/div[2]/span/div/div/p")
NATIVE_LANGUAGE_CONTAINER = (By.XPATH, "./div[1]/div[2]/div[4]/div/div[1]/div[1]")
CITY_COUNTRY_BASED_CONTAINER = (By.XPATH, "./div[1]/div[2]/div[4]/div/div[1]/div[2]")

class ProfileInfo:
    def __init__(self, noda):
        self.noda = noda

    def get_avatar(self):
        return self.noda.find_element(*AVATAR).find_element(By.XPATH, ".//*[local-name()='svg']")

    def get_name_surname_text(self) -> str:
        return self.noda.find_element(*NAME_SURNAME).text

    def get_days_in_spase2study_days_numbers_text(self) -> str:
         return self.noda.find_element(*DAYS_IN_SPASE_TO_STUDY).text

    def get_days_in_spase2study_text(self) -> str:
        return self.noda.find_element(*TEXT_UNDER_DAYS_IN_SPASE_TO_STUDY).text

    def get_native_language_text(self) -> str:
        return self.noda.find_element(*NATIVE_LANGUAGE_CONTAINER).text

    def get_native_language_icon(self) -> WebElement:
        return self.noda.find_element(*NATIVE_LANGUAGE_CONTAINER).find_element(By.XPATH, ".//*[local-name()='svg']")

    def get_profile_rating_text(self) -> str:
        return self.noda.find_element(*PROFILE_RATING_CONTAINER).text

    def get_profile_rating_icon(self) -> WebElement:
        return self.noda.find_element(*PROFILE_RATING_CONTAINER).find_element(By.XPATH, ".//*[local-name()='svg']")

    def get_review_counter_text(self) -> str:
        return self.noda.find_element(*REVIEW_COUNTER).text

    def get_city_country_based_text(self) -> str:
        return self.noda.find_element(*CITY_COUNTRY_BASED_CONTAINER).text

    def get_city_country_based_icon(self) -> str:
        return self.noda.find_element(*CITY_COUNTRY_BASED_CONTAINER).find_element(By.XPATH, ".//*[local-name()='svg']")

    def click_edit_profile_button(self):
        edit_profile_button = self.noda.find_element(*EDIT_PROFILE_BUTTON)
        edit_profile_button.click()

    def get_edit_profile_button(self) -> WebElement:
        return self.noda.find_element(*EDIT_PROFILE_BUTTON)