from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.elements.input import Input

SHOW_PASSWORD_ICON = (By.XPATH, "./button/svg")


class InputWithImage(Input):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self.show_password_icon = None

    def get_show_password_icon(self):
        if not self.show_password_icon:
            self.show_password_icon = self.node.find_element(*SHOW_PASSWORD_ICON)
        return self.show_password_icon

    def click_show_password_icon(self):
        self.show_password_icon().click()

