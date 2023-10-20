import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent

PERSON_ICON = (By.XPATH, './div[1]/div[1]/a/div/svg')
PERSON_NAME = (By.XPATH, './div[1]/div[1]/div/a/p')
CREATION_DATE = (By.XPATH, './div[1]/div[1]/div/p')
SUBJECT_LABEL = (By.XPATH, './div[2]/div[1]/span/p')
LEVEL_LABEL = (By.XPATH, './div[2]/div[2]/span/p')
OFFER_TITLE = (By.XPATH, './p')
PRICE_VALUE = (By.XPATH, './div[1]/div[2]/div[2]/p')
LAST_UPDATE = (By.XPATH, './div[1]/div[2]/div[2]/span')
STATUS_VALUE = (By.XPATH, './div[1]/div[2]/div[1]/span/p/span[2]')


class TableCardComponent(BaseComponent):  # Should we change the name to OfferCardComponent? it doesn't relate to table
    @allure.step("Get a person Icon when offers are displayed in the card format on my cooperations page")
    def get_person_icon(self) -> WebElement:
        return self.node.find_element(*PERSON_ICON)

    @allure.step("Click a person Icon when offers are displayed in the card format on my cooperations page")
    def click_person_icon(self):
        self.get_person_icon().click()

    @allure.step("Get a person Name element when offers are displayed in the card format on my cooperations page")
    def get_person_name_element(self) -> WebElement:
        return self.node.find_element(*PERSON_NAME)

    @allure.step("Get a person Name when offers are displayed in the card format on my cooperations page")
    def get_person_name(self) -> str:
        return self.node.find_element(*PERSON_NAME).text

    @allure.step("Click a person Name element when offers are displayed in the card format on my cooperations page")
    def click_person_name_element(self):
        self.get_person_name_element().click()

    @allure.step("Get an offer Last update date when offers are displayed in the card format on my cooperations page")
    def get_last_update(self) -> str:
        return self.node.find_element(*CREATION_DATE).text

    @allure.step("Get a Subject name when offers are displayed in the card format on my cooperations page")
    def get_subject_label(self) -> str:
        return self.node.find_element(*SUBJECT_LABEL).text

    @allure.step("Get a skill Level when offers are displayed in the card format on my cooperations page")
    def get_level_label(self) -> str:
        return self.node.find_element(*LEVEL_LABEL).text

    @allure.step("Get an Offer title when offers are displayed in the card format on my cooperations page")
    def get_offer_title(self) -> str:
        return self.node.find_element(*OFFER_TITLE).text

    @allure.step("Get an offer Price when offers are displayed in the card format on my cooperations page")
    def get_price_value(self) -> str:
        return self.node.find_element(*PRICE_VALUE).text
