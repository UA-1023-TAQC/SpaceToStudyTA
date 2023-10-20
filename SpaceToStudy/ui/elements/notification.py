import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.elements.base_element import BaseElement

NOTIFICATION = (By.XPATH, "/html/body/div/div[2]")
NOTIFICATION_TEXT = (By.XPATH, "//*[@id='root']/div[2]/div")


class Notification(BaseElement):

    def __init__(self, node: WebElement):
        super().__init__(node)
        self._notification = None
        self._notification_text = None

    @allure.step("Get notification")
    def get_notification(self) -> WebElement:
        if not self._notification:
            self._notification = self.node.find_element(*NOTIFICATION)
        return self._notification

    @allure.step("Get notification text")
    def get_notification_text(self) -> str:
        if not self._notification_text:
            self._notification_text = self.node.find_element(*NOTIFICATION_TEXT).text
        return self._notification_text
