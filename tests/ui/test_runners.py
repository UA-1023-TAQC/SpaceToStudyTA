import unittest

import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from SpaceToStudy.ui.pages.home_page.home_guest import HomePageGuest
from tests.utils.value_provider import ValueProvider

IMPLICITLY_WAIT = 5


class BaseTestRunner(unittest.TestCase):

    def setUp(self):
        self._init_driver()

    @allure.step("innit web driver")
    def _init_driver(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        self.driver.maximize_window()
        # self.addCleanup(self.driver.quit)
        self.driver.get(ValueProvider.get_base_url())

    def _login(self, email: str, password: str):
        (HomePageGuest(self.driver)
         .get_header()
         .click_login_btn()
         .set_email(email)
         .set_password(password)
         .click_login_button())

    def tearDown(self):
        self.driver.quit()


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
