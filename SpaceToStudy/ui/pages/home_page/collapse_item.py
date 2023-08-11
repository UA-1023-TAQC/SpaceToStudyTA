from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent

# COLLAPSE_BLOCK = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[1]/div")
# FLEXIBLE_LOCATION = (By.XPATH, "./div[1]")
# INDIVIDUAL_TIME = (By.XPATH, "./div[2]")
# FREE_CHOICE_OF_TUTOR = (By.XPATH, "./div[3]")
# DIGITAL_COMMUNICATION = (By.XPATH, "./div[4]")

TITLE_COLLAPSE_ITEM = (By.XPATH, "./div[1]/div/h6")
DESCRIPTION_COLLAPSE_ITEM = (By.XPATH, ".//p")


class CollapseItem(BaseComponent):

    def get_title(self) -> str:
        return self.node.find_element(*TITLE_COLLAPSE_ITEM).text

    def get_description(self) -> str:
        return self.node.find_element(*DESCRIPTION_COLLAPSE_ITEM).text

    def is_expanded(self) -> bool:
        aria_expanded = self.node.find_element(By.XPATH, ".//div[@aria-expanded]").get_attribute("aria-expanded")
        return aria_expanded == "true"

    def click(self):
        self.node.click()
