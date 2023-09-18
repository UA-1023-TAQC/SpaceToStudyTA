from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.elements.slider import Slider
from SpaceToStudy.ui.pages.base_component import BaseComponent

CLOSE_BUTTON = (By.XPATH, "//div[@role='dialog']//button[@type='button']")

TITLE_MODAL = (By.XPATH, "//p[contains(text(),'Enroll offer')]")
YOUR_REQUIRED_LEVEL_DROPDOWN = (By.XPATH, "//div[@aria-labelledby='select-label']")
YOUR_REQUIRED_LEVEL_DROPDOWN_LIST = (By.XPATH, "//ul[@aria-labelledby='select-label']")
LEVEL_DROPDOWN_ITEM = (By.XPATH, "//ul[@aria-labelledby='select-label']/li")

PREFERRED_PRICE_SLIDER = (By.XPATH, "//form/div[3]/div[1]/span")
PREFERRED_PRICE_LOWEST_VALUE_ON_SLIDER = (By.XPATH, "//span[@data-index='0'][1]")
PREFERRED_PRICE_LOWEST_VALUE_ON_SLIDER_LABEL = (By.XPATH, "//span[@data-index='0'][2]")
PREFERRED_PRICE_HIGHEST_VALUE_ON_SLIDER = (By.XPATH, "//span[@data-index='1'][1]")
PREFERRED_PRICE_HIGHEST_VALUE_ON_SLIDER_LABEL = (By.XPATH, "//span[@data-index='1'][2]")
PREFERRED_PRICE_SLIDER_THUMB = (By.XPATH, "//input[@type='range']")
PREFERRED_PRICE_INPUT = (By.XPATH, "//input[@inputmode='numeric']")

ADDITIONAL_INFORMATION_INPUT = (By.XPATH, "//textarea[@maxlength = '1000']")
SEND_COOPERATION_REQUEST_BTN = (By.XPATH, "//div[@role='dialog']//button[@type='submit']")
GRID_CARD_COMPONENT = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div/div")


class EnrollOfferModal(BaseComponent):

    def __init__(self, node):
        super().__init__(node)
        self._title_modal = None
        self._your_required_level_dropdown = None
        self._list_of_available_levels = None
        self._preferred_price_slider = None
        self._preferred_price_input = None
        self._additional_information_input = None
        self._send_cooperation_request_btn = None
        self._inline_card_component = None

    def get_your_required_level_dropdown(self):
        self.node.find_element(*YOUR_REQUIRED_LEVEL_DROPDOWN).click()
        return self

    def get_list_of_available_levels(self) -> list:
        levels = self.node.find_elements(*LEVEL_DROPDOWN_ITEM)
        self._list_of_available_levels = []
        for level in levels:
            self._list_of_available_levels.append(level)
        return self._list_of_available_levels

    def select_required_level_option(self, required_level: str):
        list_of_levels = self.get_list_of_available_levels()
        for level in list_of_levels:
            if level.get_attribute("data-value") == required_level:
                level.click()
        return self

    def get_lowest_price_on_slider(self) -> WebElement:
        return self.node.find_element(*PREFERRED_PRICE_LOWEST_VALUE_ON_SLIDER)

    def get_highest_price_on_slider(self) -> WebElement:
        return self.node.find_element(*PREFERRED_PRICE_HIGHEST_VALUE_ON_SLIDER)

    def get_lowest_price_label(self) -> int:
        return int(self.node.find_element(*PREFERRED_PRICE_LOWEST_VALUE_ON_SLIDER_LABEL)
                   .get_attribute('value'))

    def get_highest_price_label(self) -> int:
        return int(self.node.find_element(*PREFERRED_PRICE_HIGHEST_VALUE_ON_SLIDER_LABEL)
                   .get_attribute('value'))

    def set_lowest_price(self):
        self.get_lowest_price_on_slider().click()
        return self

    def set_highest_price(self):
        self.get_highest_price_on_slider().click()
        return self

    def get_current_price_label(self) -> float:
        current_price = self.node.find_element(*PREFERRED_PRICE_INPUT)
        return float(current_price.get_attribute('value'))

    def set_preferred_price_input(self, value):
        price = (self.node.find_element(*PREFERRED_PRICE_INPUT))
        price.send_keys(Keys.CONTROL + "a")
        price.send_keys(Keys.DELETE)
        price.send_keys(value)
        return self

    def drag_price_slider_left(self, pixels: int):
        slider = self.node.find_element(*PREFERRED_PRICE_SLIDER)
        slider_thumb = self.node.find_element(*PREFERRED_PRICE_SLIDER_THUMB)
        Slider(self.node).drag_slider_left(pixels, slider, slider_thumb)
        return self

    def drag_price_slider_right(self, pixels: int):
        slider = self.node.find_element(*PREFERRED_PRICE_SLIDER)
        slider_thumb = self.node.find_element(*PREFERRED_PRICE_SLIDER_THUMB)
        Slider(self.node).drag_slider_right(pixels, slider, slider_thumb)
        return self

    def drag_price_slider_to_value(self, value: int):
        slider = self.node.find_element(*PREFERRED_PRICE_SLIDER)
        slider_thumb = self.node.find_element(*PREFERRED_PRICE_SLIDER_THUMB)
        Slider(self.node).drag_slider_to_value(value, slider, slider_thumb)
        return self

    def add_additional_information(self, additional_information: str):
        self.node.find_element(*ADDITIONAL_INFORMATION_INPUT).send_keys(additional_information)
        return self

    def get_send_cooperation_request_btn(self):
        return self.node.find_element(*SEND_COOPERATION_REQUEST_BTN)

    def click_send_cooperation_request_btn(self):
        from SpaceToStudy.ui.pages.offer_details.offer_details import OfferDetailsPage
        self.get_send_cooperation_request_btn().click()
        return OfferDetailsPage(self.node)
