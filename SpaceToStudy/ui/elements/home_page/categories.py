from selenium.webdriver.common.by import By

MUSIC = (By.XPATH, "./a[1]/div/p")
DESIGN = (By.XPATH, "./a[2]/div/p")
COMPUTER_SCIENCE = (By.XPATH, "./a[3]/div/p")
LANGUAGES = (By.XPATH, "./a[4]/div/p")
MATHEMATICS = (By.XPATH, "./a[5]/div/p")
DANCE = (By.XPATH, "./a[6]/div/p")
MUSIC_OFFERS = (By.XPATH, "./a[1]/div/span")
DESIGN_OFFERS = (By.XPATH, "./a[2]/div/span")
COMPUTER_SCIENCE_OFFERS = (By.XPATH, "./a[3]/div/span")
LANGUAGES_OFFERS = (By.XPATH, "./a[4]/div/span")
MATHEMATICS_OFFERS = (By.XPATH, "./a[5]/div/span")
DANCE_OFFERS = (By.XPATH, "./a[6]/div/span")


class PopularCategories:

    def __init__(self, noda):
        self.noda = noda

    def get_music_category(self):
        return self.noda.find_element(*MUSIC)

    def get_text_music_category(self):
        self.get_music_category().get_attribute("innerHTML")

    def get_design_category(self):
            return self.noda.find_element(*DESIGN)

    def get_text_design_category(self):
            self.get_design_category().get_attribute("innerHTML")

    def get_computer_science_category(self):
        return self.noda.find_element(*COMPUTER_SCIENCE)

    def get_text_computer_science_category(self):
        self.get_computer_science_category().get_attribute("innerHTML")

    def get_languages_category(self):
        return self.noda.find_element(*LANGUAGES)

    def get_text_languages_category(self):
        self.get_languages_category().get_attribute("innerHTML")

    def get_mathematics_category(self):
        return self.noda.find_element(*MATHEMATICS)

    def get_text_mathematics_category(self):
        self.get_mathematics_category().get_attribute("innerHTML")

    def get_dance_category(self):
        return self.noda.find_element(*DANCE)

    def get_text_dance_category(self):
        self.get_dance_category().get_attribute("innerHTML")

    def get_music_offers(self):
        return self.noda.find_element(*MUSIC_OFFERS )

    def get_text_music_offers(self):
        self.get_music_offers().get_attribute("innerHTML")

    def get_design_offers(self):
            return self.noda.find_element(*DESIGN_OFFERS )

    def get_text_design_offers(self):
            self.get_design_offers().get_attribute("innerHTML")

    def get_computer_science_offers(self):
        return self.noda.find_element(*COMPUTER_SCIENCE_OFFERS )

    def get_text_computer_science_offers(self):
        self.get_computer_science_offers().get_attribute("innerHTML")

    def get_languages_offers(self):
        return self.noda.find_element(*LANGUAGES_OFFERS )

    def get_text_languages_offers(self):
        self.get_languages_offers().get_attribute("innerHTML")

    def get_mathematics_offers(self):
        return self.noda.find_element(*MATHEMATICS_OFFERS )

    def get_text_mathematics_offers(self):
        self.get_mathematics_offers().get_attribute("innerHTML")

    def get_dance_offers(self):
        return self.noda.find_element(*DANCE_OFFERS )

    def get_text_dance_offers(self):
        self.get_dance_offers().get_attribute("innerHTML")