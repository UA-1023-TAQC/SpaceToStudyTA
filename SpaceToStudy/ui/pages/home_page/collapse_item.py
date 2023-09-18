from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent

TITLE_COLLAPSE_ITEM = (By.XPATH, "./div[1]/div/h6")
DESCRIPTION_COLLAPSE_ITEM = (By.XPATH, ".//p")
TAB_ELEMENT = (By.XPATH, "./div[1]")


class CollapseItem(BaseComponent):

    def __init__(self, node: WebElement):
        super().__init__(node)

    def get_title(self) -> str:
        return self.node.find_element(*TITLE_COLLAPSE_ITEM).text

    def get_description(self) -> str:
        return self.node.find_element(*DESCRIPTION_COLLAPSE_ITEM).text

    def is_expanded(self) -> bool:
        aria_expanded = self.node.find_element(By.XPATH, ".//div[@aria-expanded]").get_attribute("aria-expanded")
        return aria_expanded == "true"

    def click(self):
        self.node.click()

    def get_el_tab(self) -> WebElement:
        return self.node.find_element(*TAB_ELEMENT)
