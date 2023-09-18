from selenium.webdriver.common.by import By

from SpaceToStudy.ui.pages.base_component import BaseComponent
from SpaceToStudy.ui.elements.input import Input
from SpaceToStudy.ui.elements.button import Button


TITLE = (By.ID, "headingText")
SUBTITLE = (By.ID, "headingSubtext")
EMAIL_INPUT = ()
EMAIL_LABEL = (By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[1]/div/form/'
                         'span/section/div/div/div[1]/div/div[1]/div/div[1]/div')
EMAIL_ERROR = (By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div'
                         '/div[2]')
FORGOT_EMAIL_BUTTON = (By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[1]/'
                                 'div/form/span/section/div/div/div[3]/button')
CREATE_ACCOUNT_BUTTON = (By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div/button')
NEXT_BUTTON = (By.XPATH, '//*[@id="identifierNext"]/div/button')
#SWITHER FOR LANG


class GooglePopUpEmailInput(BaseComponent):
    def __init__(self, node):
        super().__init__(node)
        self._email_input = None
        self._forgot_email_button = None
        self._create_account_button = None
        self._next_button = None

    def get_title_text(self) -> str:
        return self.node.find_element(*TITLE).text

    def get_subtitle_text(self) -> str:
        return self.node.find_element(*SUBTITLE).text

    def get_email_input(self):
        if not self._email_input:
            node = self.node.find_element(*EMAIL_INPUT)
            self._email_input = Input(node)
        return self._email_input

    def set_email(self, email_text):
        email_input = self.get_email_input()
        email_input.set_text(email_text)
        return self

    def get_email_label_text(self):
        email_label = self.get_email_input()
        return email_label.get_label()

    def get_email_error_message(self):
        email_error = self.get_email_input()
        return email_error.get_error_message()

    def get_forgot_email_button(self):
        node = self.node.find_element(*FORGOT_EMAIL_BUTTON)
        self._forgot_email_button = Button(node)
        return self._forgot_email_button

    def click_forgot_email_button(self):
        self.get_forgot_email_button().click_button()
        # return page

    def get_create_account_button(self):
        node = self.node.find_element(*CREATE_ACCOUNT_BUTTON)
        self._create_account_button = Button(node)
        return self._create_account_button

    def click_create_account_button(self):
        self.get_create_account_button().click_button()
        #return page

    def get_next_button(self):
        node = self.node.find_element(*NEXT_BUTTON)
        self._next_button = Button(node)
        return self._next_button

    def click_next_button(self):
        self.get_next_button().click_button()
        #return page





