from selenium.webdriver.remote.webelement import WebElement


class BaseElement:
    def __init__(self, link, node: WebElement):
        self.node = node
