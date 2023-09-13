from selenium.webdriver.common.by import By

from SpaceToStudy.ui.pages.base_component import BaseComponent
from SpaceToStudy.ui.pages.subjects.subjects_page import SubjectsPage

TITLE = (By.XPATH, "./div/p")
OFFERS = (By.XPATH, "./div/span")

class CardComponent(BaseComponent):

    def __init__(self, node):
        super().__init__(node)
        self._title = None
        self._offers = None

    def get_title(self) -> str:
        if not self._title:
            self._title = self.node.find_element(*TITLE)
        return self._title.text

    def get_offers(self) -> str:
        if not self._offers:
            self._offers = self.node.find_element(*OFFERS)
        return self._offers.text

    def click_card(self):
        self.node.click()
        return SubjectsPage(self.node.parent)