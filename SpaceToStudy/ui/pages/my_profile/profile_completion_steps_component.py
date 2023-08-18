from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent

TITLE = (By.XPATH, ".//h6")
DESCRIPTION = (By.XPATH, ".//p")
ICON = (By.XPATH, ".//*[local-name()='svg']")


class ProfileCompletionStepsComponent(BaseComponent):
    def __init__(self, node):
        super().__init__(node)
        self.node = node

    def get_profile_completion_step_title(self) -> str:
        return self.node.find_element(*TITLE).text

    def get_profile_completion_step_icon(self) -> WebElement:
        return self.node.find_element(*ICON)

    def get_profile_completion_step_description(self) -> str:
        return self.node.find_element(*DESCRIPTION).text
