import allure
from jsonschema import validate

from SpaceToStudy.api.schema_for_errors import SCHEMA_FOR_ERRORS
from SpaceToStudy.api.users.client import UsersApiClient
from tests.api.api_test_runners import BaseAPITestRunner
from tests.utils.value_provider import ValueProvider

expected_status_code = 401
expected_code = "UNAUTHORIZED"
expected_message = "The requested URL requires user authorization."
user_id = "644f6f1777e2551b87786650"


class TestAPIUsers(BaseAPITestRunner):

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/402",
                     "Create test for api/users find all users")
    def test_find_all_users_unauthorized(self):
        client = UsersApiClient(ValueProvider.get_base_api_url())
        response = client.get_users()
        self.assertEqual(expected_status_code, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_ERRORS)
        self.assertEqual(expected_code, response.json().get('code'))
        self.assertEqual(expected_message, response.json().get('message'))

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/404",
                     "Create test for api/users Find user by ID ")
    def test_find_user_by_id_unauthorized(self):
        client = UsersApiClient(ValueProvider.get_base_api_url())
        response = client.get_users_by_id(user_id)
        self.assertEqual(expected_status_code, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_ERRORS)
        self.assertEqual(expected_code, response.json().get('code'))
        self.assertEqual(expected_message, response.json().get('message'))

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/416",
                     "Create test for API GET /users/{id}/reviews Find all reviews for a user with the specified ID "
                     "and role")
    def test_get_reviews_for_user_by_id_unauthorized(self):
        client = UsersApiClient(ValueProvider.get_base_api_url())
        response = client.get_reviews_for_user_by_id(user_id, "student")
        self.assertEqual(expected_status_code, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_ERRORS)
        self.assertEqual(expected_code, response.json().get('code'))
        self.assertEqual(expected_message, response.json().get('message'))

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/426",
                     "Create tests for GET /users/{id}/reviews/stats Find review statistics for a user with the "
                     "specified ID and role ")
    def test_find_review_statistics_for_user_by_id_unauthorized(self):
        client = UsersApiClient(ValueProvider.get_base_api_url())
        response = client.get_review_statistics_for_user_by_id(user_id)
        self.assertEqual(expected_status_code, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_ERRORS)
        self.assertEqual(expected_code, response.json().get('code'))
        self.assertEqual(expected_message, response.json().get('message'))

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/469",
                     "Create tests for GET /users/{id}/cooperations Find cooperations for a user with specified ID")
    def test_find_cooperations_for_user_by_id_unauthorized(self):
        client = UsersApiClient(ValueProvider.get_base_api_url())
        response = client.get_cooperations_for_user_by_id(user_id)
        self.assertEqual(expected_status_code, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_ERRORS)
        self.assertEqual(expected_code, response.json().get('code'))
        self.assertEqual(expected_message, response.json().get('message'))

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/443",
                     "Create tests for GET /users/{id}/offers Find offers for a user with specified ID")
    def test_find_offers_for_user_by_id_unauthorized(self):
        client = UsersApiClient(ValueProvider.get_base_api_url())
        response = client.get_offers_for_user_by_id(user_id)
        self.assertEqual(expected_status_code, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_ERRORS)
        self.assertEqual(expected_code, response.json().get('code'))
        self.assertEqual(expected_message, response.json().get('message'))

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/525",
                     "Create tests for PATCH /users/{id} Find and update other user info")
    def test_patch_other_user_info_by_id_unauthorized(self):
        data_for_patch = {
            "lastName": "Holmes"
        }
        client = UsersApiClient(ValueProvider.get_base_api_url())
        response = client.patch_current_user_info_by_id(user_id, data_for_patch)
        self.assertEqual(expected_status_code, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_ERRORS)
        self.assertEqual(expected_code, response.json().get('code'))
        self.assertEqual(expected_message, response.json().get('message'))
