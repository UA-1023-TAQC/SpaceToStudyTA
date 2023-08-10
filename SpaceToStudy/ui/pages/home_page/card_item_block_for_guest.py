from selenium.webdriver.common.by import By

from SpaceToStudy.ui.pages.base_page import BasePage
from SpaceToStudy.ui.pages.home_page.card_component_for_guest import CardComponent

CARD_COMPONENT_BLOCK = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[2]/div[2]/div")


class CardItemBlock(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._card_component = None

    def get_categories(self) -> list[CardComponent]:
        if self._card_component is None:
            components = self.driver.find_elements(*CARD_COMPONENT_BLOCK)
            self._card_component = []
            for component in components:
                self._card_component.append(CardComponent(component))
        return self._card_component

