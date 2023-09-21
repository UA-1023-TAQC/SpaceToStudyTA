from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent


PERSON_ICON = (By.XPATH, './div/div[1]/div[1]/a/div/svg')
PERSON_NAME = (By.XPATH, './div/div/div/a/p')
ADD_TO_BOOKMARKS_BTN = (By.XPATH, './div/div/div[1]/button')
LANGUAGES = (By.XPATH, './div/div[2]/div[2]/p')
OFFER_TITLE = (By.XPATH, './div/div[2]/h6')
SUBJECT_LABEL = (By.XPATH, './div/div[2]/div/div[1]/span/p')
LEVEL_LABEL = (By.XPATH, './div/div[2]/div/div[2]/span/p')

PRICE_VALUE = (By.XPATH, './div/div[3]/div/div/h6')
PRICE_PERIOD = (By.XPATH, './div/div[3]/div/div/p')

STAR_ICON = (By.XPATH, './/*[@data-testid="app-rating"]')
RATING_VALUE = (By.XPATH, './/*[@data-testid="app-rating"]/span[2]')
REVIEWS_LINE = (By.XPATH, './div/div/div[1]/p')

VIEW_DETAILS_BTN = (By.XPATH, '//a[contains(text(), "View details")]')
SEND_MESSAGE_BTN = (By.XPATH, '//button[contains(text(), "Send message")]')


class GridCardComponent(BaseComponent):
    def __init__(self, node):
        super().__init__(node)

    def get_person_icon(self) -> WebElement:
        return self.node.find_element(*PERSON_ICON)

    def click_person_icon(self):
        self.get_person_icon().click()

    def get_person_name(self):
        return self.node.find_element(*PERSON_NAME)

    def get_person_name_text(self) -> str:
        return self.node.find_element(*PERSON_NAME).text

    def click_person_name(self):
        self.get_person_name().click()

    def get_add_to_bookmarks_btn(self):
        return self.node.find_element(*ADD_TO_BOOKMARKS_BTN)

    def click_add_to_bookmarks_btn(self):
        self.get_add_to_bookmarks_btn().click()
        return self

    def get_languages(self) -> str:
        return self.node.find_element(*LANGUAGES).text

    def get_offer_title(self) -> str:
        return self.node.find_element(*OFFER_TITLE).text

    def get_subject_label(self) -> str:
        return self.node.find_element(*SUBJECT_LABEL).text

    def get_level_label(self) -> str:
        return self.node.find_element(*LEVEL_LABEL).text

    def get_price_value(self) -> str:
        return self.node.find_element(*PRICE_VALUE).text

    def get_period_for_price(self) -> str:
        return self.node.find_element(*PRICE_PERIOD).text

    def get_price_period(self) -> str:
        return self.node.find_element(*PRICE_PERIOD).text

    def get_star_icon(self) -> WebElement:
        return self.node.find_element(*STAR_ICON)

    def get_rating_value(self) -> str:
        return self.node.find_element(*RATING_VALUE).text

    def get_reviews_line(self) -> str:
        return self.node.find_element(*REVIEWS_LINE).text

    def get_view_details_btn(self) -> WebElement:
        return self.node.find_element(*VIEW_DETAILS_BTN)

    def click_view_details_btn(self):
        self.get_view_details_btn().click()

    def get_send_message_btn(self) -> WebElement:
        return self.node.find_element(*SEND_MESSAGE_BTN)

    def click_send_message_btn(self):
        self.get_send_message_btn().click()
