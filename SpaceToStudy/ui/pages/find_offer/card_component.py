from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent

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


class CardComponent(BaseComponent):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self.node = node

    def get_sender_avatar_link(self) -> WebElement:
        return self.node.find_element(AVATAR_LINK)

    def click_sender_avatar_link(self):
        self.get_sender_avatar_link().click()

    def get_sender_avatar(self) -> WebElement:
        return self.node.find_element(*AVATAR)

    def get_sender_nickname_text(self) -> str:
        return self.node.find_element(*NICKNAME_TEXT).text

    def get_stars_component(self) -> WebElement:
        return self.node.find_element(*STARS_COMPONENT)

    def get_review_counter_text(self) -> str:
        return self.node.find_element(*REVIEW_COUNTER).text

    def get_title_text(self) -> str:
        return self.node.find_element(*TITLE).text

    def get_subject_text(self) -> str:
        return self.node.find_element(*SUBJECT).text

    def get_subject_element(self) -> WebElement:
        return self.node.find_element(*SUBJECT)

    def get_skill_level_text(self) -> str:
        return self.node.find_element(*SKILL_LEVEL).text

    def get_skill_level_element(self) -> WebElement:
        return self.node.find_element(*SKILL_LEVEL)

    def get_description_text(self) -> str:
        return self.node.find_element(*DESCRIPTION).text

    def get_languages_icon(self) -> WebElement:
        return self.node.find_element(*LANGUAGES_ICON)

    def get_languages_text(self) -> str:
        return self.node.find_element(*LANGUAGES_TEXT).text

    def get_price_text(self) -> str:
        return self.node.find_element(*PRICE).text

    def get_duration_text(self) -> str:
        return self.node.find_element(*DURATION).text

    def get_view_details_link(self) -> WebElement:
        return self.node.find_element(*VIEW_DETAILS_LINK)

    def click_view_details_link(self):
        self.get_view_details_link().click()

    def get_view_details_button(self) -> WebElement:
        return self.node.find_element(*VIEW_DETAILS_BUTTON)

    def get_add_to_favorite_button(self) -> WebElement:
        return self.node.find_element(*ADD_TO_FAVORITE_BUTTON)

    def click_add_to_favorite_button(self):
        self.get_add_to_favorite_button().click()

    def get_send_massage(self) -> WebElement:
        return self.node.find_element(*SEND_MESSAGE_BUTTON)

    def click_send_massage(self):
        self.get_send_massage().click()
