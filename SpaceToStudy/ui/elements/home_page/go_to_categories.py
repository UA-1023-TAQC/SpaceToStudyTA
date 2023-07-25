from selenium.webdriver.common.by import By

CATEGORIES_BUTTON = (By.XPATH, "./span")


class CategoriesBtn:

    def __init__(self, noda):
        self.noda = noda

    def go_to_categories_btn(self):
        return self.noda.find_element(*CATEGORIES_BUTTON)

    def click_go_to_categories_btn(self):
        self.go_to_categories_btn().click()