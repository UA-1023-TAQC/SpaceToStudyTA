import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent

PROGRESS_BAR_COMPLETION = (By.XPATH, ".//span")
NAME = (By.XPATH, "./p[1]")
COUNTER = (By.XPATH, "./p[2]")


class RatingProgressBar(BaseComponent):
    def __init__(self, node):
        super().__init__(node)
        self.node = node

    @allure.step("Get the rating progress bar name in 'What students say' block on 'My Profile' page")
    def get_rating_progress_bar_name_text(self) -> str:
        return self.node.find_element(*NAME).text

    @allure.step("Get the rating progress bar vote counter in 'What students say' block on 'My Profile' page")
    def get_rating_progress_bar_vote_counter_text(self) -> str:
        return self.node.find_element(*COUNTER).text

    @allure.step("Get the rating progress bar completion WebElement in 'What students say' block on 'My Profile' page")
    def get_rating_progress_bar_completion(self) -> WebElement:
        return self.node.find_element(*PROGRESS_BAR_COMPLETION)
