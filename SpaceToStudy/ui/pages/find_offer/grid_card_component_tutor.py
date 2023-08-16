from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

AVATAR_LINK = (By.XPATH, "./div/div[1]/a")
AVATAR = (By.XPATH, "./div/div[1]/a/div/*[local-name()='svg']")
NICKNAME_TEXT = (By.XPATH, "./div/div[1]/div/a/p")
NICKNAME_LINK = (By.XPATH, "./div/div[1]/div/a")
STARS_COMPONENT = (By.XPATH, "./div/div[1]/div/div")
REVIEW_COUNTER = (By.XPATH, "./div/div[1]/div/p")

TITLE = (By.XPATH, "./div/div[2]/h6")
SUBJECT = (By.XPATH, "./div/div[2]/div[1]/div[1]/*[local-name()='span']")
SKILL_LEVEL = (By.XPATH, "./div/div[2]/div[1]/div[2]/*[local-name()='span']")
DESCRIPTION = (By.XPATH, "./div/div[2]/p")
LANGUAGES_ICON = (By.XPATH, "./div/div[2]/div[2]/*[local-name()='svg']")
LANGUAGES_TEXT = (By.XPATH, "./div/div[2]/div[2]/p")

PRICE = (By.XPATH, "./div/div[3]/div[1]/div/h6")
DURATION = (By.XPATH, "./div/div[3]/div[1]/div/p")
ADD_TO_FAVORITE_BUTTON = (By.XPATH, "./div/div[3]/div[1]/button")
VIEW_DETAILS_BUTTON = (By.XPATH, "./div/div[3]/div[2]/a/*[local-name()='span']")
VIEW_DETAILS_LINK = (By.XPATH, "./div/div[3]/div[2]/a")
SEND_MESSAGE_BUTTON = (By.XPATH, "./div/div[3]/div[2]/button")

"""
Full screen page
"""


class GridCardComponentTutor:
    def __init__(self, card_components: List[WebElement]):
        # super().__init__(card_components)
        self.card_components = card_components

    def get_sender_avatar_link(self, offer_id: int) -> WebElement:
        card_component = self.card_components[offer_id]
        return card_component.find_element(AVATAR_LINK)

    def click_sender_avatar_link(self, offer_id: int):
        self.get_sender_avatar_link(offer_id).click()

    def get_sender_avatar(self, offer_id: int) -> WebElement:
        card_component = self.card_components[offer_id]
        return card_component.find_element(*AVATAR)

    def get_sender_nickname_text(self, offer_id: int) -> str:
        card_component = self.card_components[offer_id]
        return card_component.find_element(*NICKNAME_TEXT).text

    def get_stars_component(self, offer_id: int) -> WebElement:
        card_component = self.card_components[offer_id]
        return card_component.find_element(*STARS_COMPONENT)

    def get_review_counter_text(self, offer_id: int) -> str:
        card_component = self.card_components[offer_id]
        return card_component.find_element(*REVIEW_COUNTER).text

    def get_title_text(self, offer_id: int) -> str:
        card_component = self.card_components[offer_id]
        return card_component.find_element(*TITLE).text

    def get_subject_text(self, offer_id: int) -> str:
        card_component = self.card_components[offer_id]
        return card_component.find_element(*SUBJECT).text

    def get_subject_element(self, offer_id: int) -> WebElement:
        card_component = self.card_components[offer_id]
        return card_component.find_element(*SUBJECT)

    def get_skill_level_text(self, offer_id: int) -> str:
        card_component = self.card_components[offer_id]
        return card_component.find_element(*SKILL_LEVEL).text

    def get_skill_level_element(self, offer_id: int) -> WebElement:
        card_component = self.card_components[offer_id]
        return card_component.find_element(*SKILL_LEVEL)

    def get_description_text(self, offer_id: int) -> str:
        card_component = self.card_components[offer_id]
        return card_component.find_element(*DESCRIPTION).text

    def get_languages_icon(self, offer_id: int) -> WebElement:
        card_component = self.card_components[offer_id]
        return card_component.find_element(*LANGUAGES_ICON)

    def get_languages_text(self, offer_id: int) -> str:
        card_component = self.card_components[offer_id]
        return card_component.find_element(*LANGUAGES_TEXT).text

    def get_price_text(self, offer_id: int) -> str:
        card_component = self.card_components[offer_id]
        return card_component.find_element(*PRICE).text

    def get_duration_text(self, offer_id: int) -> str:
        card_component = self.card_components[offer_id]
        return card_component.find_element(*DURATION).text

    def get_view_details_link(self, offer_id: int) -> WebElement:
        card_component = self.card_components[offer_id]
        return card_component.find_element(*VIEW_DETAILS_LINK)

    def click_view_details_link(self, offer_id: int):
        self.get_view_details_link(offer_id).click()

    def get_view_details_button(self, offer_id: int) -> WebElement:
        card_component = self.card_components[offer_id]
        return card_component.find_element(*VIEW_DETAILS_BUTTON)

    def get_add_to_favorite_button(self, offer_id: int) -> WebElement:
        card_component = self.card_components[offer_id]
        return card_component.find_element(*ADD_TO_FAVORITE_BUTTON)

    def click_add_to_favorite_button(self, offer_id: int):
        self.get_add_to_favorite_button(offer_id).click()

    def get_send_massage(self, offer_id: int) -> WebElement:
        card_component = self.card_components[offer_id]
        return card_component.find_element(*SEND_MESSAGE_BUTTON)

    def click_send_massage(self, offer_id: int):
        self.get_send_massage(offer_id).click()
