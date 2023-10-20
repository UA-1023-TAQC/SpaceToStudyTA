import allure
from selenium.webdriver import Keys
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.elements.input import Input


class InputDropDownList(Input):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self.default_press_count = 1

    @allure.step("Set {text} text into input element with autofill option")
    def set_text_to_autocomplete_input(self, text, element_locator):
        self.set_text(text)
        self.node.find_element(*element_locator).click()

    @allure.step("User presses a key on the keyboard {press_count} times without releasing it")
    def press_down_button(self, press_count: int):
        self.default_press_count = press_count
        for _ in range(self.default_press_count):
            self.get_input().send_keys(Keys.DOWN)
        return self

    @allure.step("User releases a key {press_count} times from the keyboard")
    def press_up_button(self, press_count: int):
        self.default_press_count = press_count
        self.get_input().click()
        for _ in range(self.default_press_count):
            self.get_input().send_keys(Keys.UP)
        return self

    @allure.step("User presses enter on the keyboard")
    def press_enter_button(self):
        self.get_input().send_keys(Keys.ENTER)
        return self
