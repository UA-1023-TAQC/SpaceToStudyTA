import allure
from selenium.webdriver import ActionChains
from time import sleep

from selenium.webdriver import Keys
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
LANGUAGE_LIST = (By.XPATH, "//div[@role='presentation']/div/ul/li")
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
RATING_ANY_RATING_RADIOBTN = (By.XPATH, "./div/div[4]/div/label[1]/span[1]")
RATING_ANY_RATING_TITLE = (By.XPATH, "./div/div[4]/div/label[1]/span[2]")
RATING_5_STARS_RADIOBTN = (By.XPATH, "./div/div[4]/div/label[2]/span[1]")
RATING_5_STARS_TITLE = (By.XPATH, "./div/div[4]/div/label[2]/span[2]")
RATING_4_AND_ABOVE_RADIOBTN = (By.XPATH, "./div/div[4]/div/label[3]/span[1]")
RATING_4_AND_ABOVE_TITLE = (By.XPATH, "./div/div[4]/div/label[3]/span[2]")
RATING_3_AND_ABOVE_RADIOBTN = (By.XPATH, "./div/div[4]/div/label[4]/span[1]")
RATING_3_AND_ABOVE_TITLE = (By.XPATH, "./div/div[4]/div/label[4]/span[2]")

SEARCH_BY_NAME_TITLE = (By.XPATH, "./div/p[5]")
SEARCH_BY_NAME_INPUT = (By.XPATH, "./div/div[5]/div/input")

APPLY_FILTERS_BTN = (By.XPATH, ".//button[contains(text(), 'Apply filters')]")
CLEAR_FILTERS_BTN = (By.XPATH, ".//button[contains(text(), 'Clear filters')]")


