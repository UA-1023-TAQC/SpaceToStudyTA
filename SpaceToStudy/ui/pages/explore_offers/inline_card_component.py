from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent

import re


PERSON_ICON = (By.XPATH, './div/div[1]/a/div/svg')
PERSON_NAME = (By.XPATH, './div/div[1]/div/a/p')
STARLINE_ELEMENT = (By.XPATH, './div/div[1]/div/div')
REVIEWS_LINE = (By.XPATH, './div/div[1]/div/p')
OFFER_TITLE = (By.XPATH, './div/div[2]/h6')
SUBJECT_LABEL = (By.XPATH, './div/div[2]/div[1]/div[1]/span/p')
LEVEL_LABEL = (By.XPATH, './div/div[2]/div[1]/div[2]/span/p')
OFFER_DETAILS = (By.XPATH, './div/div[2]/p')
LANGUAGES = (By.XPATH, './div/div[2]/div[2]/p')
PRICE_VALUE = (By.XPATH, './div/div[3]/div[1]/div/h6')

PERIOD_FOR_PRICE = (By.XPATH, './div/div[3]/div[1]/div/p')
VIEW_DETAILS_BTN = (By.XPATH, '//a[contains(text(), "View details")]')
SEND_MESSAGE_BTN = (By.XPATH, '//button[contains(text(), "Send message")]')
ADD_TO_BOOKMARKS_BTN = (By.XPATH, '//button[data-testid="iconButton"]')


class InlineCardComponent(BaseComponent):
    def __init__(self, node):
        super().__init__(node)

    def get_person_icon(self) -> WebElement:
        return self.node.find_element(*PERSON_ICON)

    def click_person_icon(self):
        self.get_person_icon().click()

    def get_person_name_element(self) -> WebElement:
        return self.node.find_element(*PERSON_NAME)

    def get_person_name(self) -> str:
        return self.node.find_element(*PERSON_NAME).text

    def get_starline_element(self) -> WebElement:
        return self.node.find_element(*STARLINE_ELEMENT)

    def get_reviews_line(self) -> str:
        return self.node.find_element(*REVIEWS_LINE).text

    def get_offer_title(self) -> str:
        return self.node.find_element(*OFFER_TITLE).text

    def get_subject_label(self) -> str:
        return self.node.find_element(*SUBJECT_LABEL).text

    def get_level_label(self) -> str:
        return self.node.find_element(*LEVEL_LABEL).text

    def get_offer_details(self) -> str:
        return self.node.find_element(*OFFER_DETAILS).text

    def get_languages(self) -> str:
        return self.node.find_element(*LANGUAGES).text

    def get_price_value(self) -> float:
        price_text = self.node.find_element(*PRICE_VALUE).text
        match = re.search(r'[\d.]+', price_text)
        price_value = float(match.group())
        return price_value

    def get_period_for_price(self) -> str:
        return self.node.find_element(*PERIOD_FOR_PRICE).text

    def get_view_details_btn(self) -> WebElement:
        return self.node.find_element(*VIEW_DETAILS_BTN)

    def get_view_details_btn_text(self) -> str:
        return self.node.find_element(*VIEW_DETAILS_BTN).text

    def click_view_details_btn(self):
        self.get_view_details_btn().click()

    def get_send_message_btn(self) -> WebElement:
        return self.node.find_element(*SEND_MESSAGE_BTN)

    def get_send_message_btn_text(self) -> str:
        return self.node.find_element(*SEND_MESSAGE_BTN).text

    def click_send_message_btn(self):
        self.get_send_message_btn().click()

    def get_add_to_bookmarks_btn(self) -> WebElement:
        return self.node.find_element(*ADD_TO_BOOKMARKS_BTN)

    def click_add_to_bookmarks_btn(self):
        self.get_add_to_bookmarks_btn().click()
