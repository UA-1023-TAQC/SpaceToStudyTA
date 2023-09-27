import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent
from SpaceToStudy.ui.pages.home_page.home_guest import HomePageGuest
from SpaceToStudy.ui.pages.header.header_component import HeaderComponent

NAME = (By.XPATH, "./a")


class NavigateComponent(BaseComponent):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self.name = None

    @allure.step("Click on a navigation link")
    def click(self):
        self.node.click()
        return self.node

    @allure.step("Get the text of a navigation link")
    def get_name(self) -> str:
        if not self.name:
            self.name = self.node.find_element(*NAME)
            return self.name.text

    @allure.step("Click 'What can you do' button in header")
    def click_what_can_u_do(self):
        self.node.click()
        return HomePageGuest(HomePageGuest(self.node).get_what_can_u_do_block())

    @allure.step("Click 'How it works' button in header")
    def click_how_it_works(self):
        self.node.click()
        return HomePageGuest(HomePageGuest(self.node).get_how_it_works_block())

    @allure.step("Click 'Who we are' button in header")
    def click_who_we_are(self):
        self.node.click()
        return HomePageGuest(HomePageGuest(self.node).get_who_we_are_block())