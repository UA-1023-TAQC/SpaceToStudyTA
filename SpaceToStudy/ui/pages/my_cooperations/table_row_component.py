import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent

PERSON_ICON = (By.XPATH, './td[1]/div/a/div/svg')
PERSON_NAME = (By.XPATH, './td[1]/div/div/a/p')
OFFER_TITLE = (By.XPATH, './td[2]/p')
SUBJECT_LABEL = (By.XPATH, './td[3]/div/div[1]/span/p')
LEVEL_LABEL = (By.XPATH, './td[3]/div/div[2]/span/p')
PRICE_VALUE = (By.XPATH, './td[4]')
LAST_UPDATE = (By.XPATH, './td[5]')
STATUS_VALUE = (By.XPATH, './td[6]/div/span/p/span[2]')


class TableRowComponent(BaseComponent):
    @allure.step("Get a person Icon for offer in the offers table on my cooperations page")
    def get_person_icon(self) -> WebElement:
        return self.node.find_element(*PERSON_ICON)

    @allure.step("Click a person Icon for offer in the offers table on my cooperations page")
    def click_person_icon(self):
        self.get_person_icon().click()

    @allure.step("Get a person Name element for offer in the offers table on my cooperations page")
    def get_person_name_element(self) -> WebElement:
        return self.node.find_element(*PERSON_NAME)

    @allure.step("Get a person Name for offer in the offers table on my cooperations page")
    def get_person_name(self) -> str:
        return self.node.find_element(*PERSON_NAME).text

    @allure.step("Click a person Name element for offer in the offers table on my cooperations page")
    def click_person_name_element(self):
        self.get_person_name_element().click()

    @allure.step("Get an Offer title for offer in the offers table on my cooperations page")
    def get_offer_title(self) -> str:
        return self.node.find_element(*OFFER_TITLE).text

    @allure.step("Get a Subject name for offer in the offers table on my cooperations page")
    def get_subject_label(self) -> str:
        return self.node.find_element(*SUBJECT_LABEL).text

    @allure.step("Get a skill Level for offer in the offers table on my cooperations page")
    def get_level_label(self) -> str:
        return self.node.find_element(*LEVEL_LABEL).text

    @allure.step("Get an offer Price in the offers table on my cooperations page")
    def get_price_value(self) -> str:
        return self.node.find_element(*PRICE_VALUE).text

    @allure.step("Get an offer Last update date in the offers table on my cooperations page")
    def get_last_update(self) -> str:
        return self.node.find_element(*LAST_UPDATE).text

    @allure.step("Get an offer Status in the offers table on my cooperations page")
    def get_status_value(self) -> str:
        return self.node.find_element(*STATUS_VALUE).text
