from selenium.webdriver.common.by import By

from SpaceToStudy.ui.elements.input import Input
from SpaceToStudy.ui.pages.base_page import BasePage

FIRST_NAME_INPUT = (By.ID, "mui-7")
LAST_NAME_INPUT = (By.ID, "mui-8")
EMAIL_INPUT = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/form/div[2]/div")
PASSWORD_INPUT = (By.ID, "mui-10")
CONFIRM_PASSWORD_INPUT = (By.ID, "mui-11")

FIRST_NAME_LABEL = (By.ID, "//*[@id='mui-10-label']")
LAST_NAME_LABEL = (By.ID, "//*[@id='mui-11-label']")
EMAIL_LABEL = (By.XPATH, "//*[@id='mui-12-label']")
PASSWORD_LABEL = (By.ID, "//*[@id='mui-13-label']")
CONFIRM_PASSWORD_LABEL = (By.XPATH, "//*[@id='mui-14-label']")

FIRST_NAME_ERROR = (By.XPATH, "//*[@id='mui-10-helper-text']/span")
LAST_NAME_ERROR = (By.XPATH, "//*[@id='mui-11-helper-text']/span")
EMAIL_ERROR = (By.XPATH, "//*[@id='mui-12-helper-text']/span")
PASSWORD_ERROR = (By.XPATH, "//*[@id='mui-13-helper-text']/span")
CONFIRM_PASSWORD_ERROR = (By.XPATH, "//*[@id='mui-14-helper-text']/span")

I_AGREE_CHECKBOX = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/form/div[5]/label/span[1]/input")
SIGN_UP_BTN = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/form/button")

TERMS_LINK = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/form/div[5]/label/span[2]/div/a[1]")
PRIVACY_POLICY_LINK = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/form/div[5]/label/span[2]/div/a[2]")
LOGIN = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/div/div[3]/p[2]")


class RegistrationModal(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._first_name_input = None
        self._last_name_input = None
        self._email_input = None
        self._password_input = None
        self._confirm_password_input = None
        self._terms = None
        self._privacy_policy = None

    def get_first_name_input(self):
        if not self._first_name_input:
            node = self.driver.find_element(*FIRST_NAME_INPUT)
            self._first_name_input = Input(node)
        return self._first_name_input

    def set_first_name(self, first_name_text):
        first_name_input = self.get_first_name_input()
        first_name_input.set_text(first_name_text)

    def get_first_name_label_text(self):
        first_name_input = self.get_first_name_input()
        return first_name_input.get_label()

    def get_first_name_error_message(self):
        first_name_input = self.get_first_name_input()
        return first_name_input.get_error_message()

    def get_last_name_input(self):
        if not self._last_name_input:
            node = self.driver.find_element(*LAST_NAME_INPUT)
            self._last_name_input = Input(node)
        return self._last_name_input

    def set_last_name(self, last_name_text):
        last_name_input = self.get_last_name_input()
        last_name_input.set_text(last_name_text)

    def get_last_name_label_text(self):
        last_name_input = self.get_last_name_input()
        return last_name_input.get_label()

    def get_last_name_error_message(self):
        last_name_input = self.get_last_name_input()
        return last_name_input.get_error_message()

    def get_email_input(self):
        if not self._email_input:
            node = self.driver.find_element(*EMAIL_INPUT)
            self._email_input = Input(node)
        return self._email_input

    def set_email(self, email_text):
        email_input = self.get_email_input()
        email_input.set_text(email_text)

    def get_email_label_text(self):
        email_input = self.get_email_input()
        return email_input.get_label()

    def get_email_error_message(self):
        email_input = self.get_email_input()
        return email_input.get_error_message()

    def get_password_input(self):
        if not self._password_input:
            node = self.driver.find_element(*PASSWORD_INPUT)
            self._password_input = Input(node)
        return self._password_input

    def get_confirm_password_input(self):
        if not self._confirm_password_input:
            node = self.driver.find_element(*CONFIRM_PASSWORD_INPUT)
            self._confirm_password_input = Input(node)
        return self._confirm_password_input

    def get_i_agree_checkbox(self):
        return self.driver.find_element(*I_AGREE_CHECKBOX)

    def click_i_agree_checkbox(self):
        self.driver.get_i_agree_checkbox.click()

    def get_sign_up_btn(self):
        return self.driver.find_element(*SIGN_UP_BTN)

    def click_sign_up_btn(self):
        self.driver.get_sign_up_btn.click()