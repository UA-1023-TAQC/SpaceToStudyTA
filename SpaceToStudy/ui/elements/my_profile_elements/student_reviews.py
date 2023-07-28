from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


TITLE = (By.XPATH, "./p")
RATING = (By.XPATH, "./div[1]/div[1]")
RATING_PROGRESS_BARS = (By.XPATH, "./div[1]/div[2]")
COMMENTS = (By.XPATH, "./div[2]/div")
MORE_RESULT_BUTTON = (By.XPATH, "./div[2]/button")

class StudentReviews:
    def __init__(self, noda):
        self.noda = noda

    def get_title_text(self) -> str:
        return self.noda.find_element(*TITLE).text

    def get_rating_number_text(self) -> str:
        return self.noda.find_element(*RATING).find_element(By.XPATH, ".//h4").text

    def get_review_counter_text(self) -> str:
        return self.noda.find_element(*RATING).find_element(By.XPATH, ".//p").text

    def get_reflects_the_stars_element(self) -> WebElement:
        return self.noda.find_element(*RATING).find_element(By.XPATH, ".//span")

    def get_rating_element(self) -> WebElement:
        return self.noda.find_element(*RATING)

    def get_rating_progress_bars_element(self) -> WebElement:
        return self.noda.find_element(*RATING_PROGRESS_BARS)

    def get_rating_progress_bars_list(self) -> List[WebElement]:
        return self.noda.find_element(*RATING_PROGRESS_BARS).find_elements(By.XPATH, "./div")

    def get_rating_progress_bar_name(self, rating_progress_bar) -> str:
        """
        Use func get_rating_progress_bars_list to create list of elements
        :param rating_progress_bar: WebElement
        :return: str
        """
        result = self.noda.find_element(*RATING_PROGRESS_BARS).find_elements(By.XPATH, ".//p")
        return result[0].text

    def get_rating_progress_bar_vote_counter(self, rating_progress_bar) -> str:
        """
        Use func get_rating_progress_bars_list to create list of elements
        :param rating_progress_bar: WebElement
        :return: str
        """
        result = self.noda.find_element(*RATING_PROGRESS_BARS).find_elements(By.XPATH, ".//p")
        return result[1].text

    def get_rating_progress_bar_span_element(self, rating_progress_bar) -> WebElement:
        """
        Use func get_rating_progress_bars_list to create list of elements
        :param rating_progress_bar: WebElement
        :return: str
        """
        return self.noda.find_element(*RATING_PROGRESS_BARS).find_element(By.XPATH, ".//span")



