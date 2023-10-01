import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.elements.checkbox import Checkbox
from SpaceToStudy.ui.elements.input import Input
from SpaceToStudy.ui.elements.input_with_image import InputWithImage
from SpaceToStudy.ui.elements.link import Link
from SpaceToStudy.ui.pages.base_component import BaseComponent
from SpaceToStudy.ui.pages.login_modal.login_modal import LoginModal
from SpaceToStudy.ui.pages.sign_up_modal.please_confirm_modal import PleaseConfirm

CLOSE_BTN = (By.XPATH, "/html/body/div[2]/div[3]/div/div/button")
PLEASE_CONFIRM = (By.XPATH, "/html/body/div[3]/div[3]/div")

TITLE = (By.XPATH, "//h2")
FIRST_NAME_INPUT = (By.XPATH, "//label[contains(text(), 'First name')]/..")
LAST_NAME_INPUT = (By.XPATH, "//label[contains(text(), 'Last name')]/..")
EMAIL_INPUT = (By.XPATH, "//label[contains(text(), 'Email')]/..")
PASSWORD_INPUT = (By.XPATH, "//label[contains(text(), 'Password')]/..")
CONFIRM_PASSWORD_INPUT = (By.XPATH, "//label[contains(text(), 'Confirm password')]/..")

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

I_AGREE_CHECKBOX = (By.XPATH, "//form//input[@type='checkbox']/..")
SIGN_UP_BTN = (By.XPATH, "//button[contains(text(), 'Sign up')]")
OR_CONTINUE_TEXT = (By.XPATH, "//div[@data-testid='popupContent']//p[contains(text(), 'or continue')]")
SIGN_UP_WITH_GOOGLE_IFRAME = (By.XPATH, "//div[@id='googleButton']//iframe")
SIGN_UP_WITH_GOOGLE_BTN = (By.XPATH, "//span[text()='Sign up with Google']")
ALREADY_HAVE_ACCOUNT_TEXT = (By.XPATH, "//p[text()='Already have a Space2Study account?']")

TERMS_LINK = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/form/div[5]/label/span[2]/div/a[1]")
PRIVACY_POLICY_LINK = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/form/div[5]/label/span[2]"
                                 "/div/a[2]")
LOGIN_LINK = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/div/div[3]/p[2]")
LOGIN_MODAL = (By.XPATH, "//*[@role='dialog']")

TITLE_MODAL = (By.XPATH, "//h2")



