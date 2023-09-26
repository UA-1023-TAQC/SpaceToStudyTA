import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.elements.base_element import BaseElement

STARLINE = (By.XPATH, '//div[@data-testid="app-rating"]')
STARS = (By.XPATH, './span[1]')
NUMERIC_VALUE_FOR_STARS = (By.XPATH, './span[2]')


class Starline(BaseElement):
    def __init__(self, node: WebElement):
        super().__init__(node)

    @allure.step("Get starline")
    def get_starline(self) -> WebElement:
        return self.node.find_element(*STARLINE)

    @allure.step("Get stars view rating")
    def get_stars_view_rating(self):
        return self.node.find_element(*STARS)

    @allure.step("Get star view value")
    def get_stars_view_value(self) -> str:
        value = self.get_stars_view_rating().get_attribute('aria-label')
        match value:
            case '1 Star':
                return '1'
            case '2 Stars':
                return '2'
            case '3 Stars':
                return '3'
            case '4 Stars':
                return '4'
            case '5 Stars':
                return '5'
            case _:
                return 'Unknown'

    @allure.step("Get numeric value for stars")
    def get_numeric_value_for_stars(self) -> str:
        return self.node.find_element(*NUMERIC_VALUE_FOR_STARS).text
