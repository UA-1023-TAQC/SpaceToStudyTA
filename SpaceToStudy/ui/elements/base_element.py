import allure
from selenium.webdriver.remote.webelement import WebElement


class BaseElement:
    def __init__(self, node: WebElement):
        self.node = node

    @allure.step("Is element displayed")
    def is_displayed(self) -> bool:
        return self.node.is_displayed()

    @allure.step("Get the value of {property_name} css property of element")
    def get_value_css_property(self, property_name):
        return self.node.value_of_css_property(property_name)
