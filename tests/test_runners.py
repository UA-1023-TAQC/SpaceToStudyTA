import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

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
        pass


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
