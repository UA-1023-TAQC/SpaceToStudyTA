from selenium.webdriver.common.by import By

FIND_TUTOR_BUTTON = (By.XPATH, "./span")


class FindTutorButton:

    def __init__(self, noda):
        self.noda = noda

    def find_tutor_button(self):
        return self.noda.find_element(*FIND_TUTOR_BUTTON)

    def click_find_tutor_button(self):
        self.find_tutor_button().click()
