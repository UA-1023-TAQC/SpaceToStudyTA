from selenium.webdriver.common.by import By

ALL_BTN = (By.XPATH, "./button[1]")
ACTIVE_BTN = (By.XPATH, "./button[2]")
DRAFT_BTN = (By.XPATH, "./button[3]")
CLOSED_BTN = (By.XPATH, "./button[4]")


class SelectOffers:
    def __init__(self, node):
        self.node = node

    def get_all_btn(self):
        return self.node.find_element(*ALL_BTN)

    def get_active_btn(self):
        return self.node.find_element(*ACTIVE_BTN)

    def get_draft_btn(self):
        return self.node.find_element(*DRAFT_BTN)

    def get_closed_btn(self):
        return self.node.find_element(*CLOSED_BTN)

    def click_all_btn(self):
        self.get_all_btn().click()

    def click_active_btn(self):
        self.get_active_btn().click()

    def click_draft_btn(self):
        self.get_draft_btn().click()

    def click_closed_btn(self):
        self.get_closed_btn().click()
