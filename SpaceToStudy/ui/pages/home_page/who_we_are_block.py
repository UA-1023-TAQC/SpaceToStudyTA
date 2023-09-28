import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent

TITLE = (By.XPATH, "./div[1]/p")
DESC = (By.XPATH, "./div[1]/span")
VIDEO = (By.XPATH, "./div[2]")


class WhoWeAreBlock(BaseComponent):
    def __init__(self, node):
        super().__init__(node)
        self._title = None
        self._desc = None
        self._video = None

    @allure.step("Get the title element of 'Who We Are' block")
    def get_title_element(self) -> WebElement:
        if not self._title:
            self._title = self.node.find_element(*TITLE)
        return self._title
    
    @allure.step("Get the title text of 'Who We Are' block")
    def get_title(self) -> str:
        return self.get_title_element().text
    
    @allure.step("Get the description element of 'Who We Are' block")
    def get_desc_element(self) -> WebElement:
        if not self._desc:
            self._desc = self.node.find_element(*DESC)
        return self._desc

    @allure.step("Get the description text of 'Who We Are' block")
    def get_desc(self) -> str:
        return self.get_desc_element().text

    @allure.step("Get the video element in 'Who We Are' block")
    def get_video(self) -> WebElement:
        if not self._video:
            self._video = self.node.find_element(*VIDEO)
        return self._video
    
    @allure.step("Get the list of web elements for 'Who We Are'' block")
    def get_who_we_are_elements(self) -> dict:
        return {"title": self.get_title_element(),
                "description": self.get_desc_element(),
                "video": self.get_video()}
