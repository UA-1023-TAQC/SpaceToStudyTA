import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.elements.slider import Slider
from SpaceToStudy.ui.pages.base_component import BaseComponent
from SpaceToStudy.ui.pages.explore_offers.grid_card_component import GridCardComponent

CLOSE_BTN = (By.XPATH, "//div[@role='dialog']//button[@type='button']")

MODAL_TITLE = (By.XPATH, "//p[contains(text(),'Enroll offer')]")
MODAL_TITLE_DESC = (By.XPATH, "//span[contains(text(), 'Send a Request to Create a Cooperation')]")

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
GRID_CARD_COMPONENT = (By.XPATH, "//div[@data-testid='popupContent']/div/div/div/div")


class EnrollOfferModal(BaseComponent):

    def __init__(self, node):
        super().__init__(node)
        self._modal_title = None
        self._modal_title_description = None
        self._your_required_level_dropdown = None
        self._list_of_available_levels = None
        self._preferred_price_slider = None
        self._preferred_price_input = None
        self._additional_information_input = None
        self._send_cooperation_request_btn = None
        self._grid_card_component = None

    @allure.step("Get the title of 'Enroll offer' modal window")
    def get_modal_title_text(self) -> str:
        if not self._modal_title:
            self._modal_title = self.node.find_element(*MODAL_TITLE).text
        return self._modal_title.text

    @allure.step("Get the description under the title of 'Enroll offer' modal window")
    def get_modal_title_description(self) -> str:
        if not self._modal_title_description:
            self._modal_title_description = self.node.find_element(*MODAL_TITLE_DESC)
        return self._modal_title_description.text

    @allure.step("Get 'Your required level' dropdown on 'Enroll offer' modal window")
    def get_your_required_level_dropdown(self):
        self.node.find_element(*YOUR_REQUIRED_LEVEL_DROPDOWN).click()
        return self

    @allure.step("Get the list of available levels of tutoring in 'Your required level' dropdown \
                on 'Enroll offer' modal window")
    def get_list_of_available_levels(self) -> list:
        levels = self.node.find_elements(*LEVEL_DROPDOWN_ITEM)
        self._list_of_available_levels = []
        for level in levels:
            self._list_of_available_levels.append(level)
        return self._list_of_available_levels

    @allure.step("Select level of tutoring in 'Your required level' dropdown on 'Enroll offer' modal window")
    def select_required_level_option(self, required_level: str):
        list_of_levels = self.get_list_of_available_levels()
        for level in list_of_levels:
            if level.get_attribute("data-value") == required_level:
                level.click()
        return self

    @allure.step("Get the lowest price WebElement on the slider on 'Enroll offer' modal window")
    def get_lowest_price_on_slider(self) -> WebElement:
        return self.node.find_element(*PREFERRED_PRICE_LOWEST_VALUE_ON_SLIDER)

    @allure.step("Get the highest price WebElement on the slider on 'Enroll offer' modal window")
    def get_highest_price_on_slider(self) -> WebElement:
        return self.node.find_element(*PREFERRED_PRICE_HIGHEST_VALUE_ON_SLIDER)

    @allure.step("Get the lowest price label on the slider on 'Enroll offer' modal window")
    def get_lowest_price_value(self) -> int:
        return int(self.node.find_element(*PREFERRED_PRICE_LOWEST_VALUE_ON_SLIDER_LABEL)
                   .get_attribute('value'))

    @allure.step("Get the highest price label on the slider on 'Enroll offer' modal window")
    def get_highest_price_value(self) -> int:
        return int(self.node.find_element(*PREFERRED_PRICE_HIGHEST_VALUE_ON_SLIDER_LABEL)
                   .get_attribute('value'))

    @allure.step("Set the lowest price on the slider on 'Enroll offer' modal window")
    def set_lowest_price(self):
        self.get_lowest_price_on_slider().click()
        return self

    @allure.step("Set the highest price on the slider on 'Enroll offer' modal window")
    def set_highest_price(self):
        self.get_highest_price_on_slider().click()
        return self

    @allure.step("Get the current price value on the slider on 'Enroll offer' modal window")
    def get_current_price_value(self) -> float:
        current_price = self.node.find_element(*PREFERRED_PRICE_INPUT)
        return float(current_price.get_attribute('value'))

    @allure.step("Set the preferred price in the input on 'Enroll offer' modal window")
    def set_preferred_price_input(self, value):
        price = (self.node.find_element(*PREFERRED_PRICE_INPUT))
        price.send_keys(Keys.CONTROL + "a")
        price.send_keys(Keys.DELETE)
        price.send_keys(value)
        return self

    @allure.step("Drag the slider to the left by {value} points on 'Enroll offer' modal window")
    def drag_price_slider_left(self, value: int):
        slider = self.node.find_element(*PREFERRED_PRICE_SLIDER)
        slider_thumb = self.node.find_element(*PREFERRED_PRICE_SLIDER_THUMB)
        Slider(self.node).drag_slider_left(value, slider, slider_thumb)
        return self

    @allure.step("Drag the slider to the right by {value} points on 'Enroll offer' modal window")
    def drag_price_slider_right(self, value: int):
        slider = self.node.find_element(*PREFERRED_PRICE_SLIDER)
        slider_thumb = self.node.find_element(*PREFERRED_PRICE_SLIDER_THUMB)
        Slider(self.node).drag_slider_right(value, slider, slider_thumb)
        return self

    @allure.step("Drag the slider to the {value} value on 'Enroll offer' modal window")
    def drag_price_slider_to_value(self, value: int):
        slider = self.node.find_element(*PREFERRED_PRICE_SLIDER)
        slider_thumb = self.node.find_element(*PREFERRED_PRICE_SLIDER_THUMB)
        Slider(self.node).drag_slider_to_value(value, slider, slider_thumb)
        return self

    @allure.step("Add the information in 'Additional information' text area on 'Enroll offer' modal window")
    def add_additional_information(self, additional_information: str):
        self.node.find_element(*ADDITIONAL_INFORMATION_INPUT).send_keys(additional_information)
        return self

    @allure.step("Get 'Send cooperation request' button on 'Enroll offer' modal window")
    def get_send_cooperation_request_btn(self):
        return self.node.find_element(*SEND_COOPERATION_REQUEST_BTN)

    @allure.step("Click 'Send cooperation request' button on 'Enroll offer' modal window")
    def click_send_cooperation_request_btn(self):
        from SpaceToStudy.ui.pages.offer_details.offer_details import OfferDetailsPage
        self.get_send_cooperation_request_btn().click()
        return OfferDetailsPage(self.node)

    @allure.step("Get 'GridCardComponent' component with the info about offer on 'Enroll offer' modal window")
    def get_grid_card_component(self) -> GridCardComponent:
        if not self._grid_card_component:
            node = self.node.find_element(*GRID_CARD_COMPONENT)
            self._grid_card_component = GridCardComponent(node)
        return self._grid_card_component

    @allure.step("Get 'Close' button in the upper right corner on 'Enroll offer' modal window")
    def get_close_btn(self):
        return self.node.find_element(*CLOSE_BTN)

    @allure.step("Click 'Close' button in the upper right corner on 'Enroll offer' modal window")
    def click_close_btn(self):
        from SpaceToStudy.ui.pages.offer_details.offer_details import OfferDetailsPage
        self.get_close_btn().click()
        return OfferDetailsPage(self.node)
