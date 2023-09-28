import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent

BACK_BUTTON = (By.XPATH, "//button[contains(text(), 'Back')]")
NEXT_BUTTON = (By.XPATH, "//button[contains(text(), 'Next')]")
FINISH_BUTTON = (By.XPATH, "//button[contains(text(), 'Finish')]")


class FirstLoginFooter(BaseComponent):
    def get_back_button(self) -> WebElement:
        return self.node.find_element(*BACK_BUTTON)

    @allure.step("Click back button")
    def click_back_button(self):
        self.get_back_button().click()
        return self.node.parent

    def get_next_button(self) -> WebElement:
        return self.node.find_element(*NEXT_BUTTON)

    @allure.step("Click next button")
    def click_next_button(self):
        self.get_next_button().click()
        return self.node.parent

    def get_finish_button(self) -> WebElement:
        return self.node.find_element(*FINISH_BUTTON)

    @allure.step("Click finish button")
    def click_finish_button(self):
        self.get_finish_button().click()
        return self.node.parent
