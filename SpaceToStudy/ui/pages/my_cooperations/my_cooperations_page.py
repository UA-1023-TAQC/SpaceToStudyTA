import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_page import BasePage


NAVIGATION_BAR = (By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/nav')
MAIN_NAVIGATION_LINK = (By.XPATH, '//a[text()="Main"]')
CURRENT_PAGE_NAME = (By.XPATH, '//p[@to="my-cooperations"]')
MY_COOPERATIONS_PAGE_TITLE = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/p')
VIEW_MY_OFFERS_BTN = (By.XPATH, '//a[contains(text(), "View my offers")]')

TABLE_FILTER_BAR_START_PATH = '//*[@id="root"]/div/div[2]/div[2]/div[2]'
ALL_TABLE_FILTER = (By.XPATH, f'{TABLE_FILTER_BAR_START_PATH}/button[1]')
ACTIVE_TABLE_FILTER = (By.XPATH, f'{TABLE_FILTER_BAR_START_PATH}/button[2]')
PENDING_TABLE_FILTER = (By.XPATH, f'{TABLE_FILTER_BAR_START_PATH}/button[3]')
CLOSED_TABLE_FILTER = (By.XPATH, f'{TABLE_FILTER_BAR_START_PATH}/button[4]')

FILTER_TEXT_FIELD = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[3]/div[1]/div/input')
ROW_VIEW_TOGGLE_BUTTON = (By.XPATH, '//button[@aria-label="inline card view"]')
CARD_VIEW_TOGGLE_BUTTON = (By.XPATH, '//button[@aria-label="grid card view"]')

TABLE_TITLES_ROW_START_PATH = '//*[@id="root"]/div/div[2]/div[2]/div[4]/div/div/table/thead/tr'
NAME_TABLE_TITLE = (By.XPATH, f'{TABLE_TITLES_ROW_START_PATH}/th[1]/span')
OFFER_TITLE_TABLE_TITLE = (By.XPATH, f'{TABLE_TITLES_ROW_START_PATH}/th[2]/span')
SUBJECT_TABLE_TITLE = (By.XPATH, f'{TABLE_TITLES_ROW_START_PATH}/th[3]/span')
PRICE_TABLE_TITLE = (By.XPATH, f'{TABLE_TITLES_ROW_START_PATH}/th[4]/span')
LAST_UPDATE_TABLE_TITLE = (By.XPATH, f'{TABLE_TITLES_ROW_START_PATH}/th[5]/span')
STATUS_TABLE_TITLE = (By.XPATH, f'{TABLE_TITLES_ROW_START_PATH}/th[6]/span')

ROW_WITH_NO_MATCHES = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[4]/div/div[2]')

SORTING_BUTTON = (By.XPATH, '//*[@aria-haspopup="listbox"]')
LIST_OF_SORTING_OPTIONS = (By.XPATH, '//*[@id="menu-"]/div[3]/ul/li')
NEWEST_OPTION = (By.XPATH, '//*[@id="menu-"]/div[3]/ul/li[1]')
NAME_OPTION = (By.XPATH, '//*[@id="menu-"]/div[3]/ul/li[2]')
PRICE_LOW_HIGH_OPTION = (By.XPATH, '//*[@id="menu-"]/div[3]/ul/li[3]')
PRICE_HIGH_LOW_OPTION = (By.XPATH, '//*[@id="menu-"]/div[3]/ul/li[4]')


class MyCooperationsPage(BasePage):
    @allure.step("Get the link to my cooperations page in the main navigation in the header by clicking the account icon")
    def get_main_navigation_link(self) -> WebElement:
        return self.driver.find_element(*MAIN_NAVIGATION_LINK)

    @allure.step("Click the link to my cooperations page in the main navigation in the header by clicking the account icon")
    def click_main_navigation_link(self):
        self.get_main_navigation_link().click()

    @allure.step("Get a name of the my cooperations page (element near Main)")
    def get_current_page_name(self) -> str:
        return self.driver.find_element(*CURRENT_PAGE_NAME).text
    
    @allure.step("Get a title of the my cooperations page (a big bold phrase)")
    def get_my_cooperations_page_title(self) -> str:
        return self.driver.find_element(*MY_COOPERATIONS_PAGE_TITLE).text

    @allure.step("Get 'View my offers' button)")
    def get_view_my_offers_btn(self) -> WebElement:
        return self.driver.find_element(*VIEW_MY_OFFERS_BTN)

    @allure.step("Click 'View my offers' button)")
    def click_view_my_offers_btn(self):
        self.get_view_my_offers_btn().click()

    @allure.step("Get the filter button for displaying all offers")
    def get_all_table_filter(self) -> WebElement:
        return self.driver.find_element(*ALL_TABLE_FILTER)

    @allure.step("Click the filter button for displaying all offers")
    def click_all_table_filter(self):
        self.get_all_table_filter().click()

    @allure.step("Get the filter button for displaying offers with the status 'active'")
    def get_active_table_filter(self) -> WebElement:
        return self.driver.find_element(*ACTIVE_TABLE_FILTER)

    @allure.step("Click the filter button for displaying offers with the status 'active'")
    def click_active_table_filter(self):
        self.get_active_table_filter().click()

    @allure.step("Get the filter button for displaying offers with the status 'pending'")
    def get_pending_table_filter(self) -> WebElement:
        return self.driver.find_element(*PENDING_TABLE_FILTER)

    @allure.step("Click the filter button for displaying offers with the status 'pending'")
    def click_pending_table_filter(self):
        self.get_pending_table_filter().click()

    @allure.step("Get the filter button for displaying offers with the status 'closed'")
    def get_closed_table_filter(self) -> WebElement:
        return self.driver.find_element(*CLOSED_TABLE_FILTER)

    @allure.step("Click the filter button for displaying offers with the status 'closed'")
    def click_closed_table_filter(self):
        self.get_closed_table_filter().click()

    @allure.step("Get the area 'Search user name or title'")
    def get_filter_text_field(self) -> WebElement:
        return self.driver.find_element(*FILTER_TEXT_FIELD)

    @allure.step("Get the toggle-button for displaying offers in a table format")
    def get_row_view_toggle_button(self) -> WebElement:
        return self.driver.find_element(*ROW_VIEW_TOGGLE_BUTTON)

    @allure.step("Click the toggle-button for displaying offers in a table format")
    def click_row_view_toggle_button(self):
        self.get_row_view_toggle_button().click()

    @allure.step("Get the toggle-button for displaying offers in a card format")
    def get_card_view_toggle_button(self) -> WebElement:
        return self.driver.find_element(*CARD_VIEW_TOGGLE_BUTTON)

    @allure.step("Click the toggle-button for displaying offers in a card format")
    def click_card_view_toggle_button(self):
        self.get_card_view_toggle_button().click()

    @allure.step("Get a name of the 'Name' column of the offers table")
    def get_name_table_title(self) -> str:
        return self.driver.find_element(*NAME_TABLE_TITLE).text

    @allure.step("Get the element of a name of the 'Name' column of the offers table")
    def get_name_table_title_element(self) -> WebElement:
        return self.driver.find_element(*NAME_TABLE_TITLE)

    @allure.step("Click the element of a name of the 'Name' column of the offers table to sort offers by names")
    def click_name_table_title_element(self):
        self.get_name_table_title_element().click()

    @allure.step("Get a name of the 'Offer title' column of the offers table")
    def get_offer_title_table_title(self) -> str:
        return self.driver.find_element(*OFFER_TITLE_TABLE_TITLE).text

    @allure.step("Get a name of the 'Subject' column of the offers table")
    def get_subject_table_title(self) -> str:
        return self.driver.find_element(*SUBJECT_TABLE_TITLE).text

    @allure.step("Get a name of the 'Price' column of the offers table")
    def get_price_table_title(self) -> str:
        return self.driver.find_element(*PRICE_TABLE_TITLE).text

    @allure.step("Get the element of a name of the 'Price' column of the offers table")
    def get_price_table_title_element(self) -> WebElement:
        return self.driver.find_element(*PRICE_TABLE_TITLE)

    @allure.step("Click the element of a name of the 'Price' column of the offers table to sort offers by prices")
    def click_price_table_title_element(self):
        self.get_price_table_title_element().click()

    @allure.step("Get a name of the 'Last update' column of the offers table")
    def get_last_update_table_title(self) -> str:
        return self.driver.find_element(*LAST_UPDATE_TABLE_TITLE).text

    @allure.step("Get the element of a name of the 'Last update' column of the offers table")
    def get_last_update_table_title_element(self) -> WebElement:
        return self.driver.find_element(*LAST_UPDATE_TABLE_TITLE)

    @allure.step("Click the element of a name of the 'Last update' column of the offers table to sort offers by last updating dates")
    def click_last_update_table_title_element(self):
        self.get_last_update_table_title_element().click()

    @allure.step("Get a name of the 'Status' column of the offers table")
    def get_status_table_title(self) -> str:
        return self.driver.find_element(*STATUS_TABLE_TITLE).text

    @allure.step("Get the offers sorting button when offers are displayed in a card format")
    def get_sorting_button(self) -> WebElement:
        return self.driver.find_element(*SORTING_BUTTON)

    @allure.step("Get a current selected sorting option when offers are displayed in a card format")
    def get_sorting_button_text(self) -> str:
        return self.get_sorting_button().text

    @allure.step("Click the offers sorting button when offers are displayed in a card format")
    def click_sorting_button(self):
        self.get_sorting_button().click()

    @allure.step("Get a list of all availble sorting options when offers are displayed in a card format")
    def get_list_of_sorting_options(self) -> list:
        list_of_sorting_options = []
        for option in self.driver.find_elements(*LIST_OF_SORTING_OPTIONS):
            list_of_sorting_options.append(option.text)
        return list_of_sorting_options

    @allure.step("Get the 'Newest' sorting options when offers are displayed in a card format")
    def get_newest_option(self) -> WebElement:
        return self.driver.find_element(*NEWEST_OPTION)

    @allure.step("Click the 'Newest' sorting option to sort offers by last update dates when offers are displayed in a card format")
    def click_newest_option(self):
        self.get_newest_option().click()

    @allure.step("Get the 'Name' sorting option when offers are displayed in a card format")
    def get_name_option(self) -> WebElement:
        return self.driver.find_element(*NAME_OPTION)

    @allure.step("Click the 'Name' sorting option to sort offers by names when offers are displayed in a card format")
    def click_name_option(self):
        self.get_name_option().click()

    @allure.step("Get the 'Price low-high' sorting option when offers are displayed in a card format")
    def get_price_low_high_option(self) -> WebElement:
        return self.driver.find_element(*PRICE_LOW_HIGH_OPTION)

    @allure.step("Click the 'Price low-high' sorting option to sort offers by ascending prices when offers are displayed in a card format")
    def click_price_low_high_option(self):
        self.get_price_low_high_option().click()

    @allure.step("Get the 'Price high-low' sorting option when offers are displayed in a card format")
    def get_price_high_low_option(self) -> WebElement:
        return self.driver.find_element(*PRICE_HIGH_LOW_OPTION)

    @allure.step("Click the 'Price high-low' sorting option to sort offers by descending prices when offers are displayed in a card format")
    def click_price_high_low_option(self):
        self.get_price_high_low_option().click()

    @allure.step("Get the row 'No matches' in the offers table when you try to search for a non-existing user or title")
    def get_row_with_no_matches(self) -> WebElement:
        return self.driver.find_element(*ROW_WITH_NO_MATCHES)
    
    @allure.step("Get the text for 'No matches' row in the offers table when you try to search for a non-existing user or title")
    def get_row_with_no_matches_text(self) -> str:
        return self.get_row_with_no_matches().text
