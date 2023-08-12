from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_page import BasePage
from SpaceToStudy.ui.pages.header.navigate_component import NavigateComponent

LIST_ITEMS = (By.XPATH, '/html/body/div[1]/div/header/div/ul')
LOGO = (By.XPATH, "/html/body/div[1]/div/header/div/a")
NAVIGATE_ELEMENTS = (By.XPATH, "/html/body/div[1]/div/header/div/ul/li")


class Header(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._navigate_elements = None

    def get_logo(self) -> WebElement:
        return self.driver.find_element(*LOGO)

    def click_logo(self):
        self.get_logo().click()

    def get_navigate_links(self) -> tuple[NavigateComponent]:
        if self._navigate_elements is None:
            navigate_links = self.driver.find_elements(*NAVIGATE_ELEMENTS)
            self._navigate_elements = []
            for element in navigate_links:
                self._navigate_elements.append(NavigateComponent(element))
        return self._navigate_elements
