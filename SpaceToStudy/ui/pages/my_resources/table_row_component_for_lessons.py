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

    def get_lesson_icon(self) -> WebElement:
        return self.node.find_element(*LESSON_ICON)

    def get_lesson_title(self) -> str:
        return self.node.find_element(*LESSON_TITLE).text

    def get_attachments_information(self) -> str:
        return self.node.find_element(*ATTACHMENTS_INFORMATION).text

    def get_last_updates(self) -> str:
        return self.node.find_element(*LAST_UPDATES).text

    def get_actions_btn(self) -> WebElement:
        return self.node.find_element(*ACTIONS_BTN)

    def click_actions_btn(self):
        self.get_actions_btn().click()

    def get_edit_btn(self) -> WebElement:
        return self.node.find_element(*EDIT_BTN)

    def click_edit_btn(self):
        self.get_edit_btn().click()

    def get_delete_btn(self) -> WebElement:
        return self.node.find_element(*DELETE_BTN)

    def click_delete_btn(self):
        self.get_delete_btn().click()
