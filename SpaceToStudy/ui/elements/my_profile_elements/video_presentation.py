from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

#/html/body/div/div/div[2]/div[2]/div[3]
#/html/body/div/div/div[2]/div[2]/div[3]
TITLE = (By.XPATH, "./p")
TITLE_BAR = (By.XPATH, "./div/img")
VIDEO = (By.XPATH, "./div/div/img")

class VideoPresentation:
    def __init__(self, noda):
        self.noda = noda

    def get_title_text(self) -> str:
        return self.noda.find_element(*TITLE).text

    def get_title_bar(self) -> WebElement:
        return self.noda.find_element(*TITLE_BAR)

    def get_video(self) -> WebElement:
        """
        At the time of writing the test dev use img, not video
        :return: WebElement img
        """
        return self.noda.find_element(*VIDEO)



