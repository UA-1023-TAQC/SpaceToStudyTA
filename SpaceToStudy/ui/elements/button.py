import allure
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.elements.base_element import BaseElement


class Button(BaseElement):
    def __init__(self, node: WebElement):
        super().__init__(node)

    @allure.step("Get button element")
    def get_button(self):
        return self.node

    @allure.step("Click button element")
    def click_button(self):
        self.get_button().click()

    @allure.step("Check if button element is enabled ")
    def is_enabled_button(self):
        return self.get_button().is_enabled()

    @allure.step("Get the value of {property_name} css property button element")
    def get_value_css_property(self, property_name):
        return self.get_button().value_of_css_property(property_name)
