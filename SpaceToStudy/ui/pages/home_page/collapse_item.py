from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent

TITLE_COLLAPSE_ITEM = (By.XPATH, "./div[1]/div/h6")
DESCRIPTION_COLLAPSE_ITEM = (By.XPATH, ".//p")


class CollapseItem(BaseComponent):

    def __init__(self, node: WebElement):
        super().__init__(node)

    def get_title(self) -> WebElement:
        return self.node.find_element(*TITLE_COLLAPSE_ITEM)

    def get_title_text(self) -> str:
        return self.get_title().text

    def get_description(self) -> WebElement:
        return self.node.find_element(*DESCRIPTION_COLLAPSE_ITEM)

    def get_description_text(self) -> str:
        return self.get_description().text
    def get_color_of_title(self):
        return self.node.find_element(*TITLE_COLLAPSE_ITEM).value_of_css_property("color")


    def is_expanded(self) -> bool:
        aria_expanded = self.node.find_element(By.XPATH, ".//div[@aria-expanded]").get_attribute("aria-expanded")
        return aria_expanded == "true"

    def is_aria_hidden(self) -> bool:
        aria_hidden = self.node.find_element(By.XPATH, ".//div[@aria-hidden]").get_attribute("aria-hidden")
        return aria_hidden == "true"

    def click(self):
        self.node.click()
