import allure
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
from SpaceToStudy.ui.pages.first_login_student_modal.first_login_modal import FirstLoginModal


IMG_MODAL = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[1]/img")
TITLE_MODAL = (By.XPATH, "//*[contains(text(),'Welcome back')]")
EMAIL_INPUT = (By.XPATH, "//div[@data-testid='email']")
PASSWORD_INPUT = (By.XPATH, "//label[contains(text(), 'Password')]/..")

FORGOT_PASSWORD_BUTTON = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/form/button[1]")
LOGIN_BUTTON = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/form/button[2]")
SIGN_IN_WITH_GMAIL = (By.XPATH, '//*[@id="googleButton"]/div/div/div/div[2]/span[1]')
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

    @allure.step("Get the image from the modal window")
    def get_img(self):
        if not self._img_modal:
            self._img_modal = self.node.find_element(*IMG_MODAL)
        return self._img_modal

    @allure.step("Get the title of the modal window")
    def get_title(self) -> WebElement:
        if not self._title_modal:
            self._title_modal = self.node.find_element(*TITLE_MODAL)
        return self._title_modal

    @allure.step("Get the text of the title of the modal window")
    def get_title_text(self):
        return self.get_title().text

    @allure.step("Get the email input field")
    def get_email_input(self):
        node = self.node.find_element(*EMAIL_INPUT)
        self._email_input = Input(node)
        return self._email_input

    @allure.step("The email input field is set to the value: {email}")
    def set_email(self, email: str):
        self.node.parent.implicitly_wait(1)
        self.get_email_input().set_text(email)
        return self

    @allure.step("Get the password input field")
    def get_password_input(self):
        if not self._password_input:
            node = self.node.find_element(*PASSWORD_INPUT)
            self._password_input = PasswordInput(node)
        return self._password_input

    @allure.step("The password input field is set to the value: {password}")
    def set_password(self, password: str):
        self.get_password_input().set_text(password)
        return self

    @allure.step("Get the email error message")
    def get_email_error_message(self):
        last_name_input = self.get_last_name_input()
        return last_name_input.get_error_message()

    @allure.step("Get the password error message")
    def get_password_error_message(self):
        last_name_input = self.get_last_name_input()
        return last_name_input.get_error_message()

    @allure.step("Get the 'Forgot Password' button")
    def get_forgot_password_button(self):
        node = self.node.find_element(*FORGOT_PASSWORD_BUTTON)
        self._forgot_password_button = Button(node)
        return self._forgot_password_button

    @allure.step("Get the 'Login' button")
    def get_login_button(self):
        node = self.node.find_element(*LOGIN_BUTTON)
        self._login_button = Button(node)
        return self._login_button

    @allure.step("Click the 'Login' button")
    def click_login_button(self):
        from SpaceToStudy.ui.pages.home_page.home_student import HomePageStudent
        from SpaceToStudy.ui.pages.home_page.home_tutor import HomePageTutor
        sleep(0.5)
        self.get_login_button().click_button()
        sleep(1)
        if FirstLoginModal(self.node.parent).get_general_step().is_displayed():
            return FirstLoginModal(self.node.parent)
        elif HomePageStudent(self.node.parent).get_text_button_find_tutor() == "Find tutor":
            return HomePageStudent(self.node.parent)
        else:
            return HomePageTutor(self.node.parent)

    @allure.step("Get the 'Join Us for Free' link")
    def get_join_us_for_free(self):
        node = self.node.find_element(*JOIN_US_FOR_FREE)
        self._join_us_for_free = Link(node)
        return self._join_us_for_free

    @allure.step("Get the 'Sign In with Gmail' button")
    def get_sign_in_as_gmail(self):
        if not self._sign_in_as_gmail:
            self._sign_in_as_gmail = self.node.find_element(*SIGN_IN_WITH_GMAIL)
        return self._sign_in_as_gmail

    @allure.step("Click the 'Sign In with Gmail' button")
    def click_sign_in_as_gmail(self):
        self.get_sign_in_as_gmail().click()

    @allure.step("Perform an outside click to dismiss the modal window")
    def outside_click(self):
        modal_element = self.node.find_element(By.XPATH, "/html/body/div[2]/div[3]/div")
        modal_location = modal_element.location

        x = modal_location['x'] - 10
        y = modal_location['y'] - 10

        actions = ActionChains(self.node.parent)
        actions.move_by_offset(x, y).click().perform()
        return
