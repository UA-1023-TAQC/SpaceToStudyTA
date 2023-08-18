from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent

ALL_BTN = (By.XPATH, "./button[1]")
ACTIVE_BTN = (By.XPATH, "./button[2]")
DRAFT_BTN = (By.XPATH, "./button[3]")
CLOSED_BTN = (By.XPATH, "./button[4]")


class SelectOffers(BaseComponent):
    def __init__(self, node: WebElement):
        super().__init__(node)

    def get_all_btn(self) -> WebElement:
        return self.node.find_element(*ALL_BTN)

    def get_active_btn(self) -> WebElement:
        return self.node.find_element(*ACTIVE_BTN)

    def get_draft_btn(self) -> WebElement:
        return self.node.find_element(*DRAFT_BTN)

    def get_closed_btn(self) -> WebElement:
        return self.node.find_element(*CLOSED_BTN)

    def click_all_btn(self):
        self.get_all_btn().click()

    def click_active_btn(self):
        self.get_active_btn().click()

    def click_draft_btn(self):
        self.get_draft_btn().click()

    def click_closed_btn(self):
        self.get_closed_btn().click()
