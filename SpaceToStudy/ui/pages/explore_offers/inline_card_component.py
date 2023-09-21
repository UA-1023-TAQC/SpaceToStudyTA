import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent

import re


PERSON_ICON = (By.XPATH, './div/div[1]/a/div/svg')
PERSON_NAME = (By.XPATH, './div/div/a/p')
STARLINE_ELEMENT = (By.XPATH, './div/div/div')
REVIEWS_LINE = (By.XPATH, './div/div/p')
OFFER_TITLE = (By.XPATH, './div[2]/h6')
SUBJECT_LABEL = (By.XPATH, './div[2]/div/div[1]/span/p')
LEVEL_LABEL = (By.XPATH, './div[2]/div/div[2]/span/p')
OFFER_DETAILS = (By.XPATH, './div/p')
LANGUAGES = (By.XPATH, './div/div[2]/p')
PRICE_VALUE = (By.XPATH, './div[3]/div[1]/div/h6')

PERIOD_FOR_PRICE = (By.XPATH, './div[3]/div[1]/div/p')
VIEW_DETAILS_BTN = (By.XPATH, './/a[contains(text(), "View details")]')
SEND_MESSAGE_BTN = (By.XPATH, './/button[contains(text(), "Send message")]')
ADD_TO_BOOKMARKS_BTN = (By.XPATH, './/button[@data-testid="iconButton"]')


class InlineCardComponent(BaseComponent):
    def __init__(self, node):
        super().__init__(node)

    @allure.step("Get person's icon")
    def get_person_icon(self) -> WebElement:
        return self.node.find_element(*PERSON_ICON)

    @allure.step("click on the person's icon")
    def click_person_icon(self):
        self.get_person_icon().click()

    @allure.step("Get person's name as an element")
    def get_person_name_element(self) -> WebElement:
        return self.node.find_element(*PERSON_NAME)

    @allure.step("Get person's name as a text")
    def get_person_name(self) -> str:
        return self.node.find_element(*PERSON_NAME).text

    @allure.step("Get starline as an element")
    def get_starline_element(self):
        from SpaceToStudy.ui.elements.starline import Starline
        starline_element = self.node.find_element(*STARLINE_ELEMENT)
        return Starline(starline_element)

    @allure.step("Get reviews line as a text")
    def get_reviews_line(self) -> str:
        return self.node.find_element(*REVIEWS_LINE).text

    @allure.step("Get offers title as a text")
    def get_offer_title(self) -> str:
        return self.node.find_element(*OFFER_TITLE).text

    @allure.step("Get subject label text")
    def get_subject_label(self) -> str:
        return self.node.find_element(*SUBJECT_LABEL).text

    @allure.step("Get level label")
    def get_level_label(self) -> str:
        return self.node.find_element(*LEVEL_LABEL).text

    @allure.step("Get offer details as a text")
    def get_offer_details(self) -> str:
        return self.node.find_element(*OFFER_DETAILS).text

    @allure.step("Get languages as a text")
    def get_languages(self) -> str:
        return self.node.find_element(*LANGUAGES).text

    @allure.step("Get price value")
    def get_price_value(self) -> float:
        price_text = self.node.find_element(*PRICE_VALUE).text
        match = re.search(r'[\d.]+', price_text)
        price_value = float(match.group())
        return price_value

    @allure.step("Get period for price as a text")
    def get_period_for_price(self) -> str:
        return self.node.find_element(*PERIOD_FOR_PRICE).text

    @allure.step("Get view details button")
    def get_view_details_btn(self) -> WebElement:
        return self.node.find_element(*VIEW_DETAILS_BTN)

    @allure.step("Get view details button as a text")
    def get_view_details_btn_text(self) -> str:
        return self.node.find_element(*VIEW_DETAILS_BTN).text

    @allure.step("Click on the view details button")
    def click_view_details_btn(self):
        self.get_view_details_btn().click()

    @allure.step("Get send message button")
    def get_send_message_btn(self) -> WebElement:
        return self.node.find_element(*SEND_MESSAGE_BTN)

    @allure.step("Get send message button as a text")
    def get_send_message_btn_text(self) -> str:
        return self.node.find_element(*SEND_MESSAGE_BTN).text

    @allure.step("Click on the send message button")
    def click_send_message_btn(self):
        self.get_send_message_btn().click()

    @allure.step("Get add to bookmarks button")
    def get_add_to_bookmarks_btn(self) -> WebElement:
        return self.node.find_element(*ADD_TO_BOOKMARKS_BTN)

    @allure.step("Click on the add to bookmarks button")
    def click_add_to_bookmarks_btn(self):
        self.get_add_to_bookmarks_btn().click()
