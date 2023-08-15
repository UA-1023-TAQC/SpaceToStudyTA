from selenium.webdriver.common.by import By

#from SpaceToStudy.ui.pages.my_profile.profile_info import ProfileInfo
from SpaceToStudy.ui.pages.my_profile.profile_completeness import ProfileCompleteness
from SpaceToStudy.ui.pages.my_profile.student_reviews import StudentReviews
from SpaceToStudy.ui.pages.my_profile.video_presentation import VideoPresentation
from SpaceToStudy.ui.pages.base_page import BasePage

PROFILE_INFO = (By.XPATH, "/html/body/div/div/div[2]/div[2]")
PROFILE_COMPLETENESS = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[2]")
VIDEO_PRESENTATION = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[3]")
STUDENT_REVIEW = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[4]")

class MyProfile(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_profile_completeness(self):
        node = self.driver.find_element(*PROFILE_COMPLETENESS)
        self.profileCompleteness = ProfileCompleteness(node)
        return self.profileCompleteness

    def get_video_presentation(self):
        node = self.driver.find_element(*VIDEO_PRESENTATION)
        self.VideoPresentation = VideoPresentation(node)
        return self.VideoPresentation

    def get_student_review(self):
        node = self.driver.find_element(*STUDENT_REVIEW)
        self.StudentReviews = StudentReviews(node)
        return self.StudentReviews