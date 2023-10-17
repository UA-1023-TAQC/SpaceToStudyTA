import allure

from SpaceToStudy.api.auth_client import AuthApiClient
from tests.api.api_test_runners import APITestRunnerWithStudent
from tests.utils.value_provider import ValueProvider


class TestAPIAuth(APITestRunnerWithStudent):
    @allure.testcase('https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/415')
    def test_logout(self):
        user = AuthApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = user.logout()
        self.assertEqual(response.status_code, 204)
