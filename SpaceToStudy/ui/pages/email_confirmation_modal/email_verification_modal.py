from selenium.webdriver.common.by import By

from SpaceToStudy.ui.pages.base_page import BasePage
from SpaceToStudy.ui.pages.home_page.home_guest import HomePageGuest

OK_BTN = (By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div/button')
CLOSE_BTN = (By.XPATH, '/html/body/div[2]/div[3]/div/div/button/svg')


class EmailVerificationModal(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._ok_btn = None
        self._close_button = None

    def get_ok_btn(self):
        if not self._ok_btn:
            _ok_btn = self.driver.find_element(*OK_BTN)
            self._ok_btn = HomePageGuest(_ok_btn)
        return self._ok_btn

    def get_close_button(self):
        if not self._close_button:
            _close_button = self.driver.find_element(*CLOSE_BTN)
            self._close_button = HomePageGuest(_close_button)
        return self._close_button
