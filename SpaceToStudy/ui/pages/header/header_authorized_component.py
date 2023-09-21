import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.header.header_component import HeaderComponent
from SpaceToStudy.ui.pages.header.user_menu_component import UserMenuComponent

USER_MENU = (By.XPATH, "/html/body/div[1]/div/header/div/div")


class HeaderAuthorizedComponent(HeaderComponent):

    def __init__(self, node: WebElement):
        super().__init__(node)
        self._user_menu = None

    @allure.step("Get elements user menu")
    def get_user_menu(self):
        node = self.node.find_element(*USER_MENU)
        if not self._user_menu:
            self._user_menu = UserMenuComponent(node)
            return self._user_menu

