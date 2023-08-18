from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_page import BasePage
from SpaceToStudy.ui.pages.my_offers.actions_btn_grid import ActionsBtnGrid
from SpaceToStudy.ui.pages.my_offers.dropdown_menu import DropdownMenu
from SpaceToStudy.ui.pages.my_offers.offers_interaction import OffersInteraction
from SpaceToStudy.ui.pages.my_offers.offers_table import OfferElements
from SpaceToStudy.ui.pages.my_offers.select_offer_btns import SelectOffers

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
        self._title = None
        self._create_new_offer_btn = None
        self._dropdown_menu = None
        self._actions_btn_inline = None
        self._edit_btn_inline = None
        self._view_details_btn_inline = None

    def get_offers_table(self):
        if not self._offers_table:
            node = self.driver.find_element(*OFFERS_TABLE)
            self._offers_table = OfferElements(node)
        return self._offers_table

    def get_title(self) -> WebElement:
        if not self._title:
            self._title = self.driver.find_element(*MY_OFFERS_PAGE_TITLE)
        return self._title

    def get_create_new_offer_btn(self) -> WebElement:
        if not self._create_new_offer_btn:
            self._create_new_offer_btn = self.driver.find_element(*CREATE_NEW_OFFER_BTN)
        return self._create_new_offer_btn

    def click_create_new_offer_btn(self):
        self.driver.get_create_new_offer_btn.click()

    def get_select_offer_btns(self):
        if not self._select_offer_btns:
            node = self.driver.find_element(*SELECT_OFFER_BTNS)
            self._select_offer_btns = SelectOffers(node)
        return self._select_offer_btns

    def get_offers_interaction(self):
        if not self._offers_interaction:
            node = self.driver.find_element(*OFFERS_INTERACTION)
            self._offers_interaction = OffersInteraction(node)
        return self._offers_interaction

    def get_list_box_dropdown_menu(self):
        if not self._list_box_dropdown_menu:
            node = self.driver.find_element(*LIST_BOX_DROPDOWN_MENU)
            self._list_box_dropdown_menu = DropdownMenu(node)
        return self._list_box_dropdown_menu

    def get_dropdown_menu(self) -> WebElement:
        if not self._dropdown_menu:
            self._dropdown_menu = self.driver.find_element(*DROPDOWN_MENU)
        return self._dropdown_menu

    def click_dropdown_menu(self):
        return self.get_dropdown_menu().click()

    def get_actions_btn_inline(self) -> WebElement:
        if not self._actions_btn_inline:
            self._actions_btn_inline = self.driver.find_element(*ACTIONS_BTN_INLINE)
        return self._actions_btn_inline

    def click_actions_btn_inline(self):
        self.get_actions_btn_inline().click()

    def get_edit_btn_inline(self) -> WebElement:
        if not self._edit_btn_inline:
            self._edit_btn_inline = self.driver.find_element(*EDIT_BTN_INLINE)
        return self._edit_btn_inline

    def get_view_details_btn_inline(self) -> WebElement:
        if not self._view_details_btn_inline:
            self._view_details_btn_inline = self.driver.find_element(*VIEW_DETAILS_BTN_INLINE)
        return self._view_details_btn_inline

    def click_edit_btn_inline(self):
        self.get_edit_btn_inline().click()

    def click_view_details_btn_inline(self):
        self.get_view_details_btn_inline().click()

    def get_actions_btn_grid(self):
        if not self._actions_btn_grid:
            node = self.driver.find_element(*ACTIONS_BTN_GRID)
            self._actions_btn_grid = ActionsBtnGrid(node)
        return self._actions_btn_grid
