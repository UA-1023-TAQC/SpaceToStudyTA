from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.elements.input_with_drop_down_list import InputDropDownList
from SpaceToStudy.ui.pages.base_component import BaseComponent

from time import sleep

CLOSE_BUTTON = (By.XPATH, "./button")


TITLE_MODAL = (By.XPATH, "//p[contains(text(),'Enroll offer')]")
YOUR_REQUIRED_LEVEL_DROPDOWN = (By.XPATH,
                                "/html/body/div[2]/div[3]/div/div/div/div/form/div[2]/div/div/div")
YOUR_REQUIRED_LEVEL_DROPDOWN_LIST = (By.XPATH,
                                     "/html/body/div[3]/div[3]/ul")
YOUR_REQUIRED_LEVEL_DROPDOWN_ITEM = (By.XPATH, "/html/body/div[3]/div[3]/ul/li[2]")
PREFERRED_PRICE_SLIDER = (By.XPATH,
                        "/html/body/div[2]/div[3]/div/div/div/div/form/div[3]/div[1]")
PREFERRED_PRICE_LOWEST_VALUE_ON_SLIDER = (By.XPATH,
                                    "/html/body/div[2]/div[3]/div/div/div/div/form/div[3]/div[1]/span/span[3]")
PREFERRED_PRICE_LOWEST_VALUE_ON_SLIDER_INPUT = (By.XPATH,
                                                "/html/body/div[2]/div[3]/div/div/div/div/form/div[3]/div[1]/span/span[4]")

PREFERRED_PRICE_HIGHEST_VALUE_ON_SLIDER = (By.XPATH,
                                     "/html/body/div[2]/div[3]/div/div/div/div/form/div[3]/div[1]/span/span[5]")
PREFERRED_PRICE_HIGHEST_VALUE_ON_SLIDER_INPUT = (By.XPATH,
                                                 "/html/body/div[2]/div[3]/div/div/div/div/form/div[3]/div[1]/span/span[6]")
PREFERRED_PRICE_SLIDER_MOVING_CIRCLE = (By.XPATH,
                                        "/html/body/div[2]/div[3]/div/div/div/div/form/div[3]/div[1]/span/span[5]")
PREFERRED_PRICE_INPUT = (By.XPATH,
                         "/html/body/div[2] /div[3] /div/div/div/div/form/div[3] /div[2] /div/input")
ADDITIONAL_INFORMATION_INPUT = (By.XPATH,
                                "/html/body/div[2]/div[3]/div/div/div/div/form/div[4]/div/div/textarea[1]")
SEND_COOPERATION_REQUEST_BTN = (By.XPATH,
                                "/html/body/div[2]/div[3]/div/div/div/div/form/button")
INLINE_CARD_COMPONENT = (By.XPATH,
                         "/html/body/div[2]/div[3]/div/div/div/div/div/div")




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

    def get_your_required_level_dropdown(self) -> InputDropDownList:
        if not self._your_required_level_dropdown:
            node = self.node.find_element(*YOUR_REQUIRED_LEVEL_DROPDOWN)
            self._your_required_level_dropdown = InputDropDownList(node)
        return self._your_required_level_dropdown

    def get_list_of_available_levels(self) -> list:
        levels = self.driver.find_element(*YOUR_REQUIRED_LEVEL_DROPDOWN_LIST).find_elements(*YOUR_REQUIRED_LEVEL_DROPDOWN_ITEM)
        self._list_of_available_levels = []
        for level in levels:
        #    self._list_of_available_levels.append(InlineCardComponent(offer))
        return self._list_of_available_levels

    def select_required_level_option(self, required_level):
        list_of_levels = self.get_list_of_available_levels()
        for level in list_of_levels:
            if level.get_attribute("data-value") == required_level:
                level.click()
        return self

    def get_lowest_price_on_slider(self):
        return int(self.node.find_element(*PREFERRED_PRICE_LOWEST_VALUE_ON_SLIDER).text)

    def get_highest_price_on_slider(self):
        return int(self.node.find_element(*PREFERRED_PRICE_HIGHEST_VALUE_ON_SLIDER).text)

    def get_lowest_price_input(self):
        return int(self.node.find_element(*PREFERRED_PRICE_LOWEST_VALUE_ON_SLIDER_INPUT)
                     .get_attribute('value'))

    def get_highest_price_input(self):
        return int(self.node.find_element(*PREFERRED_PRICE_HIGHEST_VALUE_ON_SLIDER_INPUT)
                     .get_attribute('value'))

    def set_lowest_value_input(self, value):
        self.node.find_element(*PREFERRED_PRICE_LOWEST_VALUE_ON_SLIDER_INPUT).send_keys(value)
        return self

    def set_highest_value_input(self, value):
        self.node.find_element(*PREFERRED_PRICE_HIGHEST_VALUE_ON_SLIDER_INPUT).send_keys(value)
        return self

    def drag_left_slider(self, pixels_to_the_right):
        slider = self.node.find_element(*PREFERRED_PRICE_SLIDER_MOVING_CIRCLE)
        ActionChains(self.node.parent) \
            .drag_and_drop_by_offset(slider, pixels_to_the_right, 0) \
            .perform()
        return self

    def drag_right_slider(self, pixels_to_the_left):
        slider = self.node.find_element(*PREFERRED_PRICE_SLIDER_MOVING_CIRCLE)
        ActionChains(self.node.parent) \
            .drag_and_drop_by_offset(slider, -pixels_to_the_left, 0) \
            .perform()
        return self

    def set_custom_value_input(self, value):
        self.node.find_element(*PREFERRED_PRICE_INPUT).send_keys(value)
        return self

    def add_additional_information(self, additional_information:str):
        self.node.find_element(*ADDITIONAL_INFORMATION_INPUT).send_keys(additional_information)
        return self

    def get_send_cooperation_request_btn(self):
        return self.node.find_element(*SEND_COOPERATION_REQUEST_BTN)

    def click_send_cooperation_request_btn(self):
        self.get_send_cooperation_request_btn().click()
        sleep(5)

