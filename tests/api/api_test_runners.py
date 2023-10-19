import unittest

from SpaceToStudy.api.auth_client import AuthApiClient
from tests.utils.value_provider import ValueProvider


def get_access_token(email, password):
    client = AuthApiClient(ValueProvider.get_base_api_url())
    client.login(email=email, password=password)
    return client.accessToken


class BaseAPITestRunner(unittest.TestCase):
    accessToken = None


class APITestRunnerWithStudent(BaseAPITestRunner):
    @classmethod
    def setUpClass(cls):
        cls.accessToken = get_access_token(ValueProvider.get_student_email(),
                                           ValueProvider.get_student_password())


class APITestRunnerWithTutor(BaseAPITestRunner):
    @classmethod
    def setUpClass(cls):
        cls.accessToken = get_access_token(ValueProvider.get_tutor_email(),
                                           ValueProvider.get_tutor_password())
