from selenium.webdriver.common.by import By

from SpaceToStudy.ui.elements.my_profile_elements.profile_info import ProfileInfo
from SpaceToStudy.ui.elements.my_profile_elements.profile_completeness import ProfileCompleteness
from SpaceToStudy.ui.elements.my_profile_elements.video_presentation import VideoPresentation
from SpaceToStudy.ui.pages.base_page import BasePage

PROFILE_INFO = (By.XPATH, "/html/body/div/div/div[2]/div[2]")
PROFILE_COMPLETENESS = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[2]")
VIDEO_PRESENTATION = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[3]")

class MyProfile(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.profile_info = None

    def menu_button_bug(self):
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

    def get_profile_completeness(self):
        noda = self.driver.find_element(*PROFILE_COMPLETENESS)
        self.profileCompleteness = ProfileCompleteness(noda)
        return self.profileCompleteness

    def get_video_presentation(self):
        noda = self.driver.find_element(*VIDEO_PRESENTATION)
        self.VideoPresentation = VideoPresentation(noda)
        return self.VideoPresentation

