from selenium.webdriver.remote.webelement import WebElement


class BaseComponent:
    def __init__(self, node: WebElement):
        self.node = node
