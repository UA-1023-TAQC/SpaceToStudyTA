import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent

MODAL_COMPONENT = '/html/body/div[2]/div[3]/div/div/div/div'

PERSON_ICON = (By.XPATH, f'{MODAL_COMPONENT}/div/div[1]/div[1]/a/div/svg')
PERSON_NAME = (By.XPATH, f'{MODAL_COMPONENT}/div/div[1]/div[1]/div/a/p')
CREATION_DATE = (By.XPATH, f'{MODAL_COMPONENT}/div/div[1]/div[1]/div/p')
SUBJECT_LABEL = (By.XPATH, f'{MODAL_COMPONENT}/div/div[2]/div[1]/span/p')
LEVEL_LABEL = (By.XPATH, f'{MODAL_COMPONENT}/div/div[2]/div[2]/span/p')
OFFER_TITLE = (By.XPATH, f'{MODAL_COMPONENT}/div/p')
PRICE_VALUE = (By.XPATH, f'{MODAL_COMPONENT}/div/div[1]/div[2]/div[2]/p')
PRICE_PERIOD = (By.XPATH, f'{MODAL_COMPONENT}/div/div[1]/div[2]/div[2]/span')
STATUS_VALUE = (By.XPATH, f'{MODAL_COMPONENT}/div/div[1]/div[2]/div[1]/span/p/span[2]')

ACCEPT_NEW_COOPERATION_TITLE = (By.XPATH, f'{MODAL_COMPONENT}/form/p')
APPROPRIATE_LEVEL_TAG = (By.XPATH, f'{MODAL_COMPONENT}/form/div[1]/p')
APPROPRIATE_LEVEL_VALUE = (By.XPATH, f'{MODAL_COMPONENT}/form/div[1]/span')
PRICE_IN_OFFER_TAG = (By.XPATH, f'{MODAL_COMPONENT}/form/div[2]/p')
PRICE_IN_OFFER_VALUE = (By.XPATH, f'{MODAL_COMPONENT}/form/div[2]/span')
SUGGESTED_PRICE_TAG = (By.XPATH, f'{MODAL_COMPONENT}/form/div[3]/p')
SUGGESTED_PRICE_VALUE = (By.XPATH, f'{MODAL_COMPONENT}/form/div[3]/span')

DECLINE_COOPERATION_BTN = (By.XPATH, '//button[text()="Decline cooperation"]')


class MyCooperationsModalComponent(BaseComponent):
    def __init__(self, node):
        super().__init__(node)

    @allure.step("Get the person icon element")
    def get_person_icon(self) -> WebElement:
        return self.node.find_element(*PERSON_ICON)

    @allure.step("Click on the person icon")
    def click_person_icon(self):
        self.get_person_icon().click()

    @allure.step("Get the person name element")
    def get_person_name_element(self) -> WebElement:
        return self.node.find_element(*PERSON_NAME)

    @allure.step("Get the person name")
    def get_person_name(self) -> str:
        return self.node.find_element(*PERSON_NAME).text

    @allure.step("Click on the person name element")
    def click_person_name_element(self):
        self.get_person_name_element().click()

    @allure.step("Get the creation date")
    def get_creation_date(self) -> str:
        return self.node.find_element(*CREATION_DATE).text

    @allure.step("Get the subject label")
    def get_subject_label(self) -> str:
        return self.node.find_element(*SUBJECT_LABEL).text

    @allure.step("Get the level label")
    def get_level_label(self) -> str:
        return self.node.find_element(*LEVEL_LABEL).text

    @allure.step("Get the offer title")
    def get_offer_title(self) -> str:
        return self.node.find_element(*OFFER_TITLE).text

    @allure.step("Get the price value")
    def get_price_value(self) -> str:
        return self.node.find_element(*PRICE_VALUE).text

    @allure.step("Get the price period")
    def get_price_period(self) -> str:
        return self.node.find_element(*PRICE_PERIOD).text

    @allure.step("Get the status value")
    def get_status_value(self) -> str:
        return self.node.find_element(*STATUS_VALUE).text

    @allure.step("Get the accept new cooperation title")
    def get_accept_new_cooperation_title(self) -> str:
        return self.node.find_element(*ACCEPT_NEW_COOPERATION_TITLE).text

    @allure.step("Get the appropriate level tag")
    def get_appropriate_level_tag(self) -> str:
        return self.node.find_element(*APPROPRIATE_LEVEL_TAG).text

    @allure.step("Get the appropriate level value")
    def get_appropriate_level_value(self) -> str:
        return self.node.find_element(*APPROPRIATE_LEVEL_VALUE).text

    @allure.step("Get the price in offer tag")
    def get_price_in_offer_tag(self) -> str:
        return self.node.find_element(*PRICE_IN_OFFER_TAG).text

    @allure.step("Get the price in offer value")
    def get_price_in_offer_value(self) -> str:
        return self.node.find_element(*PRICE_IN_OFFER_VALUE).text

    @allure.step("Get the suggested price tag")
    def get_suggested_price_tag(self) -> str:
        return self.node.find_element(*SUGGESTED_PRICE_TAG).text

    @allure.step("Get the suggested price tag")
    def get_suggested_price_value(self) -> str:
        return self.node.find_element(*SUGGESTED_PRICE_VALUE).text

    @allure.step("Get the 'Decline Cooperation' button element")
    def get_decline_cooperation_btn(self) -> WebElement:
        return self.node.find_element(*DECLINE_COOPERATION_BTN)

    @allure.step("Click on the 'Decline Cooperation' button")
    def click_decline_cooperation_btn(self):
        self.get_decline_cooperation_btn().click()
