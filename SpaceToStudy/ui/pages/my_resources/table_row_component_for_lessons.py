import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent

LESSON_ICON = (By.XPATH, './td[1]/div/svg/path')
LESSON_TITLE = (By.XPATH, './td[1]/div/p')
ATTACHMENTS_INFORMATION = (By.XPATH, './td[2]/p')
LAST_UPDATES = (By.XPATH, './td[3]/p')
ACTIONS_BTN = (By.XPATH, './td[4]/button')
EDIT_BTN = (By.XPATH, '/html/body/div[2]/div[3]/ul/li[1]')
DELETE_BTN = (By.XPATH, '/html/body/div[2]/div[3]/ul/li[2]')


class TableRowForLessonsComponent(BaseComponent):
    def __init__(self, node):
        super().__init__(node)

    @allure.step("Get lesson icon")
    def get_lesson_icon(self) -> WebElement:
        return self.node.find_element(*LESSON_ICON)

    @allure.step("Get lesson title")
    def get_lesson_title(self) -> str:
        return self.node.find_element(*LESSON_TITLE).text

    @allure.step("Get attachments information")
    def get_attachments_information(self) -> str:
        return self.node.find_element(*ATTACHMENTS_INFORMATION).text

    @allure.step("Get last updates")
    def get_last_updates(self) -> str:
        return self.node.find_element(*LAST_UPDATES).text

    @allure.step("Get actions button")
    def get_actions_btn(self) -> WebElement:
        return self.node.find_element(*ACTIONS_BTN)

    @allure.step("Click actions button")
    def click_actions_btn(self):
        self.get_actions_btn().click()

    @allure.step("Get edit button")
    def get_edit_btn(self) -> WebElement:
        return self.node.find_element(*EDIT_BTN)

    @allure.step("Click edit button")
    def click_edit_btn(self):
        self.get_edit_btn().click()

    @allure.step("Get delete button")
    def get_delete_btn(self) -> WebElement:
        return self.node.find_element(*DELETE_BTN)

    @allure.step("Click delete button")
    def click_delete_btn(self):
        self.get_delete_btn().click()
