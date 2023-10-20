import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

NEWEST = (By.XPATH, "./li[1]")
LOW_HIGH = (By.XPATH, "./li[2]")
HIGH_LOW = (By.XPATH, "./li[3]")


class DropdownMenu:
    @allure.step(
        "Init a dropdown menu for offers sorting when offers are displayed in the card format on the My Offers page")
    def __init__(self, node):
        self.node = node

    @allure.step("Get the 'Newest' sorting option when offers are displayed in a card format on the My Offers page")
    def get_newest(self) -> WebElement:
        return self.node.find_element(*NEWEST)

    @allure.step(
        "Get the 'Price low-high' sorting option when offers are displayed in a card format on the My Offers page")
    def get_low_high(self) -> WebElement:
        return self.node.find_element(*LOW_HIGH)

    @allure.step(
        "Get the 'Price high-low' sorting option when offers are displayed in a card format on the My Offers page")
    def get_high_low(self) -> WebElement:
        return self.node.find_element(*HIGH_LOW)

    @allure.step(
        "Click the 'Newest' sorting option to sort offers by last update dates when offers are displayed in a card format on the My Offers page")
    def click_newest(self):
        self.get_newest().click()

    @allure.step(
        "Click the 'Price low-high' sorting option to sort offers by ascending prices when offers are displayed in a card format on the My Offers page")
    def click_low_high(self):
        self.get_low_high().click()

    @allure.step(
        "Click the 'Price high-low' sorting option to sort offers by descending prices when offers are displayed in a card format on the My Offers page")
    def click_high_low(self):
        self.get_high_low().click()
