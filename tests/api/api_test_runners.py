import unittest

from SpaceToStudy.api.auth_client import AuthApiClient
from tests.utils.value_provider import ValueProvider


class BaseAPITestRunner(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.accessToken = None


class APITestRunnerWithStudent(BaseAPITestRunner):
    @classmethod
    def setUpClass(cls):
        api = AuthApiClient(ValueProvider.get_base_api_url())
        api.login(ValueProvider.get_student_email(),
                  ValueProvider.get_student_password())
        cls.accessToken = api.accessToken


class APITestRunnerWithTutor(BaseAPITestRunner):
    @classmethod
    def setUpClass(cls):
        api = AuthApiClient(ValueProvider.get_base_api_url())
        api.login(ValueProvider.get_tutor_email(),
                  ValueProvider.get_tutor_password())
        cls.accessToken = api.accessToken
