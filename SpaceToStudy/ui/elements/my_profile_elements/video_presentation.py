from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

TITLE = (By.XPATH, "./p")
TITLE_BAR = (By.XPATH, "./div/img")
VIDEO = (By.XPATH, "./div/div/img")

class VideoPresentation:
    def __init__(self, node):
        self.node = node

    def get_title_text(self) -> str:
        return self.node.find_element(*TITLE).text

    def get_title_bar(self) -> WebElement:
        return self.node.find_element(*TITLE_BAR)

    def get_video(self) -> WebElement:
        """
        While documenting the test procedure, it's important to note that during the testing phase,
        the developer employed image elements instead of video elements.
        :return: WebElement
        """
        return self.node.find_element(*VIDEO)



