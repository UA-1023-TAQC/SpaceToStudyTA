from selenium.webdriver.common.by import By

INPUT = (By.XPATH, "./div/div/input")
FIND_TUTOR_BTN = (By.XPATH, "./a")


class SearchTutor:
    def __init__(self, node):
        self.node = node

    def get_input(self):
        return self.node.find_element(*INPUT)

    def set_text(self, text):
        self.get_input().send_keys(text)

    def find_tutor_btn(self):
        return self.node.find_element(*FIND_TUTOR_BTN)

    def click_find_tutor_btn(self):
        self.find_tutor_btn().click()