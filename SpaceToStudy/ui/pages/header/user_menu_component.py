from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent
from SpaceToStudy.ui.pages.header.menu_items import MenuItems

MESSAGES = (By.XPATH, "./a")
NOTIFICATIONS = (By.XPATH, "./button[1]")
ACCOUNT = (By.XPATH, "./button[2]")


class UserMenuComponent(BaseComponent):
    def __init__(self, node: WebElement):
        super().__init__(node)

    def get_messages(self) -> WebElement:
        return self.node.find_element(*MESSAGES)

    def get_notifications(self) -> WebElement:
        return self.node.find_element(*NOTIFICATIONS)

    def get_account(self) -> WebElement:
        return self.node.find_element(*ACCOUNT)

    def click_get_messages(self):
        self.get_messages().click()

    def click_get_notifications(self):
        self.get_notifications().click()

    def click_get_account(self):
        self.get_account().click()
        return MenuItems(self.node.find_element(By.XPATH, "/html/body/div[2]/div[3]"))
