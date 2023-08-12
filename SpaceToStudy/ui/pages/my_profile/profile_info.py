import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.elements.my_profile_elements.profile_description import ProfileDescription
from SpaceToStudy.ui.pages.base_page import BasePage

AVATAR = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[1]/div[1]/div/*[local-name()='svg']")
EDIT_PROFILE_BUTTON = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[1]/a")

PROFILE_INFO_DESCRIPTION = (By.XPATH,  "/html/body/div/div/div[2]/div[2]/div[1]/div[2]")



class ProfileInfo(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_avatar(self) -> WebElement:
        return self.driver.find_element(*AVATAR)

    def click_edit_profile_button(self):
        edit_profile_button = self.driver.find_element(*EDIT_PROFILE_BUTTON)
        edit_profile_button.click()
        time.sleep(1)

    def get_edit_profile_button(self) -> WebElement:
        return self.driver.find_element(*EDIT_PROFILE_BUTTON)

    def get_profile_description(self):
        node = self.driver.find_element(*PROFILE_INFO_DESCRIPTION)
        self.profileDescription = ProfileDescription(node)
        return self.profileDescription

