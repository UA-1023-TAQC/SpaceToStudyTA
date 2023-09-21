import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

ALL_BTN = (By.XPATH, "./button[1]")
ACTIVE_BTN = (By.XPATH, "./button[2]")
DRAFT_BTN = (By.XPATH, "./button[3]")
CLOSED_BTN = (By.XPATH, "./button[4]")


class SelectOffers:
    def __init__(self, node):
        self.node = node

    @allure.step("Get all button")
    def get_all_btn(self) -> WebElement:
        return self.node.find_element(*ALL_BTN)

    @allure.step("Get active button")
    def get_active_btn(self) -> WebElement:
        return self.node.find_element(*ACTIVE_BTN)

    @allure.step("Get draft button")
    def get_draft_btn(self) -> WebElement:
        return self.node.find_element(*DRAFT_BTN)

    @allure.step("Get close button")
    def get_closed_btn(self) -> WebElement:
        return self.node.find_element(*CLOSED_BTN)

    @allure.step("Click all button")
    def click_all_btn(self):
        self.get_all_btn().click()

    @allure.step("Click active button")
    def click_active_btn(self):
        self.get_active_btn().click()

    @allure.step("Click draft button")
    def click_draft_btn(self):
        self.get_draft_btn().click()

    @allure.step("Click close button")
    def click_closed_btn(self):
        self.get_closed_btn().click()
