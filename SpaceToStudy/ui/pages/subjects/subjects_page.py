from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_page import BasePage

SUBJECTS_TITLE = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/p')
SUBJECTS_SUBTEXT = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/span')
SHOW_OFFERS_BTN = (By.XPATH, '//a[text()="Show offers"]')
SHOW_CATEGORIES_BTN = (By.XPATH, '//a[text()="Categories"]')
CATEGORIES_INPUT = (By.XPATH, './div[1]/div/div/input')
SEARCH_INPUT = (By.XPATH, './div[2]/div/div/div/input')
SEARCH_FIELD_HELP_TEXT = (By.XPATH, '//*[@id="mui-5450-label"]')
SEARCH_BTN = (By.XPATH, '//button[text()="Search"]')

NO_RESULTS_TITLE = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[5]/div/div/p')
NO_RESULTS_SUBTEXT = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[5]/div/div/span')
REQUEST_A_NEW_SUBJECT_BTN = (By.XPATH, '//button[text()="Request a new subjects"]')

CARDS = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[5]/div/a")


class SubjectsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._cards = None

    def get_subjects_title(self) -> WebElement:
        return self.driver.find_element(*SUBJECTS_TITLE)

    @allure.step("Get title text")
    def get_text_subjects_title(self) -> str:
        return self.get_subjects_title().text

    def get_subjects_subtext(self) -> str:
        return self.driver.find_element(*SUBJECTS_SUBTEXT).text

    def get_show_offers_btn(self) -> WebElement:
        return self.driver.find_element(*SHOW_OFFERS_BTN)

    def click_show_offers_btn(self):
        self.get_show_offers_btn().click()

    def get_show_categories_btn(self) -> WebElement:
        return self.driver.find_element(*SHOW_CATEGORIES_BTN)

    def click_show_categories_btn(self):
        self.get_show_categories_btn().click()

    def get_categories_input(self) -> WebElement:
        return self.driver.find_element(*CATEGORIES_INPUT)

    def set_categories_input(self, categories):
        self.get_categories_input().send_keys(categories)

    def get_search_input(self) -> WebElement:
        return self.driver.find_element(*SEARCH_INPUT)

    def set_search(self, text):
        self.get_search_input().send_keys(text)

    def get_search_field_help_text(self) -> str:
        return self.driver.find_element(*SEARCH_FIELD_HELP_TEXT).text

    def get_search_btn(self) -> WebElement:
        return self.driver.find_element(*SEARCH_BTN)

    def click_search_btn(self):
        self.get_search_btn().click()

    def get_no_results_title(self) -> str:
        return self.driver.find_element(*NO_RESULTS_TITLE).text

    def get_no_results_subtext(self) -> str:
        return self.driver.find_element(*NO_RESULTS_SUBTEXT).text

    def get_request_a_new_subject_btn(self) -> WebElement:
        return self.driver.find_element(*REQUEST_A_NEW_SUBJECT_BTN)

    def click_request_a_new_subject_btn(self):
        self.get_request_a_new_subject_btn().click()

    def get_cards(self) -> list:
        from SpaceToStudy.ui.pages.categories.card_component import CardComponent
        if not self._cards:
            card_set = self.driver.find_elements(*CARDS)
            self._cards = [CardComponent(card) for card in card_set]
        return self._cards