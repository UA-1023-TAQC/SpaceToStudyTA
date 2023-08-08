import time

from selenium.webdriver.common.by import By
from typing import List

from selenium.webdriver.remote.webelement import WebElement

#/html/body/div/div/div[2]/div[2]/div[2]
#/html/body/div/div/div[2]/div[2]/div[2]

SHOW_HIDE_BUTTON = (By.XPATH, "./div[1]/div/div[1]/button")
COMPLETENESS_PERCENT = (By.XPATH, "./div[1]/div/div[2]/div[1]")
COMPLETENESS_PROGRESS_BAR = (By.XPATH, "./div[1]/div/div[2]/div[2]")

#TITLE_AND_DESCRIPTION_CONTAINER = (By.XPATH, "./div[1]/a")
TITLE = (By.XPATH, "./div[1]/div/div[1]/div/h5")
DESCRIPTION = (By.XPATH, "./div[1]/div/div[1]/div/h6")
PROFILE_COMPLETION_STEPS_CONTAINERS = (By.XPATH, "./div[2]/div/div/div/div")

class ProfileCompleteness:
    def __init__(self, node):
        self.noda = node

    def get_title_text(self) -> str:
        return self.noda.find_element(*TITLE)

    def get_title_description(self) -> str:
        return self.noda.find_element(*DESCRIPTION)

    def get_show_hide_button(self) -> WebElement:
        return self.noda.find_element(*SHOW_HIDE_BUTTON)

    def click_show_hide_button(self):
        self.noda.find_element(*SHOW_HIDE_BUTTON).click()
        time.sleep(1)

    def get_completeness_percent_array(self) -> List[str]:
        percent_array_web_elements = self.noda.find_element(*COMPLETENESS_PERCENT).find_elements(By.XPATH, "./h6")
        percent_array = [percent_element.text for percent_element in percent_array_web_elements]
        return percent_array

    def get_completeness_progress_bar(self) -> WebElement:
        return self.noda.find_element(*COMPLETENESS_PROGRESS_BAR)

    def get_profile_completion_steps_list(self) -> List[WebElement]:
        profile_completion_steps_list = self.noda.find_element(*PROFILE_COMPLETION_STEPS_CONTAINERS).find_elements(By.XPATH, "./div")
        return profile_completion_steps_list

    def get_profile_completion_step_title(self, profile_completion_step_container) -> str:
        completion_steps_container_title = profile_completion_step_container.text.split('\n')
        return completion_steps_container_title[0]

    def get_profile_completion_step_icon(self, profile_completion_step_container) -> WebElement:
        return profile_completion_step_container.find_element(By.XPATH, ".//*[local-name()='svg']")

    def get_profile_completion_step_description(self, profile_completion_step_container) -> str:
        completion_steps_container_title = profile_completion_step_container.text.split('\n')
        return completion_steps_container_title[1]



