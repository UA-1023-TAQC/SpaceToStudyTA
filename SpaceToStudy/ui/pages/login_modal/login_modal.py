from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.elements.input import Input
from SpaceToStudy.ui.elements.input import PasswordInput
from SpaceToStudy.ui.elements.link import Link
from SpaceToStudy.ui.elements.button import Button
from SpaceToStudy.ui.pages.base_component import BaseComponent


IMG_MODAL = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[1]/img")
TITLE_MODAL = (By.XPATH, "//*[contains(text(),'Welcome back')]")
EMAIL_INPUT = (By.XPATH, "//div[@data-testid='email']")
PASSWORD_INPUT = (By.XPATH, "//label[contains(text(), 'Password')]/..")

FORGOT_PASSWORD_BUTTON = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/form/button[1]")
LOGIN_BUTTON = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/form/button[2]")
SIGN_IN_WITH_GMAIL = (By.XPATH, '//*[@id="googleButton"]/div/iframe')
JOIN_US_FOR_FREE = (By.XPATH, "//*[contains(text(),'Join us for free')]")

UNSUCCESS_LOGIN_POP_UP = (By.XPATH, "?????????????")


class LoginModal(BaseComponent):

    def __init__(self, node):
        super().__init__(node)
        self._img_modal = None
        self._title_modal = None
        self._email_input = None
        self._password_input = None
        self._forgot_password_button = None
        self._sign_in_as_gmail = None
        self._join_us_for_free = None
        self._login_button = None

    def get_img(self):
        if not self._img_modal:
           self._img_modal = self.node.find_element(*IMG_MODAL)
        return self._img_modal

    def get_title(self) -> WebElement:
        if not self._title_modal:
           self._title_modal = self.node.find_element(*TITLE_MODAL)
        return self._title_modal

    def get_title_text(self):
        return self.get_title().text

    def get_email_input(self):
        node = self.node.find_element(*EMAIL_INPUT)
        self._email_input = Input(node)
        return self._email_input

    def set_email(self, email: str):
        self.get_email_input().set_text(email)
        return self

    def get_password_input(self):
        if not self._password_input:
            node = self.node.find_element(*PASSWORD_INPUT)
            self._password_input = PasswordInput(node)
        return self._password_input

    def set_password(self, password: str):
        self.get_password_input().set_text(password)
        return self

    def get_email_error_message(self):
        last_name_input = self.get_last_name_input()
        return last_name_input.get_error_message()
    
    def get_password_error_message(self):
        last_name_input = self.get_last_name_input()
        return last_name_input.get_error_message()

    def get_forgot_password_button(self):
        node = self.node.find_element(*FORGOT_PASSWORD_BUTTON)
        self._forgot_password_button = Button(node)
        return self._forgot_password_button

    def get_login_button(self):
        node = self.node.find_element(*LOGIN_BUTTON)
        self._login_button = Button(node)
        return self._login_button

    def click_login_button(self):
        sleep(0.1)
        self.get_login_button().click_button()
        sleep(1)


    def get_join_us_for_free(self):
        node = self.node.find_element(*JOIN_US_FOR_FREE)
        self._join_us_for_free = Link(node)
        return self._join_us_for_free
    
    def get_sign_in_as_gmail(self):
        if not self._sign_in_as_gmail:
            self._sign_in_as_gmail = self.node.find_element(*SIGN_IN_WITH_GMAIL)
        return self._sign_in_as_gmail
    
    def click_sign_in_as_gmail(self):
        self.get_sign_in_as_gmail().click()

    def outside_click(self):
        modal_element = self.node.find_element(By.XPATH, "/html/body/div[2]/div[3]/div")
        modal_location = modal_element.location

        x = modal_location['x'] - 10
        y = modal_location['y'] - 10

        actions = ActionChains(self.node.parent)
        actions.move_by_offset(x, y).click().perform()
        return
