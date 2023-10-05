from selenium.webdriver.common.by import By

from SpaceToStudy.ui.pages.base_component import BaseComponent
from SpaceToStudy.ui.elements.input import Input
from SpaceToStudy.ui.elements.checkbox import Checkbox
from SpaceToStudy.ui.elements.button import Button

TITLE = (By.ID, "headingText")
PASSWORD_INPUT = (By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
PASSWORD_LABEL = (By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/div')
PASSWORD_ERROR = (By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[1]/div/form/span/'
                            'section[2]/div/div/div[1]/div[2]/div[2]/span')
SHOW_PASSWORD_CHECKBOX = (By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/'
                                    'div[1]/div[3]/div/div[1]/div/div/div[1]/div')
FORGOT_PASSWORD_BUTTON = (By.XPATH, '//*[@id="forgotPassword"]/div/button')
NEXT_BUTTON = (By.XPATH, '//*[@id="passwordNext"]/div/button')
SELECTED_ACCOUNT_BUTTON = (By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[1]/div/div[2]/div')


class GooglePopUpPasswordInput(BaseComponent):
    def __init__(self, node):
        super().__init__(node)
        self._password_input = None
        self._forgot_password_button = None
        self._next_button = None
        self._selected_account_button = None
        self._show_password_checkbox = None

    def get_title_text(self) -> str:
        return self.node.find_element(*TITLE).text

    def get_password_input(self):
        if not self._password_input:
            node = self.node.find_element(*PASSWORD_INPUT)
            self._password_input = Input(node)
        return self._password_input

    def set_password(self, password):
        password_input = self.get_password_input()
        password_input.set_text(password)
        return self

    def get_password_label_text(self):
        password_label = self.get_password_input()
        return password_label.get_label()

    def get_password_error_message(self):
        password_error_msg = self.get_password_input()
        return password_error_msg.get_error_message()

    def get_show_password_checkbox(self):
        node = self.node.find_element(*SHOW_PASSWORD_CHECKBOX)
        self._show_password_checkbox = Checkbox(node)
        return self._show_password_checkbox

    def click_show_password_checkbox(self):
        self.get_show_password_checkbox().set_check()

    def get_forgot_password_button(self):
        node = self.node.find_element(*FORGOT_PASSWORD_BUTTON)
        self._forgot_password_button = Button(node)
        return self._forgot_password_button

    def click_forgot_password_button(self):
        self.get_forgot_password_button().click_button()

    def get_next_button(self):
        node = self.node.find_element(*NEXT_BUTTON)
        self._next_button = Button(node)
        return self._next_button

    def click_next_button(self):
        self.get_next_button().click_button()

    def get_selected_account_button(self):
        node = self.node.find_element(*SELECTED_ACCOUNT_BUTTON)
        self._selected_account_button = Button(node)
        return self._selected_account_button

    def click_selected_account_button(self):
        self.get_selected_account_button().click_button()
