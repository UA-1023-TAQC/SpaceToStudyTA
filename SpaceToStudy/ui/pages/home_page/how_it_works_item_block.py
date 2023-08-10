from selenium.webdriver.common.by import By

from SpaceToStudy.ui.pages.base_page import BasePage
from SpaceToStudy.ui.pages.home_page.how_it_works_item_components import HowItWorksComponent

HOW_IT_WORKS_BLOCK = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[3]/div/div")
CHECKBOX = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[3]/div/div[1]/span/span[1]/input")

class HowItWorks(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._how_it_works_component = None

    def get_checkbox_how_it_works(self):
        return self.driver.find_element(CHECKBOX)

    def click_checkbox_how_it_works(self):
        self.get_checkbox_how_it_works().click()

    def get_categories(self) -> list[HowItWorksComponent]:
        if self._how_it_works_component is None:
            components = self.driver.find_elements(*HOW_IT_WORKS_BLOCK)
            self._how_it_works_component = []
            for component in components:
                self._how_it_works_component.append(HowItWorksComponent(component))

        return self._how_it_works_component