class RegistrationModal(BaseComponent):

    def __init__(self, node):
        super().__init__(node)
        self._login_link = None
        self._first_name_input = None
        self._last_name_input = None
        self._email_input = None
        self._password_input = None
        self._confirm_password_input = None
        self._i_agree_checkbox = None
        self._terms_link = None
        self._privacy_policy_link = None
        self._title_modal = None
        self._title = None
        self._please_confirm = None

    @allure.step("Get close btn")
    def get_close_btn(self):
        return self.node.find_element(*CLOSE_BTN)

    @allure.step("Click close btn")
    def click_close_btn(self):
        from SpaceToStudy.ui.pages.home_page.home_guest import HomePageGuest
        self.get_close_btn().click()
        return HomePageGuest(self.node.parent)

    @allure.step("Get please confirm")
    def get_please_confirm(self):
        self.get_close_btn().click()
        if not self._please_confirm:
            node = self.node.find_element(*PLEASE_CONFIRM)
            self._please_confirm = PleaseConfirm(node)
        return self._please_confirm

    def get_title_text(self) -> str:
        return self.node.find_element(*TITLE).text

    @allure.step("Get text login link")
    def get_title(self) -> WebElement:
        if not self._title_modal:
            self._title_modal = self.node.find_element(*TITLE_MODAL)
        return self._title_modal

    @allure.step("Get title modal text")
    def get_title_text(self) -> str:
        return self.get_title().text

    @allure.step("Get first name input")
    def get_first_name_input(self):
        if not self._first_name_input:
            node = self.node.find_element(*FIRST_NAME_INPUT)
            self._first_name_input = Input(node)
        return self._first_name_input

    @allure.step("Set {first_name_text} first name")
    def set_first_name(self, first_name_text):
        first_name_input = self.get_first_name_input()
        first_name_input.set_text(first_name_text)
        return self

    @allure.step("Get first name label text")
    def get_first_name_label_text(self):
        first_name_input = self.get_first_name_input()
        return first_name_input.get_label()

    @allure.step("Get first name error message")
    def get_first_name_error_message(self):
        first_name_input = self.get_first_name_input()
        return first_name_input.get_error_message()

    @allure.step("Get last name input")
    def get_last_name_input(self):
        if not self._last_name_input:
            node = self.node.find_element(*LAST_NAME_INPUT)
            self._last_name_input = Input(node)
        return self._last_name_input

    @allure.step("Set {last_name_text}last name input")
    def set_last_name(self, last_name_text):
        last_name_input = self.get_last_name_input()
        last_name_input.set_text(last_name_text)
        return self

    @allure.step("Get Last name label text")
    def get_last_name_label_text(self):
        last_name_input = self.get_last_name_input()
        return last_name_input.get_label()

    @allure.step("Get last name error message")
    def get_last_name_error_message(self):
        last_name_input = self.get_last_name_input()
        return last_name_input.get_error_message()

    @allure.step("Get email input")
    def get_email_input(self):
        if not self._email_input:
            node = self.node.find_element(*EMAIL_INPUT)
            self._email_input = Input(node)
        return self._email_input

    @allure.step("Set {email_text} email input")
    def set_email(self, email_text):
        email_input = self.get_email_input()
        email_input.set_text(email_text)
        return self

    @allure.step("Get email label text")
    def get_email_label_text(self):
        email_input = self.get_email_input()
        return email_input.get_label()

    @allure.step("Get email error message")
    def get_email_error_message(self):
        email_input = self.get_email_input()
        return email_input.get_error_message()

    @allure.step("Get password input")
    def get_password_input(self):
        if not self._password_input:
            node = self.node.find_element(*PASSWORD_INPUT)
            self._password_input = InputWithImage(node)
        return self._password_input

    @allure.step("Set {password_text} password input")
    def set_password(self, password_text):
        password_input = self.get_password_input()
        password_input.set_text(password_text)
        return self

    @allure.step("Get password label text")
    def get_password_label_text(self):
        password_input = self.get_password_input()
        return password_input.get_label()

    @allure.step("Get password error message")
    def get_password_error_message(self) -> str:
        password_input = self.get_password_input()
        return password_input.get_error_message()

    @allure.step("Click password icon")
    def click_password_icon(self):
        password_input = self.get_password_input()
        password_input.click_icon()
        return self

    @allure.step("Get confirm password input")
    def get_confirm_password_input(self):
        if not self._confirm_password_input:
            node = self.node.find_element(*CONFIRM_PASSWORD_INPUT)
            self._confirm_password_input = InputWithImage(node)
        return self._confirm_password_input

    @allure.step("Set {confirm_password_text} confirm password")
    def set_confirm_password(self, confirm_password_text):
        confirm_password_input = self.get_confirm_password_input()
        confirm_password_input.set_text(confirm_password_text)
        return self

    @allure.step("Get confirm password label text")
    def get_confirm_password_label_text(self):
        confirm_password_input = self.get_confirm_password_input()
        return confirm_password_input.get_label()

    @allure.step("Get confirm password error message")
    def get_confirm_password_error_message(self):
        confirm_password_input = self.get_confirm_password_input()
        return confirm_password_input.get_error_message()

    @allure.step("Click confirm password icon")
    def click_confirm_password_icon(self):
        confirm_password_input = self.get_confirm_password_input()
        confirm_password_input.get_icon()
        return self

    @allure.step("Get I agree checkbox")
    def get_i_agree_checkbox(self):
        node = self.node.find_element(*I_AGREE_CHECKBOX)
        self._i_agree_checkbox = Checkbox(node)
        return self._i_agree_checkbox

    @allure.step("Click I agree checkbox")
    def click_i_agree_checkbox(self):
        self.get_i_agree_checkbox().set_check()
        return self

    @allure.step("Get terms link")
    def get_terms_link(self):
        if not self._terms_link:
            node = self.node.find_element(*TERMS_LINK)
            self._terms_link = Link(node)
        return self._terms_link

    @allure.step("Get terms link text")
    def get_terms_link_text(self):
        terms_link_text = self.get_terms_link()
        return terms_link_text.get_link_text()

    @allure.step("Click terms link")
    def click_terms_link(self):
        terms_link = self.get_terms_link()
        terms_link.click_link()
        # ToDo

    @allure.step("Get privacy policy link")
    def get_privacy_policy_link(self):
        if not self._privacy_policy_link:
            node = self.node.find_element(*PRIVACY_POLICY_LINK)
            self._privacy_policy_link = Link(node)
        return self._privacy_policy_link

    @allure.step("Get text privacy policy link")
    def get_privacy_policy_link_text(self):
        privacy_policy_link_text = self.get_privacy_policy_link()
        return privacy_policy_link_text.get_link_text()

    @allure.step("Click privacy policy link")
    def click_privacy_policy_link(self):
        privacy_policy_link = self.get_privacy_policy_link()
        privacy_policy_link.click_link()
        # ToDo return page privacy policy

    @allure.step("Get sign up btn")
    def get_sign_up_btn(self):
        return self.node.find_element(*SIGN_UP_BTN)

    @allure.step("Click sign up btn")
    def click_sign_up_btn(self):
        sign_up_btn = self.get_sign_up_btn()
        sign_up_btn.click()

    @allure.step("Get 'or continue' text")
    def get_or_continue_text(self):
        return self.node.find_element(*OR_CONTINUE_TEXT)

    @allure.step("Get 'Sign up with Google' iframe")
    def get_sign_up_with_google_iframe(self):
        return self.node.find_element(*SIGN_UP_WITH_GOOGLE_IFRAME)

    @allure.step("Get 'Sign up with Google' button text")
    def get_sign_up_with_google_btn_text(self) -> str:
        iframe = self.get_sign_up_with_google_iframe()
        self.node.parent.switch_to.frame(iframe)
        button_text = self.node.parent.find_element(*SIGN_UP_WITH_GOOGLE_BTN).text
        self.node.parent.switch_to.default_content()
        return button_text

    @allure.step("Get 'Already have account' text")
    def get_already_have_account_text(self):
        return self.node.find_element(*ALREADY_HAVE_ACCOUNT_TEXT)

    def get_title_text(self) -> WebElement:
        if not self._title:
            self._title = self.node.find_element(*TITLE)
        return self._title.text

    @allure.step("Get login link")
    def get_login_link(self) -> WebElement:
        if not self._login_link:
            self._login_link = self.node.find_element(*LOGIN_LINK)
        return self._login_link

    @allure.step("Get text login link")
    def get_login_link_text(self) -> str:
        return self.get_login_link().text

    @allure.step("Click login link")
    def click_login_link(self):
        login_link = self.get_login_link()
        login_link.click()
        node = self.node.parent.find_element(*LOGIN_MODAL)
        return LoginModal(node)

    @allure.step("Is displayed element")
    def is_displayed(self) -> bool:
        return self.node.is_displayed()
