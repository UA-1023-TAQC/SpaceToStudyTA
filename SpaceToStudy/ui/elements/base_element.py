from selenium.webdriver.remote.webelement import WebElement


class BaseElement:
    def __init__(self, node: WebElement):
        self.node = node
