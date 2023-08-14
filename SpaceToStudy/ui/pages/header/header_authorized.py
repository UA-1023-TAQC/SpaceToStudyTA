from selenium.webdriver.common.by import By


from SpaceToStudy.ui.elements.header.user_menu import UserMenu
from SpaceToStudy.ui.pages.header.header import Header

USER_MENU = (By.XPATH, "/html/body/div[1]/div/header/div/div")


class HeaderTutor(Header):

    def __init__(self, driver):
        super().__init__(driver)
        self._user_menu = None

    def get_user_menu(self):
        node = self.driver.find_element(*USER_MENU)
        self._user_menu = UserMenu(node)
        return self._user_menu
