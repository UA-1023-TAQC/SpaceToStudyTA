from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.header.header_component import HeaderComponent

LOGIN_BTN = (By.XPATH, "/html/body/div/div/header/div/div/button[3]")


class HeaderUnauthorizedComponent(HeaderComponent):

    def __init__(self, node: WebElement):
        super().__init__(node)

    def get_login_btn(self) -> WebElement:
        return self.node.find_element(*LOGIN_BTN)

    def click_login_btn(self):
        self.get_login_btn().click()
