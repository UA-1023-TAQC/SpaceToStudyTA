from selenium.webdriver.common.by import By


AVATAR = (By.XPATH, "./div[1]/div[1]/div")
NAME_SURNAME = (By.XPATH, "./div[1]/div[2]/div[1]/p")
DAYS_IN_SPASE_TO_STADY = (By.XPATH, "./div[1]/div[2]/div[3]/div[1]/p")

class ProfileInfo:
    def __init__(self, noda):
        self.noda = noda

    def get_avatar(self):
        return self.noda.find_element(*AVATAR)

    def get_name_surname_text(self):
        return self.noda.find_element(*NAME_SURNAME).text

    def get_days_in_spase2study_text(self):
         return self.noda.find_element(*DAYS_IN_SPASE_TO_STADY).text
