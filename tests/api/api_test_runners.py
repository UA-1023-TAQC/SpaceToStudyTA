import unittest
import requests

from SpaceToStudy.api.auth_client import AuthApiClient
from tests.utils.value_provider import ValueProvider


class BaseAPITestRunner(unittest.TestCase):
    def setUp(self):
        self.api = AuthApiClient(ValueProvider.get_base_api_url())
        self.accessToken = None

    def get_response_json(self, url):
        response = requests.get(url, headers={"Authorization": f"Bearer {self.accessToken}"})
        return response.json()


class APITestRunnerWithStudent(BaseAPITestRunner):
    def setUp(self):
        api = AuthApiClient(ValueProvider.get_base_api_url())
        api.login(ValueProvider.get_student_email(),
                  ValueProvider.get_student_password())
        self.accessToken = api.accessToken


class APITestRunnerWithTutor(BaseAPITestRunner):
    def setUp(self):
        api = AuthApiClient(ValueProvider.get_base_api_url())
        api.login(ValueProvider.get_tutor_email(),
                  ValueProvider.get_tutor_password())
        self.accessToken = api.accessToken
