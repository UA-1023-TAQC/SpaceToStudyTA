import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.elements.base_element import BaseElement

LINK = (By.XPATH, ". ")


class Link(BaseElement):

    def __init__(self, node: WebElement):
        super().__init__(node)

    @allure.step("Get text link element")
    def get_link_text(self) -> str:
        return self.node.find_element(*LINK).text

    @allure.step("Click link element")
    def click_link(self):
        self.node.find_element(*LINK).click()

    @allure.step("Get link element href")
    def get_link_href(self) -> str:
        return self.node.find_element(*LINK).get_attribute("href")
