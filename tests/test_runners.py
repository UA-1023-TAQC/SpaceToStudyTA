import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from SpaceToStudy.ui.pages.header.header_unauthorized_component import HeaderUnauthorizedComponent
from SpaceToStudy.ui.pages.login_modal.login_modal import LoginModal
from tests.value_pvider import ValueProvider

IMPLICITLY_WAIT = 5


class BaseTestRunner(unittest.TestCase):

    def setUp(self):
        self._init_driver()

    def _init_driver(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        self.driver.maximize_window()
        self.addCleanup(self.driver.quit)
        self.driver.get(ValueProvider.get_base_url())

    def _login(self, email: str, password: str):
        header = HeaderUnauthorizedComponent(self.driver)
        header.click_login_btn()
        login_modal = LoginModal(self.driver)
        login_modal.set_email_input(email)
        login_modal.set_password_input(password)
        sleep(1)
        login_modal.click_login_button()
        sleep(1)


class TestRunnerWithStudent(BaseTestRunner):
    def setUp(self):
        self._init_driver()
        self._login(ValueProvider.get_student_email(),
                    ValueProvider.get_student_password())


class TestRunnerWithTutor(BaseTestRunner):
    def setUp(self):
        self._init_driver()
        self._login(ValueProvider.get_tutor_email(),
                    ValueProvider.get_tutor_password())
