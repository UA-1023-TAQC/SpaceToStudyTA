import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent
from SpaceToStudy.ui.pages.home_page.home_guest import HomePageGuest

NAME = (By.XPATH, "./a")


class NavigateComponent(BaseComponent):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self.name = None

    @allure.step("Click on a navigation link")
    def click(self):
        self.node.click()
        return self.node
        return HomePageGuest(self.node.parent)

    @allure.step("Get the text of a navigation link")
    def get_name(self) -> str:
        if not self.name:
            self.name = self.node.find_element(*NAME)
            return self.name.text
