import allure
from selenium.webdriver.common.by import By

from SpaceToStudy.ui.pages.base_component import BaseComponent

OK_BTN = (By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div/button')
CLOSE_BTN = (By.XPATH, '/html/body/div[2]/div[3]/div/div/button/svg')
VERIFICATION_MODAL_WINDOW = (By.XPATH, '/html/body/div[2]/div[3]/div/div/div')


class EmailVerificationModal(BaseComponent):

    def __init__(self, node):
        super().__init__(node)
        self._ok_btn = None
        self._close_button = None

    @allure.step("Getting the 'OK' button")
    def get_ok_btn(self):
        if not self._ok_btn:
            self._ok_btn = self.node.find_element(*OK_BTN)
        return self._ok_btn

    @allure.step("Clicking the 'OK' button")
    def click_ok_btn(self):
        from SpaceToStudy.ui.pages.home_page.home_guest import HomePageGuest
        self.get_ok_btn().click()
        return HomePageGuest(self.node)

    @allure.step("Getting the 'Close' button")
    def get_close_button(self):
        if not self._close_button:
            self._close_button = self.node.find_element(*CLOSE_BTN)
        return self._close_button

    @allure.step("Clicking the 'Close' button")
    def click_close_button(self):
        from SpaceToStudy.ui.pages.home_page.home_guest import HomePageGuest
        self.get_close_button().click()
        return HomePageGuest(self.node)

    @allure.step("Checking element visibility")
    def is_displayed(self) -> bool:
        return self.node.is_displayed()
