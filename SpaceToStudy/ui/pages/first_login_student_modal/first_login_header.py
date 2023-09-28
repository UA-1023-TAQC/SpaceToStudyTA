import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent

GENERAL_PAGE = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[1]/div[1]")
INTERESTS_PAGE = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[1]/div[2]")
LANGUAGE_PAGE = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[1]/div[3]")
PHOTO_PAGE = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[1]/div[4]")


class FirstLoginHeader(BaseComponent):
    def get_general_page(self) -> WebElement:
        return self.node.find_element(*GENERAL_PAGE)

    @allure.step("Click general page")
    def click_general_page(self):
        self.get_general_page().click()
        from SpaceToStudy.ui.pages.first_login_student_modal.general_page import GeneralPageStudent
        return GeneralPageStudent(self.node.parent)

    def get_interests_page(self) -> WebElement:
        return self.node.find_element(*INTERESTS_PAGE)

    @allure.step("Click interests page")
    def click_interests_page(self):
        self.get_interests_page().click()
        from SpaceToStudy.ui.pages.first_login_student_modal.interests_page import InterestsPageStudent
        return InterestsPageStudent(self.node.parent)

    def get_language_page(self) -> WebElement:
        return self.node.find_element(*LANGUAGE_PAGE)

    @allure.step("Click language page")
    def click_language_page(self):
        self.get_language_page().click()
        from SpaceToStudy.ui.pages.first_login_student_modal.language_page import LanguagePageStudent
        return LanguagePageStudent(self.node.parent)

    def get_photo_page(self) -> WebElement:
        return self.node.find_element(*PHOTO_PAGE)

    @allure.step("Click photo page")
    def click_photo_page(self):
        self.get_photo_page().click()
        from SpaceToStudy.ui.pages.first_login_student_modal.photo_page import PhotoPageStudent
        return PhotoPageStudent(self.node.parent)
