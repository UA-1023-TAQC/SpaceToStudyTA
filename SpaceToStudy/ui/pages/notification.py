import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.elements.base_element import BaseElement
from SpaceToStudy.ui.pages.base_component import BaseComponent

NOTIFICATION_ELEMENT = (By.XPATH, "/html/body/div/div[2]")
NOTIFICATION_TEXT = (By.XPATH, "/html/body/div/div[2]/div/div[2]")


class Notification(BaseComponent):

    def __init__(self, node: WebElement):
        super().__init__(node)
        self._notification = None
        self._notification_text = None

    @allure.step("Get notification")    
    def get_notification_element(self) -> WebElement:
        if not self._notification:
            self._notification = self.driver.find_element(*NOTIFICATION_ELEMENT)
        return self._notification
    
    @allure.step("Get notification text")
    def get_notification_text(self) -> str:
        if not self._notification_text:
            self._notification_text = self.node.find_element(*NOTIFICATION_TEXT).text
        return self._notification_text