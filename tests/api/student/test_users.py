import allure
from jsonschema import validate

from SpaceToStudy.api.users.client import UsersApiClient
from SpaceToStudy.api.users.schemas import SCHEMA_FOR_ALL_USERS, SCHEMA_FOR_USER
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

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/404",
                     "Create test for api/users Find user by ID ")
    def test_find_user_by_id(self):
        expected_status_code = 200
        user_id_tutor = "644f6f1777e2551b87786650"
        user_id_student = "650023e50eeb49de31750c84"

        client = UsersApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_users_by_id(user_id_tutor)
        self.assertEqual(expected_status_code, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_USER)

        response = client.get_users_by_id(user_id_tutor, "tutor")
        self.assertEqual(expected_status_code, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_USER)

        response = client.get_users_by_id(user_id_student, "student")
        self.assertEqual(expected_status_code, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_USER)

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/404",
                     "Create test for api/users Find user by ID ")
    def test_find_user_by_id_invalid_id(self):
        expected_status_code = 400
        expected_code = "INVALID_ID"
        expected_message = "ID is invalid."
        user_id = "abcdefg"

        client = UsersApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_users_by_id(user_id)
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_code, response.json().get('code'))
        self.assertEqual(expected_message, response.json().get('message'))
        validate(instance=response.json(), schema=SCHEMA_FOR_ERRORS)

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/404",
                     "Create test for api/users Find user by ID ")
    def test_find_user_by_id_unauthorized(self):
        expected_status_code = 401
        expected_code = "UNAUTHORIZED"
        expected_message = "The requested URL requires user authorization."
        user_id = "644f6f1777e2551b87786650"

        client = UsersApiClient(ValueProvider.get_base_api_url())
        response = client.get_users_by_id(user_id)
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_code, response.json().get('code'))
        self.assertEqual(expected_message, response.json().get('message'))
        validate(instance=response.json(), schema=SCHEMA_FOR_ERRORS)

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/404",
                     "Create test for api/users Find user by ID ")
    def test_find_user_by_id_not_found_id(self):
        expected_status_code = 404
        expected_code = "DOCUMENT_NOT_FOUND"
        expected_message = "User with the specified ID was not found."
        user_id = "004f6f1777e2551b87786650"

        client = UsersApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_users_by_id(user_id)
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_code, response.json().get('code'))
        self.assertEqual(expected_message, response.json().get('message'))
        validate(instance=response.json(), schema=SCHEMA_FOR_ERRORS)
