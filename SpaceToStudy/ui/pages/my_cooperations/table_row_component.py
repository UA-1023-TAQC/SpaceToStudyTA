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

    def click_person_name_element(self):
        self.get_person_name_element().click()

    def get_offer_title(self) -> str:
        return self.node.find_element(*OFFER_TITLE).text

    def get_subject_label(self) -> str:
        return self.node.find_element(*SUBJECT_LABEL).text

    def get_level_label(self) -> str:
        return self.node.find_element(*LEVEL_LABEL).text

    def get_price_value(self) -> str:
        return self.node.find_element(*PRICE_VALUE).text

    def get_last_update(self) -> str:
        return self.node.find_element(*LAST_UPDATE).text

    def get_status_value(self) -> str:
        return self.node.find_element(*STATUS_VALUE).text
