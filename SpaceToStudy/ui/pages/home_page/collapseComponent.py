from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from SpaceToStudy.ui.pages.base_page import BasePage

COLLAPSE_BLOCK = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[1]/div")


class CollapseComponent(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._collapse_block = None

    def get_collapse_block(self) -> WebElement:
        if not self._collapse_block:
            self._collapse_block = self.driver.find_element(*COLLAPSE_BLOCK)
        return self._collapse_block
