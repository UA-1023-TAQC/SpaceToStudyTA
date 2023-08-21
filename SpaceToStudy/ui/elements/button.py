from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.elements.base_element import BaseElement

BUTTON = (By.XPATH, "./button")
LABEL = (By.XPATH, "./label")


class Button(BaseElement):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self._button = None
        self._label = None
        self._button_css_class = None

    def get_button(self):
        if not self._button:
            self._button = self.node.find_element(*BUTTON)
        return self._button

    def get_label(self):
        if not self._label:
            self._label = self.node.find_element(*LABEL)
        return self._label.text
    
    def get_button_css_class(self):
        if self._button:
            self._button_css_class = self._button.get_attribute("class")
        return self._button_css_class
    
    def click_button(self):
        self.get_button().click()
        

    

    
    
