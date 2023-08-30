from selenium.webdriver import Keys
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.elements.input import Input


class InputDropDownList(Input):
    def __init__(self, node: WebElement):
        super().__init__(node)

    def press_down_button(self, press_count):
        input_field = self.get_input()
        input_field.click()
        for _ in range(press_count):
            input_field.send_keys(Keys.DOWN)
        return self

    def press_up_button(self, press_count):
        input_field = self.get_input()
        input_field.click()
        for _ in range(press_count):
            input_field.send_keys(Keys.UP)
        return self

    def press_enter_button(self):
        input_field = self.get_input()
        input_field.send_keys(Keys.ENTER)
        return self
