from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent

TABLE_BODY_CARD_VIEW = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[4]')
FIRST_CARD = (By.XPATH, f'{TABLE_BODY_CARD_VIEW}/div')
PERSON_ICON = (By.XPATH, f'{FIRST_CARD}/div[1]/div[1]/a/div/svg')
PERSON_NAME = (By.XPATH, f'{FIRST_CARD}/div[1]/div[1]/div/a/p')
CREATION_DATE = (By.XPATH, f'{FIRST_CARD}/div[1]/div[1]/div/p')
SUBJECT_LABEL = (By.XPATH, f'{FIRST_CARD}/div[2]/div[1]/span/p')
LEVEL_LABEL = (By.XPATH, f'{FIRST_CARD}/div[2]/div[2]/span/p')
OFFER_TITLE = (By.XPATH, f'{FIRST_CARD}/p')
PRICE_VALUE = (By.XPATH, f'{FIRST_CARD}/div[1]/div[2]/div[2]/p')
LAST_UPDATE = (By.XPATH, f'{FIRST_CARD}/div[1]/div[2]/div[2]/span')
STATUS_VALUE = (By.XPATH, f'{FIRST_CARD}/div[1]/div[2]/div[1]/span/p/span[2]')


class TableCardComponent(BaseComponent):
    def __init__(self, node):
        super().__init__(node)

    def get_first_card(self) -> WebElement:
        return self.driver.find_element(*FIRST_CARD)

    def click_first_card(self):
        self.get_first_card().click()

    def get_person_icon(self) -> WebElement:
        return self.driver.find_element(*PERSON_ICON)

    def click_person_icon(self):
        self.get_person_icon().click()

    def get_person_name_element(self) -> WebElement:
        return self.driver.find_element(*PERSON_NAME)

    def get_person_name(self) -> str:
        return self.driver.find_element(*PERSON_NAME).text

    def click_person_name_element(self):
        self.get_person_name_element().click()

    def get_creation_date(self) -> str:
        return self.driver.find_element(*CREATION_DATE).text

    def get_subject_label(self) -> str:
        return self.driver.find_element(*SUBJECT_LABEL).text

    def get_level_label(self) -> str:
        return self.driver.find_element(*LEVEL_LABEL).text

    def get_offer_title(self) -> str:
        return self.driver.find_element(*OFFER_TITLE).text

    def get_price_value(self) -> str:
        return self.driver.find_element(*PRICE_VALUE).text

    def get_last_update(self) -> str:
        return self.driver.find_element(*LAST_UPDATE).text
