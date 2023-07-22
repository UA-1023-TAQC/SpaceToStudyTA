from selenium.webdriver.common.by import By

from SpaceToStudy.ui.elements.my_offers.actions_btn_grid import ActionsBtnGrid
from SpaceToStudy.ui.elements.my_offers.dropdown_menu import DropdownMenu
from SpaceToStudy.ui.elements.my_offers.offers_interaction import OffersInteraction
from SpaceToStudy.ui.elements.my_offers.offers_table import OfferElements
from SpaceToStudy.ui.elements.my_offers.select_offer_btns import SelectOffers
from SpaceToStudy.ui.pages.base_page import BasePage

OFFERS_TABLE = (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[4]/div/div/table/tbody/tr[2]')
MY_OFFERS_PAGE_TITLE = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/p")
CREATE_NEW_OFFER_BTN = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/button")
SELECT_OFFER_BTNS = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[2]")
OFFERS_INTERACTION = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[3]")
LIST_BOX_DROPDOWN_MENU = (By.XPATH, "/html/body/div[2]/div[3]/ul")
DROPDOWN_MENU = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div")
ACTIONS_BTN_INLINE = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[4]/div/div/table/tbody/tr[2]/td[6]/button")
EDIT_BTN_INLINE = (By.XPATH, "/html/body/div[2]/div[3]/ul/li[1]")
VIEW_DETAILS_BTN_INLINE = (By.XPATH, "/html/body/div[2]/div[3]/ul/li[2]")
ACTIONS_BTN_GRID = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[4]/div[2]/div/div[4]")


class MyOffersPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._offers_table = None
        self._select_offer_btns = None
        self._offers_interaction = None
        self._list_box_dropdown_menu = None
        self._actions_btn_grid = None

    def get_offers_table(self):
        node = self.driver.find_element(*OFFERS_TABLE)
        self._offers_table = OfferElements(node)
        return self._offers_table

    def get_title(self):
        return self.driver.find_element(*MY_OFFERS_PAGE_TITLE)

    def get_create_new_offer_btn(self):
        return self.driver.find_element(*CREATE_NEW_OFFER_BTN)

    def click_create_new_offer_btn(self):
        self.driver.get_create_new_offer_btn.click()

    def get_select_offer_btns(self):
        node = self.driver.find_element(*SELECT_OFFER_BTNS)
        self._select_offer_btns = SelectOffers(node)
        return self._select_offer_btns

    def get_offers_interaction(self):
        node = self.driver.find_element(*OFFERS_INTERACTION)
        self._offers_interaction = OffersInteraction(node)
        return self._offers_interaction

    def get_list_box_dropdown_menu(self):
        node = self.driver.find_element(*LIST_BOX_DROPDOWN_MENU)
        self._list_box_dropdown_menu = DropdownMenu(node)
        return self._list_box_dropdown_menu

    def get_dropdown_menu(self):
        return self.driver.find_element(*DROPDOWN_MENU)

    def click_dropdown_menu(self):
        return self.get_dropdown_menu().click()

    def get_actions_btn_inline(self):
        return self.driver.find_element(*ACTIONS_BTN_INLINE)

    def click_actions_btn_inline(self):
        self.get_actions_btn_inline().click()

    def get_edit_btn_inline(self):
        return self.driver.find_element(*EDIT_BTN_INLINE)

    def get_view_details_btn_inline(self):
        return self.driver.find_element(*VIEW_DETAILS_BTN_INLINE)

    def click_edit_btn_inline(self):
        self.get_edit_btn_inline().click()

    def click_view_details_btn_inline(self):
        self.get_view_details_btn_inline().click()

    def get_actions_btn_grid(self):
        node = self.driver.find_element(*ACTIONS_BTN_GRID)
        self._actions_btn_grid = ActionsBtnGrid(node)
        return self._actions_btn_grid
