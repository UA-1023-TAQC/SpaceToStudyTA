import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent

TEXT_DIV = (By.XPATH, "./div[1]")
TITLE = (By.XPATH, "./div[1]/p")
DESC = (By.XPATH, "./div[1]/span")
VIDEO = (By.CSS_SELECTOR, "#who-we-are > div.MuiBox-root > div > img")


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

    @allure.step("Get the video element display in 'Who We Are' block")
    def get_video_display(self) -> str:
        return self.get_video().value_of_css_property("display")

    @allure.step("Get the text aligning in 'Wo We Are' block")
    def get_text_aligning(self) -> str:
        return self.node.find_element(*TEXT_DIV).value_of_css_property("text-align")
