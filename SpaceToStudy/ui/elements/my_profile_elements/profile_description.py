import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

NAME_SURNAME = (By.XPATH, "./div[1]/p")
TIME_IN_SPASE_TO_STUDY = (By.XPATH, "./div[3]/div[1]/p")
TEXT_UNDER_TIME_IN_SPASE_TO_STUDY = (By.XPATH, "./div[3]/div[1]/span")

PROFILE_RATING_NUMBER = (By.XPATH, "./div[3]/div[2]/span/div/div/p")
PROFILE_RATING_ICON = (By.XPATH, "./div[3]/div[2]/span/div/div/*[local-name()='svg']")
PROFILE_RATING_REVIEWS = (By.XPATH, "./div[3]/div[2]/span/div/a")

NATIVE_LANGUAGE_ICON = (By.XPATH, "./div[4]/div/div[1]/div[1]/div[1]/*[local-name()='svg']")
NATIVE_LANGUAGE_TEXT = (By.XPATH, "./div[4]/div/div[1]/div[1]/div[2]")

CITY_COUNTRY_BASED_ICON = (By.XPATH, "./div[4]/div/div[1]/div[2]/div[1]/*[local-name()='svg']")
CITY_COUNTRY_BASED_TEXT = (By.XPATH, "./div[4]/div/div[1]/div[2]/div[2]")


class ProfileDescription:
    def __init__(self, noda):
        self.noda = noda

    def get_name_surname_text(self) -> str:
        return self.noda.find_element(*NAME_SURNAME).text

    def get_time_in_spase2study_text(self) -> str:
         return self.noda.find_element(*TIME_IN_SPASE_TO_STUDY).text

    def get_text_under_time_in_spase2study_text(self) -> str:
        return self.noda.find_element(*TEXT_UNDER_TIME_IN_SPASE_TO_STUDY).text

    def get_native_language_text(self) -> str:
        return self.noda.find_element(*NATIVE_LANGUAGE_TEXT).text

    def get_native_language_icon(self) -> WebElement:
        return self.noda.find_element(*NATIVE_LANGUAGE_ICON)

    def get_profile_rating_number_text(self) -> str:
        return self.noda.find_element(*PROFILE_RATING_NUMBER).text

    def get_profile_rating_icon(self) -> WebElement:
        return self.noda.find_element(*PROFILE_RATING_ICON)

    def get_profile_rating_reviews_text(self) -> str:
        return self.noda.find_element(*PROFILE_RATING_REVIEWS).text

    def click_profile_rating_reviews(self):
        self.noda.find_element(*PROFILE_RATING_REVIEWS).click
        time.sleep(1)

    def get_city_country_based_text(self) -> str:
        return self.noda.find_element(*CITY_COUNTRY_BASED_TEXT).text

    def get_city_country_based_icon(self) -> WebElement:
        return self.noda.find_element(*CITY_COUNTRY_BASED_ICON)