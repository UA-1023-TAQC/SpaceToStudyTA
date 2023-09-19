from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.header.header_component import HeaderComponent
from SpaceToStudy.ui.pages.login_modal.login_modal import LoginModal

LOGIN_BTN = (By.XPATH, "/html/body/div/div/header/div/div/button[3]")
LOGIN_MODAL = (By.XPATH, "/html/body/div[2]/div[3]")


class HeaderUnauthorizedComponent(HeaderComponent):

    def __init__(self, node: WebElement):
        super().__init__(node)

    def get_login_btn(self) -> WebElement:
        return self.node.find_element(*LOGIN_BTN)

    def click_login_btn(self) -> LoginModal:
        self.get_login_btn().click()
        return LoginModal(self.node)

    def is_login_button_present(self) -> bool:
        try:
            self.get_login_btn()
            return True
        except NoSuchElementException:
            return False

    def get_login_modal(self) -> WebElement:
        return self.node.find_element(By.XPATH, *LOGIN_MODAL)
