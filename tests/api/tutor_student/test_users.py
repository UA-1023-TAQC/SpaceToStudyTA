import allure
from jsonschema import validate
from parameterized.parameterized import parameterized_class, parameterized

from SpaceToStudy.api.schema_for_errors import SCHEMA_FOR_ERRORS
from SpaceToStudy.api.users.client import UsersApiClient
from SpaceToStudy.api.users.schemas import (SCHEMA_FOR_ALL_USERS,
                                            SCHEMA_FOR_USER,
                                            SCHEMA_FOR_REVIEWS_BY_USER_ID,
                                            SCHEMA_FOR_REVIEW_STATISTICS_FOR_USER,
                                            SCHEMA_FOR_COOPERATIONS_BY_USER_ID)
from tests.api.api_test_runners import BaseAPITestRunner, get_access_token
from tests.utils.value_provider import ValueProvider as VP


@parameterized_class([
    {"name:": VP.get_student_first_name(),
     "accessToken": get_access_token(VP.get_student_email(), VP.get_student_password())},
    {"name:": VP.get_tutor_first_name(),
     "accessToken": get_access_token(VP.get_tutor_email(), VP.get_tutor_password())},
])
class TestAPIUsers(BaseAPITestRunner):

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/402",
                     "Create test for api/users find all users")
    def test_find_all_users(self):
        expected_status_code = 200
        client = UsersApiClient(VP.get_base_api_url(), self.accessToken)
        response = client.get_users()
        self.assertEqual(expected_status_code, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_ALL_USERS)

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/404",
                     "Create test for api/users Find user by ID role:{role} user_id:{user_id}")
    @parameterized.expand([
        (None, "644f6f1777e2551b87786650"),
        ("tutor", "644f6f1777e2551b87786650"),
        ("student", "650023e50eeb49de31750c84"),
    ])
    def test_find_user_by_id(self, role, user_id):
        expected_status_code = 200

        client = UsersApiClient(VP.get_base_api_url(), self.accessToken)
        response = client.get_users_by_id(user_id, role)
        self.assertEqual(expected_status_code, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_USER)

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/404",
                     "Create test for api/users Find user by ID role:{role} user_id:{user_id}")
    @parameterized.expand([
        ("student", "644f6f1777e2551b87786650"),
        ("tutor", "650023e50eeb49de31750c84"),
        (123, "644f6f1777e2551b87786650"),
        ("abc", "644f6f1777e2551b87786650"),
    ])
    def test_find_user_by_id_incorrect_role(self, role, user_id):
        expected_status_code = 200

        client = UsersApiClient(VP.get_base_api_url(), self.accessToken)
        response = client.get_users_by_id(user_id, role)
        self.assertEqual(expected_status_code, response.status_code)
        self.assertIsNone(response.json())

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/416",
                     "Create test for API GET /users/{id}/reviews Find all reviews for a user with the specified ID "
                     "and role role:{role} user_id:{user_id}")
    @parameterized.expand([
        ("tutor", "647dec927ffdce904010287c", None, None, None),
        ("tutor", "647dec927ffdce904010287c", 5, None, None),
        ("tutor", "647dec927ffdce904010287c", 3, 2, None),
        ("tutor", "647dec927ffdce904010287c", 5, 1, 6),
        ("student", "650023e50eeb49de31750c84", None, None, None),
        (None, "647dec927ffdce904010287c", 3, 0, 5),
        (None, "647dec927ffdce904010287c", None, None, None),
    ])
    def test_get_reviews_for_user_by_id(self, role, user_id, rating, skip, limit):
        expected_status_code = 200

        client = UsersApiClient(VP.get_base_api_url(), self.accessToken)
        response = client.get_reviews_for_user_by_id(user_id, role, rating, skip, limit)
        self.assertEqual(expected_status_code, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_REVIEWS_BY_USER_ID)

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/416",
                     "Create test for API GET /users/{id}/reviews Find all reviews for a user with the specified ID "
                     "and role role:{role} user_id:{user_id}")
    @parameterized.expand([
        ("cat", "647dec927ffdce904010287c", None, "abc", "abc"),
        ("cat", "647dec927ffdce904010287c", 3.5, 2.5, 2.5)
    ])
    def test_get_reviews_for_user_by_id_incorrect_parameters(self, role, user_id, rating, skip, limit):
        expected_status_code = 200

        client = UsersApiClient(VP.get_base_api_url(), self.accessToken)
        response = client.get_reviews_for_user_by_id(user_id, role, rating, skip, limit)
        self.assertEqual(expected_status_code, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_REVIEWS_BY_USER_ID)
        self.assertEqual(0, response.json()["count"], "Received JSON contains reviews")

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/416",
                     "Create test for API GET /users/{id}/reviews Find all reviews for a user with the specified ID "
                     "and role")
    def test_get_reviews_for_user_by_id_invalid_rating_parameter_type(self):
        user_id = "644f6f1777e2551b87786650"
        rating = "abc"
        expected_status_code = 500
        expected_code = "INTERNAL_SERVER_ERROR"
        expected_message = (f'Cast to Number failed for value "{rating}" (type string) at path "rating" for model '
                            f'"Review"')

        client = UsersApiClient(VP.get_base_api_url(), self.accessToken)
        response = client.get_reviews_for_user_by_id(user_id, "tutor", rating, 2, 6)
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_code, response.json().get('code'))
        self.assertEqual(expected_message, response.json().get('message'))

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/426",
                     "Create tests for GET /users/{id}/reviews/stats Find review statistics for a user with the "
                     "specified ID: {user_id} and role: {role}")
    @parameterized.expand([
        ("tutor", "647dec927ffdce904010287c"),
        ("student", "650023e50eeb49de31750c84")
    ])
    def test_find_review_statistics_for_user_by_id(self, role, user_id):
        expected_status_code = 200

        client = UsersApiClient(VP.get_base_api_url(), self.accessToken)
        response = client.get_review_statistics_for_user_by_id(user_id, role)
        self.assertEqual(expected_status_code, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_REVIEW_STATISTICS_FOR_USER)

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/426",
                     "Create tests for GET /users/{id}/reviews/stats Find review statistics for a user with the "
                     "specified ID: {user_id} and role: {role}")
    @parameterized.expand([
        (None, "647dec927ffdce904010287c"),
        ("cat", "647dec927ffdce904010287c"),
        (123, "647dec927ffdce904010287c")
    ])
    def test_find_review_statistics_for_user_by_id_invalid_role(self, role, user_id):
        expected_status_code = 200

        client = UsersApiClient(VP.get_base_api_url(), self.accessToken)
        response = client.get_review_statistics_for_user_by_id(user_id, role)
        self.assertEqual(expected_status_code, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_REVIEW_STATISTICS_FOR_USER)
        self.assertEqual({}, response.json(), "Received JSON is not empty")

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/469",
                     "Create tests for GET /users/{id}/cooperations Find cooperations for a user with the specified "
                     "ID :{user_id}")
    @parameterized.expand([
        ("tutor", "647dec927ffdce904010287c"),
        ("student", "650023e50eeb49de31750c84")
    ])
    def test_find_cooperations_for_user_by_id(self, _, user_id):
        expected_status_code = 200

        client = UsersApiClient(VP.get_base_api_url(), self.accessToken)
        response = client.get_cooperations_for_user_by_id(user_id)
        self.assertEqual(expected_status_code, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_COOPERATIONS_BY_USER_ID)

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/512",
                     "Create negative API tests GET /users [Status_code 400]")
    @parameterized.expand([
        ("get_users_by_id", None),
        ("get_reviews_for_user_by_id", "student"),
        ("get_review_statistics_for_user_by_id", None),
        ("get_cooperations_for_user_by_id", None)
    ])
    def test_invalid_id(self, method, role):
        expected_status_code = 400
        expected_code = "INVALID_ID"
        expected_message = "ID is invalid."
        invalid_id = "abcdefg"

        client = UsersApiClient(VP.get_base_api_url(), self.accessToken)
        if role is None:
            response = getattr(client, method)(invalid_id)
        else:
            response = getattr(client, method)(invalid_id, role)

        self.assertEqual(expected_status_code, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_ERRORS)
        self.assertEqual(expected_code, response.json().get('code'))
        self.assertEqual(expected_message, response.json().get('message'))

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/513",
                     "Create negative API tests GET /users [Status_code 404]")
    @parameterized.expand([
        ("get_users_by_id", None),
        ("get_reviews_for_user_by_id", "student"),
        ("get_review_statistics_for_user_by_id", None),
        ("get_cooperations_for_user_by_id", None)
    ])
    def test_id_not_found(self, method, role):
        expected_status_code = 404
        expected_code = "DOCUMENT_NOT_FOUND"
        expected_message = "User with the specified ID was not found."
        nonexistent_id = "004f6f1777e2551b87786650"

        client = UsersApiClient(VP.get_base_api_url(), self.accessToken)
        if role is None:
            response = getattr(client, method)(nonexistent_id)
        else:
            response = getattr(client, method)(nonexistent_id, role)

        self.assertEqual(expected_status_code, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_ERRORS)
        self.assertEqual(expected_code, response.json().get('code'))
        self.assertEqual(expected_message, response.json().get('message'))

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/479",
                     "Create tests for PATCH /users/{id} Find and update current user info")
    def test_patch_current_user_info_by_id(self):
        data_for_patch = {
            "lastName": "Holmes"
        }
        expected_status_code = 204

        # get current name value
        client = UsersApiClient(VP.get_base_api_url(), self.accessToken)
        access_token_decoded_json = client.get_decode_access_token()
        user_id = access_token_decoded_json.get("id")
        current_lastname = client.get_users_by_id(user_id).json()["lastName"]

        # patch
        response = client.patch_current_user_info_by_id(user_id, data_for_patch)
        self.assertEqual(expected_status_code, response.status_code)
        new_lastname = client.get_users_by_id(user_id).json()["lastName"]
        self.assertNotEqual(current_lastname, new_lastname)

        # return to original value
        response = client.patch_current_user_info_by_id(user_id, {"lastName": current_lastname})
        self.assertEqual(expected_status_code, response.status_code)

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/525",
                     "Create test for PATCH/users/{id} Find and update other user info[Status_code 400, 403, 404]")
    @parameterized.expand([
        ("valid_id", "64e88b8b253a3ff15b9c6cf5", 403, "FORBIDDEN", "You do not have permission to perform this action."),
        ("invalid_id", "abcdefg", 400, "INVALID_ID", "ID is invalid."),
        ("nonexistent_id", "00088b8b253a3ff15b9c6cf5", 404, "DOCUMENT_NOT_FOUND", "User with the specified ID was not "
                                                                                  "found."),
    ])
    def test_patch_other_user_info_by_id(self, _, user_id, expected_status_code, expected_code, expected_message):
        data_for_patch = {
            "lastName": "Holmes"
        }
        client = UsersApiClient(VP.get_base_api_url(), self.accessToken)
        response = client.patch_current_user_info_by_id(user_id, data_for_patch)
        self.assertEqual(expected_status_code, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_ERRORS)
        self.assertEqual(expected_code, response.json().get('code'))
        self.assertEqual(expected_message, response.json().get('message'))
