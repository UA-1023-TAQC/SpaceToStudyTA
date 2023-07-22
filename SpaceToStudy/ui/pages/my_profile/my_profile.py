import time

from selenium.webdriver.common.by import By

from SpaceToStudy.ui.elements.profile_info import ProfileInfo
from SpaceToStudy.ui.pages.base_page import BasePage


PROFILE_INFO = (By.XPATH, "/html/body/div/div/div[2]/div[2]")

class MyProfile(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.profile_info = None

    def get_profile_img(self):
        pass

    def get_menu_button(self):
        """
        bug:
        when press "Main" button "/html/body/div/div/div[2]/div[1]/nav/ol/li[1]/a"
        redirects to Main page is ok, but when you click undo "<-" its redirect to same page (Main)
        """
        pass


    def get_profile_info(self):
        noda = self.driver.find_element(*PROFILE_INFO)
        self.profile_info = ProfileInfo(noda)
        return self.profile_info