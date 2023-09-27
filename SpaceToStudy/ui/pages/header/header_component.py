from selenium.webdriver import Keys
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent

LIST_ITEMS = (By.XPATH, '/html/body/div[1]/div/header/div/ul')
LOGO = (By.XPATH, "/html/body/div[1]/div/header/div/a")
NAVIGATE_ELEMENTS = (By.XPATH, "/html/body/div[1]/div/header/div/ul/li")


class HeaderComponent(BaseComponent):

    def __init__(self, node):
        super().__init__(node)
        self._navigate_elements = []

    @allure.step("Get logo on the header")
    def get_logo(self) -> WebElement:
        return self.node.find_element(*LOGO)

    @allure.step("Click logo on the header")
    def click_logo(self):
        self.get_logo().click()

    @allure.step("Get navigate links on the header")
    def get_navigate_links(self) -> list: #the name should be changed for "get_navigate_elements"
        from SpaceToStudy.ui.pages.header.navigate_component import NavigateComponent
        if not self._navigate_elements:
            navigate_links = self.node.find_elements(*NAVIGATE_ELEMENTS)
            for element in navigate_links:
                self._navigate_elements.append(NavigateComponent(element))
        return self._navigate_elements
    
    # @allure.step("Get navigate links on the header")
    # def get_navigate_links(self) -> dict:
    #     self._navigate_elements = {} #needs to be changed in init
    #     from SpaceToStudy.ui.pages.header.navigate_component import NavigateComponent
    #     if not self._navigate_elements:
    #         navigate_links = self.node.find_elements(*NAVIGATE_ELEMENTS)
    #         navigate_el_names = ["what_can_u_do",
    #                              "How_it_works",
    #                              "Who we are"]
    #         self._navigate_elements = {key: NavigateComponent(value) for key in navigate_el_names for value in navigate_links }
    #     return self._navigate_elements

    def tab_key(self, count_of_tabs: int):
        self.get_logo().send_keys(Keys.TAB * count_of_tabs)
        return