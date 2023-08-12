from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

CATEGORIES_BTN = (By.XPATH, ".[1]")
HOWITWORKS_BTN = (By.XPATH, ".[2]")
FAQ_BTN = (By.XPATH, ".[3]")


class StudentHeader:
    def __init__(self, node):
        self.node = node

    def get_categories_btn(self) -> WebElement:
        return self.node.find_element(*CATEGORIES_BTN)

    def get_howItWorks_btn(self) -> WebElement:
        return self.node.find_element(*HOWITWORKS_BTN)

    def get_faq_btn(self) -> WebElement:
        return self.node.find_element(*FAQ_BTN)

    def click_categories_btn(self):
        self.get_categories_btn().click()

    def click_howItWorks_btn(self):
        self.get_howItWorks_btn().click()

    def click_faq_btn(self):
        self.get_faq_btn().click()
