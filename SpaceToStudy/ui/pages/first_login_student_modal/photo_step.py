import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.first_login_student_modal.first_login_modal import FirstLoginModal
from SpaceToStudy.ui.pages.home_page.home_student import HomePageStudent

STARTING_TEXT = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/div[2]/div[1]/p[1]")
UPLOAD_BUTTON = (By.XPATH, "//label[contains(text(), 'Upload')]")
MAXIMUM_FILE_SIZE = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/div[2]/div[1]/p[2]")
FINISH_BUTTON = (By.XPATH, "//button[contains(text(), 'Finish')]")

class PhotoStepStudent(FirstLoginModal):
    @allure.step("Get image")
    def get_starting_text(self) -> str:
        return self.node.find_element(*STARTING_TEXT).text

    @allure.step("Get upload button")
    def get_upload_button(self) -> WebElement:
        return self.node.find_element(*UPLOAD_BUTTON)

    @allure.step("Click upload button")
    def click_upload_button(self):
        self.get_upload_button().click()
        return self

    @allure.step("Get maximum file size text")
    def get_maximum_file_size(self) -> str:
        return self.node.find_element(*MAXIMUM_FILE_SIZE).text
    
    @allure.step("Click back button")
    def click_back_button(self):
        from SpaceToStudy.ui.pages.first_login_student_modal.language_step import LanguageStepStudent
        self.get_back_button().click()
        return LanguageStepStudent(self.node)

    @allure.step("Get finish button")
    def get_finish_button(self) -> WebElement:
        return self.node.find_element(*FINISH_BUTTON)
    
    @allure.step("Click finish button")
    def click_finish_button(self):
        self.get_finish_button().click()
        return HomePageStudent(self.node)
