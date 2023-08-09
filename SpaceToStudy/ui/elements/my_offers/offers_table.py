from selenium.webdriver.common.by import By

TITLE = (By.XPATH, "./td[1]")
CATEGORY_NAME = (By.XPATH, "./td[2]/div/div[1]/span/p")
SUBJECT = (By.XPATH, "./td[2]/div/div[2]/span/p")
PRICE = (By.XPATH, "./td[3]")
LAST_UPDATE = (By.XPATH, "./td[4]")
STATUS = (By.XPATH, "./td[5]/div/span/p/span[2]")


class OfferElements:
    def __init__(self, noda):
        self.noda = noda

    def get_offer_title(self):
        return self.noda.find_element(*TITLE).text

    def get_offer_category_name(self):
        return self.noda.find_element(*CATEGORY_NAME).text

    def get_offer_subject_name(self):
        return self.noda.find_element(*SUBJECT).text

    def get_offer_price(self):
        return self.noda.find_element(*PRICE).text

    def get_offer_last_update(self):
        return self.noda.find_element(*LAST_UPDATE).text

    def get_offer_status(self):
        return self.noda.find_element(*STATUS).text
