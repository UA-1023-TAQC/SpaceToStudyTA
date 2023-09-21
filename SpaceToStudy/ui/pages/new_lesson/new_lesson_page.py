import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_page import BasePage

TITLE = (By.XPATH, "//form//div[contains(@style, 'font-size: 35px')]/input")
DESCRIPTION = (By.XPATH, "//form//div[contains(@style, 'font-size: 16px')]/input")

BUILT_IN_APPLICATION = (By.XPATH, '//div[@role="application"]')
SAVE_BTN = (By.XPATH, '//button[text()="Save"]')
CANCEL_BTN = (By.XPATH, '//button[text()="Cancel"]')


class NewLessonPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Get the title WebElement of lesson on NewLessonPage")
    def get_title_element(self) -> WebElement:
        return self.driver.find_element(*TITLE)

    @allure.step("Get the title text of lesson on NewLessonPage")
    def get_title_text(self) -> str:
        return self.driver.find_element(*TITLE).text

    @allure.step("Click the title WebElement of lesson on NewLessonPage")
    def click_title(self):
        self.get_title_element().click()

    @allure.step("Set the title '{title}' of lesson on NewLessonPage")
    def set_title(self, title: str):
        self.get_title_element().send_keys(title)

    @allure.step("Get the description WebElement of lesson on NewLessonPage")
    def get_description_element(self) -> WebElement:
        return self.driver.find_element(*DESCRIPTION)

    @allure.step("Get the description text of lesson on NewLessonPage")
    def get_description_text(self) -> str:
        return self.driver.find_element(*DESCRIPTION).text

    @allure.step("Click the description WebElement of lesson on NewLessonPage")
    def click_description(self):
        self.get_description_element().click()

    @allure.step("Set the description '{description}' of lesson on NewLessonPage")
    def set_description(self, description: str):
        self.get_description_element().send_keys(description)

    @allure.step("Get the built-in application WebElement on NewLessonPage")
    def get_built_in_application(self) -> WebElement:
        return self.driver.find_element(*BUILT_IN_APPLICATION)

    @allure.step("Get 'Save' button WebElement on NewLessonPage")
    def get_save_btn(self) -> WebElement:
        return self.driver.find_element(*SAVE_BTN)

    @allure.step("Get 'Save' button text on NewLessonPage")
    def get_save_btn_text(self) -> str:
        return self.driver.find_element(*SAVE_BTN).text

    @allure.step("Click 'Save' button on NewLessonPage")
    def click_save_btn(self):
        self.get_save_btn().click()

    @allure.step("Get 'Cancel' button WebElement on NewLessonPage")
    def get_cancel_btn(self) -> WebElement:
        return self.driver.find_element(*CANCEL_BTN)

    @allure.step("Get 'Cancel' button text on NewLessonPage")
    def get_cancel_btn_text(self) -> str:
        return self.driver.find_element(*CANCEL_BTN).text

    @allure.step("Click 'Cancel' button on NewLessonPage")
    def click_cancel_btn(self):
        self.get_cancel_btn().click()
