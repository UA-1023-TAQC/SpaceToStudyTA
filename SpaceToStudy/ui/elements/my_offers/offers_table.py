from selenium.webdriver.common.by import By

TITLE = (By.XPATH, "./td[1]")
CATEGORY_NAME = (By.XPATH, "./td[2]/div/div[1]/span/p")
SUBJECT = (By.XPATH, "./td[2]/div/div[2]/span/p")
PRICE = (By.XPATH, "./td[3]")
LAST_UPDATE = (By.XPATH, "./td[4]")
STATUS = (By.XPATH, "./td[5]/div/span/p/span[2]")


class OfferElements:
    def __init__(self, node):
        self.node = node

    def get_offer_title(self) -> str:
        return self.node.find_element(*TITLE).text

    def get_offer_category_name(self) -> str:
        return self.node.find_element(*CATEGORY_NAME).text

    def get_offer_subject_name(self) -> str:
        return self.node.find_element(*SUBJECT).text

    def get_offer_price(self) -> str:
        return self.node.find_element(*PRICE).text

    def get_offer_last_update(self) -> str:
        return self.node.find_element(*LAST_UPDATE).text

    def get_offer_status(self) -> str:
        return self.node.find_element(*STATUS).text
