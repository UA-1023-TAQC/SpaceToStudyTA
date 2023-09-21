import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.elements.input import Input

ICON = (By.XPATH, "./following-sibling::div/div/button/svg")


class InputWithImage(Input):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self.icon = None

    @allure.step("Get icon element")
    def get_icon(self):
        if not self.icon:
            self.icon = self.node.find_element(*ICON)
        return self.icon

    @allure.step("Click icon element")
    def click_icon(self):
        self.get_icon().click()
