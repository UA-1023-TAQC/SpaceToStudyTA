from selenium.webdriver.common.by import By

NEWEST = (By.XPATH, "./li[1]")
LOW_HIGH = (By.XPATH, "./li[2]")
HIGH_LOW = (By.XPATH, "./li[3]")


class DropdownMenu:

    def __init__(self, node):
        self.node = node

    def get_newest(self):
        return self.node.find_element(*NEWEST)

    def get_low_high(self):
        return self.node.find_element(*LOW_HIGH)

    def get_high_low(self):
        return self.node.find_element(*HIGH_LOW)

    def click_newest(self):
        self.get_newest().click()

    def click_low_high(self):
        self.get_low_high().click()

    def click_high_low(self):
        self.get_high_low().click()
