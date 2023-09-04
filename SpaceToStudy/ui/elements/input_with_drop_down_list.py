from selenium.webdriver import Keys
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.elements.input import Input


class InputDropDownList(Input):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self.default_press_count = 1

    def press_down_button(self, press_count: int):
        self.default_press_count = press_count
        for _ in range(self.default_press_count):
            self.get_input().send_keys(Keys.DOWN)
        return self

    def press_up_button(self, press_count: int):
        self.default_press_count = press_count
        self.get_input().click()
        for _ in range(self.default_press_count):
            self.get_input().send_keys(Keys.UP)
        return self

    def press_enter_button(self):
        self.get_input().send_keys(Keys.ENTER)
        return self
