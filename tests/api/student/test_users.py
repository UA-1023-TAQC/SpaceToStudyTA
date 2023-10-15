import allure
from jsonschema import validate

from SpaceToStudy.api.users.client import UsersApiClient
from SpaceToStudy.api.users.schemas import SCHEMA_FOR_ALL_USERS
from tests.api.api_test_runners import APITestRunnerWithStudent
from tests.utils.value_provider import ValueProvider


class TestAPIUsers(APITestRunnerWithStudent):

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/402",
                     "Create test for api/users find all users")
    def test_find_all_users(self):
        client = UsersApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_users()
        self.assertEqual(response.status_code, 200)
        validate(instance=response.json(), schema=SCHEMA_FOR_ALL_USERS)
