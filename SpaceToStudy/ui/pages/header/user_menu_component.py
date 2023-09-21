import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent

MESSAGES = (By.XPATH, "./a")
NOTIFICATIONS = (By.XPATH, "./button[1]")
ACCOUNT = (By.XPATH, "./button[2]")


class UserMenuComponent(BaseComponent):
    def __init__(self, node: WebElement):
        super().__init__(node)

    @allure.step("Get 'Messages' user menu item")
    def get_messages(self) -> WebElement:
        return self.node.find_element(*MESSAGES)

    @allure.step("Get 'Notifications' user menu item")
    def get_notifications(self) -> WebElement:
        return self.node.find_element(*NOTIFICATIONS)

    @allure.step("Get 'Account' user menu item")
    def get_account(self) -> WebElement:
        return self.node.find_element(*ACCOUNT)

    @allure.step("Click 'Messages' user menu item")
    def click_get_messages(self):
        self.get_messages().click()

    @allure.step("Click 'Notifications' user menu item")
    def click_get_notifications(self):
        self.get_notifications().click()

    @allure.step("Click 'Account' user menu item")
    def click_account(self):
        from SpaceToStudy.ui.pages.header.menu_items import MenuItems
        self.get_account().click()
        return MenuItems(self.node.find_element(By.XPATH, "/html/body/div[2]/div[3]"))
