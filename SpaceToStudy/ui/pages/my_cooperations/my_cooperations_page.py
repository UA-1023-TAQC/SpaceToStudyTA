from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_page import BasePage

NAVIGATION_BAR = (By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/nav')
MAIN_NAVIGATION_LINK = (By.XPATH, '//a[text()="Main"]')
CURRENT_PAGE_NAME = (By.XPATH, '//p[@to="my-cooperations"]')
MY_COOPERATIONS_PAGE_TITLE = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/p')
VIEW_MY_OFFERS_BTN = (By.XPATH, '//a[contains(text(), "View my offers")]')

TABLE_FILTER_BAR = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]')
ALL_TABLE_FILTER = (By.XPATH, f'{TABLE_FILTER_BAR}/button[1]')
ACTIVE_TABLE_FILTER = (By.XPATH, f'{TABLE_FILTER_BAR}/button[2]')
PENDING_TABLE_FILTER = (By.XPATH, f'{TABLE_FILTER_BAR}/button[3]')
CLOSED_TABLE_FILTER = (By.XPATH, f'{TABLE_FILTER_BAR}/button[4]')

FILTER_TEXT_FIELD = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[3]/div[1]/div/input')
ROW_VIEW_TOGGLE_BUTTON = (By.XPATH, '//button[@aria-label="inline card view"]')
CARD_VIEW_TOGGLE_BUTTON = (By.XPATH, '//button[@aria-label="grid card view"]')

TABLE_TITLES_ROW = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[4]/div/div/table/thead/tr')
NAME_TABLE_TITLE = (By.XPATH, f'{TABLE_TITLES_ROW}/th[1]/span')
OFFER_TITLE_TABLE_TITLE = (By.XPATH, f'{TABLE_TITLES_ROW}/th[2]/span')
SUBJECT_TABLE_TITLE = (By.XPATH, f'{TABLE_TITLES_ROW}/th[3]/span')
PRICE_TABLE_TITLE = (By.XPATH, f'{TABLE_TITLES_ROW}/th[4]/span')
LAST_UPDATE_TABLE_TITLE = (By.XPATH, f'{TABLE_TITLES_ROW}/th[5]/span')
STATUS_TABLE_TITLE = (By.XPATH, f'{TABLE_TITLES_ROW}/th[6]/span')

ROW_WITH_NO_MATCHES = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[4]/div/div[2]')

SORTING_BUTTON = (By.XPATH, '//*[@aria-haspopup="listbox"]')
LIST_OF_SORTING_OPTIONS = (By.XPATH, '//*[@id="menu-"]/div[3]/ul/li')
NEWEST_OPTION = (By.XPATH, '//*[@id="menu-"]/div[3]/ul/li[1]')
NAME_OPTION = (By.XPATH, '//*[@id="menu-"]/div[3]/ul/li[2]')
PRICE_LOW_HIGH_OPTION = (By.XPATH, '//*[@id="menu-"]/div[3]/ul/li[3]')
PRICE_HIGH_LOW_OPTION = (By.XPATH, '//*[@id="menu-"]/div[3]/ul/li[4]')

//*[@id="root"]/div/div[2]/div[2]/div[4]/div/div/table/tbody/tr[3]
//*[@id="root"]/div/div[2]/div[2]/div[4]/div/div/table/tbody/tr[2]

