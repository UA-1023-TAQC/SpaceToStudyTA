import allure
from jsonschema import validate

from SpaceToStudy.api.users.client import UsersApiClient
from SpaceToStudy.api.users.schemas import SCHEMA_FOR_ALL_USERS
from SpaceToStudy.api.schema_for_errors import SCHEMA_FOR_ERRORS
from tests.api.api_test_runners import APITestRunnerWithStudent
from tests.utils.value_provider import ValueProvider


class TestAPIUsers(APITestRunnerWithStudent):

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/402",
                     "Create test for api/users find all users")
    def test_find_all_users(self):
        expected_status_code = 200
        client = UsersApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_users()
        self.assertEqual(expected_status_code, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_ALL_USERS)

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/402",
                     "Create test for api/users find all users")
    def test_find_all_users_unauthorized(self):
        expected_status_code = 401
        expected_code = "UNAUTHORIZED"
        expected_message = "The requested URL requires user authorization."
        client = UsersApiClient(ValueProvider.get_base_api_url())
        response = client.get_users()
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_code, response.json().get('code'))
        self.assertEqual(expected_message, response.json().get('message'))
        validate(instance=response.json(), schema=SCHEMA_FOR_ERRORS)
