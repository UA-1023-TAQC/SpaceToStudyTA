from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent

CLOSE_BUTTON = (By.XPATH, "./button")

LEVEL_TITLE = (By.XPATH, "./div/p")
BLOCK_OF_LEVEL_FILTERS = (By.XPATH, "./div/div[1]")
LEVEL_BEGINNER_CHECKBOX = (By.XPATH, "./div/div[1]/label[1]/span/input")
LEVEL_BEGINNER_TITLE = (By.XPATH, "./div/div[1]/label[1]/p")
LEVEL_INTERMEDIATE_CHECKBOX = (By.XPATH, "./div/div[1]/label[2]/span/input")
LEVEL_INTERMEDIATE_TITLE = (By.XPATH, "./div/div[1]/label[2]/p")
LEVEL_ADVANCED_CHECKBOX = (By.XPATH, "./div/div[1]/label[3]/span/input")
LEVEL_ADVANCED_TITLE = (By.XPATH, "./div/div[1]/label[3]/p")
LEVEL_TEST_PREPARATION_CHECKBOX = (By.XPATH, "./div/div[1]/label[4]/span/input")
LEVEL_TEST_PREPARATION_TITLE = (By.XPATH, "./div/div[1]/label[4]/p")
LEVEL_PROFESSIONAL_CHECKBOX = (By.XPATH, "./div/div[1]/label[5]/span/input")
LEVEL_PROFESSIONAL_TITLE = (By.XPATH, "./div/div[1]/label[5]/p")
LEVEL_SPECIALIZED_CHECKBOX = (By.XPATH, "./div/div[1]/label[6]/span/input")
LEVEL_SPECIALIZED_TITLE = (By.XPATH, "./div/div[1]/label[6]/p")

LANGUAGE_TITLE = (By.XPATH, "./div/p[2]")
LANGUAGE_INPUT = (By.XPATH, "./div/div[2]/div/div/div/input")
NATIVE_SPEAKER_CHECKBOX = (By.XPATH, "./div/div[2]/label/span/input")
NATIVE_SPEAKER_TITLE = (By.XPATH, "./div/div[2]/label/p")

PRICE_TITLE = (By.XPATH, "./div/p[3]")
PRICE_BLOCK = (By.XPATH, "./div/div[3]")
PRICE_LEFT_SLIDER = (By.XPATH, "./div/div[3]/span/span[7]/input")
PRICE_RIGHT_SLIDER = (By.XPATH, "./div/div[3]/span/span[8]/input")
PRICE_LOWEST_VALUE_ON_SLIDER = (By.XPATH, "./div/div[3]/span/span[4]")
PRICE_HIGHEST_VALUE_ON_SLIDER = (By.XPATH, "./div/div[3]/span/span[6]")
PRICE_LOWEST_VALUE_INPUT = (By.XPATH, "./div/div[3]/div/div[1]/div/div/input")
PRICE_HIGHEST_VALUE_INPUT = (By.XPATH, "./div/div[3]/div/div[2]/div/div/input")

RATING_TITLE = (By.XPATH, "./div/p[4]")
RATING_BLOCK = (By.XPATH, "./div/div[4]/div")
RATING_ANY_RATING_RADIOBTN = (By.XPATH, "./div/div[4]/div/label[1]/span[1]/input")
RATING_ANY_RATING_TITLE = (By.XPATH, "./div/div[4]/div/label[1]/span[2]")
RATING_5_STARS_RADIOBTN = (By.XPATH, "./div/div[4]/div/label[2]/span[1]/input")
RATING_5_STARS_TITLE = (By.XPATH, "./div/div[4]/div/label[2]/span[2]")
RATING_4_AND_ABOVE_RADIOBTN = (By.XPATH, "./div/div[4]/div/label[3]/span[1]/input")
RATING_4_AND_ABOVE_TITLE = (By.XPATH, "./div/div[4]/div/label[3]/span[2]")
RATING_3_AND_ABOVE_CRADIOBTN = (By.XPATH, "./div/div[4]/div/label[4]/span[1]/input")
RATING_3_AND_ABOVE_TITLE = (By.XPATH, "./div/div[4]/div/label[4]/span[2]")

SEARCH_BY_NAME_TITLE = (By.XPATH, "./div/p[5]")
SEARCH_BY_NAME_INPUT = (By.XPATH, "./div/div[5]/div/input")

APPLY_FILTERS_BTN = (By.XPATH, ".//button[contains(text(), 'Apply filters')]")
CLEAR_FILTERS_BTN = (By.XPATH, ".//button[contains(text(), 'Clear filters')]")


class FiltersSidebarComponent(BaseComponent):
    def __init__(self, node):
        super().__init__(node)

    def click_level_beginner_checkbox(self):
        self.node.find_element(*LEVEL_BEGINNER_CHECKBOX).click()
        return self

    def click_level_intermediate_checkbox(self):
        self.node.find_element(*LEVEL_INTERMEDIATE_CHECKBOX).click()
        return self

    def click_level_advanced_checkbox(self):
        self.node.find_element(*LEVEL_ADVANCED_CHECKBOX).click()
        return self

    def click_level_test_preparation_checkbox(self):
        self.node.find_element(*LEVEL_TEST_PREPARATION_CHECKBOX).click()
        return self

    def click_level_professional_checkbox(self):
        self.node.find_element(*LEVEL_PROFESSIONAL_CHECKBOX).click()
        return self

    def click_level_specialized_checkbox(self):
        self.node.find_element(*LEVEL_SPECIALIZED_CHECKBOX).click()
        return self

    def click_language_input(self):
        self.node.find_element(*LANGUAGE_INPUT).click()
        return self

    def set_language_input(self, language):
        self.node.find_element(*LANGUAGE_INPUT).send_keys(language)
        return self

    def click_native_speaker_checkbox(self):
        self.node.find_element(*NATIVE_SPEAKER_CHECKBOX).click()
        return self

    def click_any_rating_radio_btn(self):
        self.node.find_element(*RATING_ANY_RATING_RADIOBTN).click()
        return self

    def click_5_stars_radio_btn(self):
        self.node.find_element(*RATING_5_STARS_RADIOBTN).click()
        return self

    def click_4_and_above_radio_btn(self):
        self.node.find_element(*RATING_4_AND_ABOVE_RADIOBTN).click()
        return self

    def click_3_and_above_radio_btn(self):
        self.node.find_element(*RATING_3_AND_ABOVE_CRADIOBTN).click()
        return self

    def click_apply_filters_btn(self):
        from SpaceToStudy.ui.pages.explore_offers.explore_offers_page import ExploreOffersPage
        self.node.find_element(*APPLY_FILTERS_BTN).click()
        return ExploreOffersPage(self.node.parent)