class MyCooperationsPageStudent(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_main_navigation_link(self) -> WebElement:
        return self.driver.find_element(*MAIN_NAVIGATION_LINK)

    def click_main_navigation_link(self):
        self.get_main_navigation_link().click()

    def get_current_page_name(self) -> str:
        return self.driver.find_element(*CURRENT_PAGE_NAME).text

    def get_my_cooperations_page_title(self) -> str:
        return self.driver.find_element(*MY_COOPERATIONS_PAGE_TITLE).text

    def get_view_my_offers_btn(self) -> WebElement:
        return self.driver.find_element(*VIEW_MY_OFFERS_BTN)

    def click_view_my_offers_btn(self):
        self.get_view_my_offers_btn().click()

    def get_all_table_filter(self) -> WebElement:
        return self.driver.find_element(*ALL_TABLE_FILTER)

    def click_all_table_filter(self):
        self.get_all_table_filter().click()

    def get_active_table_filter(self) -> WebElement:
        return self.driver.find_element(*ACTIVE_TABLE_FILTER)

    def click_active_table_filter(self):
        self.get_active_table_filter().click()

    def get_pending_table_filter(self) -> WebElement:
        return self.driver.find_element(*PENDING_TABLE_FILTER)

    def click_pending_table_filter(self):
        self.get_pending_table_filter().click()

    def get_closed_table_filter(self) -> WebElement:
        return self.driver.find_element(*CLOSED_TABLE_FILTER)

    def click_closed_table_filter(self):
        self.get_closed_table_filter().click()

    def get_filter_text_field(self) -> WebElement:
        return self.driver.find_element(*FILTER_TEXT_FIELD)

    def get_row_view_toggle_button(self) -> WebElement:
        return self.driver.find_element(*ROW_VIEW_TOGGLE_BUTTON)

    def click_row_view_toggle_button(self):
        self.get_row_view_toggle_button().click()

    def get_card_view_toggle_button(self) -> WebElement:
        return self.driver.find_element(*CARD_VIEW_TOGGLE_BUTTON)

    def click_card_view_toggle_button(self):
        self.get_card_view_toggle_button().click()

    def get_name_table_title(self) -> str:
        return self.driver.find_element(*NAME_TABLE_TITLE).text

    def get_name_table_title_element(self) -> WebElement:
        return self.driver.find_element(*NAME_TABLE_TITLE)

    def click_name_table_title_element(self):
        self.get_name_table_title_element().click()

    def get_offer_title_table_title(self) -> str:
        return self.driver.find_element(*OFFER_TITLE_TABLE_TITLE).text

    def get_subject_table_title(self) -> str:
        return self.driver.find_element(*SUBJECT_TABLE_TITLE).text

    def get_price_table_title(self) -> str:
        return self.driver.find_element(*PRICE_TABLE_TITLE).text

    def get_price_table_title_element(self) -> WebElement:
        return self.driver.find_element(*PRICE_TABLE_TITLE)

    def click_price_table_title_element(self):
        self.get_price_table_title_element().click()

    def get_last_update_table_title(self) -> str:
        return self.driver.find_element(*LAST_UPDATE_TABLE_TITLE).text

    def get_last_update_table_title_element(self) -> WebElement:
        return self.driver.find_element(*LAST_UPDATE_TABLE_TITLE)

    def click_last_update_table_title_element(self):
        self.get_last_update_table_title_element().click()

    def get_status_table_title(self) -> str:
        return self.driver.find_element(*STATUS_TABLE_TITLE).text

    def get_sorting_button(self) -> WebElement:
        return self.driver.find_element(*SORTING_BUTTON)

    def get_sorting_button_text(self) -> str:
        return self.get_sorting_button().text

    def click_sorting_button(self):
        self.get_sorting_button().click()

    def get_list_of_sorting_options(self) -> list:
        list_of_sorting_options = []
        for option in self.driver.find_elements(*LIST_OF_SORTING_OPTIONS):
            list_of_sorting_options.append(option.text)
        return list_of_sorting_options

    def get_newest_option(self) -> WebElement:
        return self.driver.find_element(*NEWEST_OPTION)

    def click_newest_option(self):
        self.get_newest_option().click()

    def get_name_option(self) -> WebElement:
        return self.driver.find_element(*NAME_OPTION)

    def click_name_option(self):
        self.get_name_option().click()

    def get_price_low_high_option(self) -> WebElement:
        return self.driver.find_element(*PRICE_LOW_HIGH_OPTION)

    def click_price_low_high_option(self):
        self.get_price_low_high_option().click()

    def get_price_high_low_option(self) -> WebElement:
        return self.driver.find_element(*PRICE_HIGH_LOW_OPTION)

    def click_price_high_low_option(self):
        self.get_price_high_low_option().click()

    def get_row_with_no_matches(self) -> WebElement:
        return self.driver.find_element(*ROW_WITH_NO_MATCHES)

    def get_row_with_no_matches_text(self) -> str:
        return self.get_row_with_no_matches().text
