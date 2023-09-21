import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent
from SpaceToStudy.ui.pages.my_profile.my_profile_page import MyProfile

MY_OFFERS = (By.XPATH, "./ul/a[3]")
MY_PROFILE = (By.XPATH, "./ul/a[1]")
MY_COOPERATION = (By.XPATH, "./ul/a[2]")
LOG_OUT = (By.XPATH, "./ul/a[4]")

MY_PROFILE_PAGE = (By.XPATH, "/html/body/div/div/div[2]/div[2]")


class MenuItems(BaseComponent):

    def __init__(self, node):
        super().__init__(node)
        self._my_offers = None
        self._my_profile = None
        self._my_cooperation = None
        self._log_out = None

    @allure.step("Get 'My offers' menu item")
    def menu_items_my_offers(self) -> WebElement:
        if not self._my_offers:
            self._my_offers = self.node.find_element(*MY_OFFERS)
        return self._my_offers

    @allure.step("Click 'My offers' menu item")
    def click_menu_items_my_offers(self):
        self.menu_items_my_offers().click()

    @allure.step("Get 'My profile' menu item")
    def menu_items_my_profile(self) -> WebElement:
        if not self._my_profile:
            self._my_profile = self.node.find_element(*MY_PROFILE)
        return self._my_profile

    @allure.step("Click 'My profile' menu item")
    def click_menu_items_my_profile(self):
        self.menu_items_my_profile().click()
        return MyProfile(self.node.parent)

    @allure.step("Get 'My cooperations' menu item")
    def menu_items_my_cooperation(self) -> WebElement:
        if not self._my_cooperation:
            self._my_cooperation = self.node.find_element(*MY_COOPERATION)
        return self._my_cooperation

    @allure.step("Click 'My cooperations' menu item")
    def click_menu_items_my_cooperation(self):
        self.menu_items_my_cooperation().click()

    @allure.step("Get 'Log out' menu item")
    def menu_items_log_out(self) -> WebElement:
        if not self._log_out:
            self._log_out = self.node.find_element(*LOG_OUT)
        return self._log_out

    @allure.step("Click 'Log out' menu item")
    def click_menu_items_log_out(self):
        self.menu_items_log_out().click()