class FiltersSidebarComponent(BaseComponent):
    def __init__(self, node):
        super().__init__(node)
        self._list_of_languages = None

    @allure.step("Click on the level beginner checkbox")
    def click_level_beginner_checkbox(self):
        self.node.find_element(*LEVEL_BEGINNER_CHECKBOX).click()
        return self

    @allure.step("Click on the level intermediate checkbox")
    def click_level_intermediate_checkbox(self):
        self.node.find_element(*LEVEL_INTERMEDIATE_CHECKBOX).click()
        return self

    @allure.step("Click on the level advanced checkbox")
    def click_level_advanced_checkbox(self):
        self.node.find_element(*LEVEL_ADVANCED_CHECKBOX).click()
        return self

    @allure.step("Click on the level test preparation checkbox")
    def click_level_test_preparation_checkbox(self):
        self.node.find_element(*LEVEL_TEST_PREPARATION_CHECKBOX).click()
        return self

    @allure.step("Click on the level professional checkbox")
    def click_level_professional_checkbox(self):
        self.node.find_element(*LEVEL_PROFESSIONAL_CHECKBOX).click()
        return self

    @allure.step("Click on the level specialized checkbox")
    def click_level_specialized_checkbox(self):
        self.node.find_element(*LEVEL_SPECIALIZED_CHECKBOX).click()
        return self

    @allure.step("Click on the language input")
    def click_language_input(self):
        self.node.find_element(*LANGUAGE_INPUT).click()
        return self

    @allure.step("Get language input")
    def get_language_input(self):
        return self.node.find_element(*LANGUAGE_INPUT)

    @allure.step("Get list of languages")
    def get_list_of_languages(self) -> list:
        languages = self.node.find_elements(*LANGUAGE_LIST)
        self._list_of_languages = []
        for language in languages:
            self._list_of_languages.append(language.text)
        return self._list_of_languages

    @allure.step("Set language input")
    def set_language_input(self, language):
        languages = self.node.find_elements(*LANGUAGE_LIST)
        for item in languages:
            if item.text == language:
                item.click()
                break
        return self

    @allure.step("Click on the native speaker checkbox")
    def click_native_speaker_checkbox(self):
        self.node.find_element(*NATIVE_SPEAKER_CHECKBOX).click()
        return self

    @allure.step("Get the lowest value on slider")
    def get_lowest_value_on_slider(self):
        return float(self.node.find_element(*PRICE_LOWEST_VALUE_ON_SLIDER).text)

    @allure.step("Get the highest value on slider")
    def get_highest_value_on_slider(self):
        return float(self.node.find_element(*PRICE_HIGHEST_VALUE_ON_SLIDER).text)

    @allure.step("Get the lowest value input")
    def get_lowest_value_input(self):
        return float(self.node.find_element(*PRICE_LOWEST_VALUE_INPUT)
                     .get_attribute('value'))

    @allure.step("Get the highest value input")
    def get_highest_value_input(self):
        return float(self.node.find_element(*PRICE_HIGHEST_VALUE_INPUT)
                     .get_attribute('value'))

    @allure.step("Set the lowest value input")
    def set_lowest_value_input(self, value):
        self.node.find_element(*PRICE_LOWEST_VALUE_INPUT) \
            .send_keys(Keys.CONTROL + "a" + Keys.BACKSPACE)
        self.node.find_element(*PRICE_LOWEST_VALUE_INPUT).send_keys(value)
        return self

    @allure.step("Set the highest value input")
    def set_highest_value_input(self, value):
        self.node.find_element(*PRICE_HIGHEST_VALUE_INPUT)\
            .send_keys(Keys.CONTROL + "a" + Keys.BACKSPACE)
        self.node.find_element(*PRICE_HIGHEST_VALUE_INPUT).send_keys(value)
        return self

    @allure.step("Drag left slider")
    def drag_left_slider(self, pixels_to_the_right):
        slider = self.node.find_element(*PRICE_LEFT_SLIDER)
        ActionChains(self.node.parent) \
            .drag_and_drop_by_offset(slider, pixels_to_the_right, 0) \
            .perform()
        return self

    @allure.step("Drag right slider")
    def drag_right_slider(self, pixels_to_the_left):
        slider = self.node.find_element(*PRICE_RIGHT_SLIDER)
        ActionChains(self.node.parent) \
            .drag_and_drop_by_offset(slider, -pixels_to_the_left, 0) \
            .perform()
        return self

    @allure.step("Click on any rating radio button")
    def click_any_rating_radio_btn(self):
        self.node.find_element(*RATING_ANY_RATING_RADIOBTN).click()
        return self

    @allure.step("Click on the 5 stars radio button")
    def click_5_stars_radio_btn(self):
        self.node.find_element(*RATING_5_STARS_RADIOBTN).click()
        return self

    @allure.step("Click on the 4 stars and above radio button")
    def click_4_and_above_radio_btn(self):
        self.node.find_element(*RATING_4_AND_ABOVE_RADIOBTN).click()
        return self

    @allure.step("Click on the 3 stars and above radio button")
    def click_3_and_above_radio_btn(self):
        self.node.find_element(*RATING_3_AND_ABOVE_RADIOBTN).click()
        return self

    @allure.step("Set search by name input")
    def set_search_by_name_input(self, name):
        self.node.find_element(*SEARCH_BY_NAME_INPUT).send_keys(name)
        return self

    @allure.step("Click on the apply filters button")
    def click_apply_filters_btn(self):
        sleep(0.5)
        from SpaceToStudy.ui.pages.explore_offers.explore_offers_page import ExploreOffersPage
        self.node.find_element(*APPLY_FILTERS_BTN).click()
        return ExploreOffersPage(self.node.parent)

    @allure.step("Click on the clear filters button")
    def click_clear_filters_btn(self):
        self.node.find_element(*CLEAR_FILTERS_BTN).click()
        return self

    @allure.step("Click on the close button")
    def click_close_button(self):
        from SpaceToStudy.ui.pages.explore_offers.explore_offers_page import ExploreOffersPage
        self.node.find_element(*CLOSE_BUTTON).click()
        return ExploreOffersPage(self.node.parent)
