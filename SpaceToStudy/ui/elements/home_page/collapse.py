from selenium.webdriver.common.by import By


FLEXIBLE_LOCATION = (By.XPATH, "./div[1]")
INDIVIDUAL_TIME = (By.XPATH, "./div[2]")
FREE_CHOICE_OF_TUTOR = (By.XPATH, "./div[3]")
DIGITAL_COMMUNICATION = (By.XPATH, "./div[4]")


class CollapseBlock:

    def __init__(self, noda):
        self.noda = noda

    def open_flexible_location(self):
        return self.noda.find_element(*FLEXIBLE_LOCATION)

    def click_open_flexible_location(self):
        self.open_flexible_location().click()

    def open_individual_time(self):
        return self.noda.find_element(*INDIVIDUAL_TIME)

    def click_open_individual_time(self):
        self.open_individual_time().click()

    def open_free_choice_of_tutors(self):
        return self.noda.find_element(*FREE_CHOICE_OF_TUTOR)

    def click_open_free_choice_of_tutors(self):
        self.open_free_choice_of_tutors().click()

    def open_digital_communication(self):
        return self.noda.open_digital_communication(*DIGITAL_COMMUNICATION)

    def click_open_digital_communication(self):
        self.open_digital_communication().click()

