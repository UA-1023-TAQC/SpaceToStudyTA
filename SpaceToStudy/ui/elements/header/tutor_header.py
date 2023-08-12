from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

CATEGORIES_BTN = (By.XPATH, ".[1]")
SUBJECTS_BTN = (By.XPATH, ".[2]")
OFFERS_BTN = (By.XPATH, ".[3]")
MYRESOURCES_BTN = (By.XPATH, ".[4]")


class TutorHeader:
    def __init__(self, node):
        self.node = node

    def get_categories_btn(self) -> WebElement:
        return self.node.find_element(*CATEGORIES_BTN)

    def get_subjects_btn(self) -> WebElement:
        return self.node.find_element(*SUBJECTS_BTN)

    def get_offers_btn(self) -> WebElement:
        return self.node.find_element(*OFFERS_BTN)

    def get_myResources_btn(self) -> WebElement:
        return self.node.find_element(*MYRESOURCES_BTN)

    def click_categories_btn(self):
        self.get_categories_btn().click()

    def click_subjects_btn(self):
        self.get_subjects_btn().click()

    def click_offers_btn(self):
        self.get_offers_btn().click()

    def click_myResources_btn(self):
        self.get_myResources_btn().click()
