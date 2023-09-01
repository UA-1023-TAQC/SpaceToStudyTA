from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent

MY_OFFERS = (By.XPATH, "./ul/a[3]")

class MenuItems(BaseComponent):

    def __init__(self, node):
        super().__init__(node)
        self._my_offers = None

    def menu_items_my_offers(self) -> WebElement:
        if not self._my_offers:
            self._my_offers = self.node.find_element(*MY_OFFERS)
        return self._my_offers

    def click_menu_items_my_offers(self):
        self.menu_items_my_offers().click()

