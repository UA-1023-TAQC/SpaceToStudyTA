from time import sleep
from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_page import BasePage

# PROFILE_COMPLETENESS = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[2]")
# VIDEO_PRESENTATION = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[3]")
# STUDENT_REVIEW = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[4]")

AVATAR = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[1]/div[1]/div/*[local-name()='svg']")
EDIT_PROFILE_BUTTON = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[1]/a")

NAME_SURNAME = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[1]/div[2]/div[1]/p")
TIME_IN_SPASE_TO_STUDY = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/p")
TEXT_UNDER_TIME_IN_SPASE_TO_STUDY = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/span")

PROFILE_RATING_NUMBER = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]/span/div/div/p")
PROFILE_RATING_ICON = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]/span/div/div/*[local-name()='svg']")
PROFILE_RATING_REVIEWS = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]/span/div/a")

NATIVE_LANGUAGE_ICON = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[1]/div[2]/div[4]/div/div[1]/div[1]/div[1]/*[local-name()='svg']")
NATIVE_LANGUAGE_TEXT = (By.XPATH, "./div[4]/div/div[1]/div[1]/div[2]")

CITY_COUNTRY_BASED_ICON = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[1]/div[2]/div[4]/div/div[1]/div[2]/div[1]/*[local-name()='svg']")
CITY_COUNTRY_BASED_TEXT = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[1]/div[2]/div[4]/div/div[1]/div[2]/div[2]")

COMPLETENESS_SHOW_HIDE_BUTTON = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div/div[1]/button")
COMPLETENESS_PERCENT = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div/div[2]/div[1]/h6")
COMPLETENESS_PROGRESS_BAR = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div/div[2]/div[2]")

COMPLETENESS_TITLE = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div/div[1]/div/h5")
COMPLETENESS_DESCRIPTION = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div/div[1]/div/h6")
COMPLETENESS_STEPS_CONTAINERS = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[4]/div[2]/div/div")

VIDEO_PRESENTATION_TITLE = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[3]/p")
VIDEO_PRESENTATION_TITLE_BAR = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[3]/div/img")
VIDEO = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[3]/div/div/img")

REVIEWS_TITLE = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[4]/p")
RATING_NUMBER = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[4]/div[1]/div[1]/div[1]/h4")
RATING_STARS_CONTAINER = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[4]/div[1]/div[1]/div[2]/span")
RATING_REVIEW_COUNTER = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[4]/div[1]/div[1]/p")

RATING_PROGRESS_BARS = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[4]/div[1]/div[2]/div")
COMMENTS = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[4]/div[2]/div/div")
MORE_REVIEW_BUTTON = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[4]/div[2]/button")


class MyProfile(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.more_review_button = None
        self.reviews_title = None
        self.video = None
        self.video_presentation_title_bar = None
        self.video_presentation_title = None
        self.completeness_steps_containers = None
        self.completeness_progress_bar = None
        self.completeness_percent_array = None
        self.completeness_show_hide_button = None
        self.completeness_description = None
        self.completeness_title = None
        self.city_country_based_icon = None
        self.profile_rating_icon = None
        self.native_language_icon = None
        self.text_under_time_in_spase_to_study = None
        self.edit_profile_button = None
        self.avatar = None

    def get_avatar(self) -> WebElement:
        return self.driver.find_element(*AVATAR)

    def get_edit_profile_button(self) -> WebElement:
        if not self.edit_profile_button:
            self.edit_profile_button = self.driver.find_element(*EDIT_PROFILE_BUTTON)
        return self.edit_profile_button

    def click_edit_profile_button(self):
        self.get_edit_profile_button().click()
        sleep(1)

    def get_name_surname_text(self) -> str:
        return self.driver.find_element(*NAME_SURNAME).text

    def get_time_in_spase2study_text(self) -> str:
        return self.driver.find_element(*TIME_IN_SPASE_TO_STUDY).text

    def get_text_under_time_in_spase2study_text(self) -> str:
        if not self.text_under_time_in_spase_to_study:
            self.text_under_time_in_spase_to_study = self.driver.find_element(*TEXT_UNDER_TIME_IN_SPASE_TO_STUDY).text
        return self.text_under_time_in_spase_to_study

    def get_native_language_text(self) -> str:
        return self.driver.find_element(*NATIVE_LANGUAGE_TEXT).text

    def get_native_language_icon(self) -> WebElement:
        return self.driver.find_element(*NATIVE_LANGUAGE_ICON)

    def get_profile_rating_number_text(self) -> str:
        return self.driver.find_element(*PROFILE_RATING_NUMBER).text

    def get_profile_rating_icon(self) -> WebElement:
        if not self.profile_rating_icon:
            self.profile_rating_icon = self.driver.find_element(*PROFILE_RATING_ICON)
        return self.profile_rating_icon

    def get_profile_rating_reviews_text(self) -> str:
        return self.driver.find_element(*PROFILE_RATING_REVIEWS).text

    def get_profile_rating_reviews(self) -> WebElement:
        return self.driver.find_element(*PROFILE_RATING_REVIEWS)

    def click_profile_rating_reviews(self):
        self.get_profile_rating_reviews().click()
        sleep(1)

    def get_city_country_based_text(self) -> str:
        return self.driver.find_element(*CITY_COUNTRY_BASED_TEXT).text

    def get_city_country_based_icon(self) -> WebElement:
        if not self.city_country_based_icon:
            self.city_country_based_icon = self.driver.find_element(*CITY_COUNTRY_BASED_ICON)
        return self.city_country_based_icon

    def get_completeness_title_text(self) -> str:
        if not self.completeness_title:
            self.completeness_title = self.driver.find_element(*COMPLETENESS_TITLE).text
        return self.completeness_title

    def get_completeness_title_description(self) -> str:
        if not self.completeness_description:
            self.completeness_description = self.driver.find_element(*COMPLETENESS_DESCRIPTION).text
        return self.completeness_description

    def get_show_hide_button(self) -> WebElement:
        if not self.completeness_show_hide_button:
            self.completeness_show_hide_button = self.driver.find_element(*COMPLETENESS_SHOW_HIDE_BUTTON)
        return self.completeness_show_hide_button

    def click_show_hide_button(self):
        self.get_show_hide_button().click()
        sleep(1)

    def get_completeness_percent_array(self) -> List[str]:
        if not self.completeness_percent_array:
            percent_array_web_elements = self.driver.find_elements(*COMPLETENESS_PERCENT)
            self.completeness_percent_array = [percent_element.text for percent_element in percent_array_web_elements]
        return self.completeness_percent_array

    def get_completeness_progress_bar(self) -> WebElement:
        if not self.completeness_progress_bar:
            self.completeness_progress_bar = self.driver.find_element(*COMPLETENESS_PROGRESS_BAR)
        return self.completeness_progress_bar

    def get_profile_completion_steps_containers(self) -> List[WebElement]:
        if not self.completeness_steps_containers:
            self.completeness_steps_containers = self.driver.find_elements(*COMPLETENESS_STEPS_CONTAINERS)
        return self.completeness_steps_containers

    # DONE

    def get_video_presentation_title_text(self) -> str:
        if not self.video_presentation_title:
            self.video_presentation_title = self.driver.find_element(*VIDEO_PRESENTATION_TITLE).text
        return self.video_presentation_title

    def get_video_presentation_title_bar(self) -> WebElement:
        if not self.video_presentation_title_bar:
            self.video_presentation_title_bar = self.driver.find_element(*VIDEO_PRESENTATION_TITLE_BAR)
        return self.video_presentation_title_bar

    def get_video(self) -> WebElement:
        """
        While documenting the test procedure, it's important to note that during the testing phase,
        the developer employed image elements instead of video elements.
        :return: WebElement
        """
        if not self.video:
            self.video = self.driver.find_element(*VIDEO)
        return self.video

    # -------------------------

    def get_reviews_title_text(self) -> str:
        if not self.reviews_title:
            self.reviews_title = self.driver.find_element(*REVIEWS_TITLE)
        return self.reviews_title.text

    def get_rating_number_text(self) -> str:
        return self.driver.find_element(*RATING_NUMBER).text

    def get_review_counter_text(self) -> str:
        return self.driver.find_element(*RATING_REVIEW_COUNTER).text

    def get_stars_container(self) -> WebElement:
        return self.driver.find_element(*RATING_STARS_CONTAINER)

    def get_rating_progress_bars_list(self) -> List[WebElement]:
        return self.driver.find_elements(*RATING_PROGRESS_BARS)

    def get_students_comments_list(self) -> List[WebElement]:
        return self.driver.find_elements(*COMMENTS)

    def get_student_more_review_button(self) -> WebElement:
        if not self.more_review_button:
            self.more_review_button = self.driver.find_element(*MORE_REVIEW_BUTTON)
        return self.more_review_button

    def student_more_review_button_click(self):
        self.get_student_more_review_button().click()
