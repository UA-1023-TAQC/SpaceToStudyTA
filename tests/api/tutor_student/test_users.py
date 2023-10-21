import allure
from jsonschema import validate
from parameterized.parameterized import parameterized_class, parameterized

from SpaceToStudy.api.schema_for_errors import SCHEMA_FOR_ERRORS
from SpaceToStudy.api.users.client import UsersApiClient
from SpaceToStudy.api.users.schemas import SCHEMA_FOR_ALL_USERS, SCHEMA_FOR_USER, SCHEMA_FOR_REVIEWS_BY_USER_ID
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
        ("123", "644f6f1777e2551b87786650"),
        ("abc", "644f6f1777e2551b87786650"),
    ])
    def test_find_user_by_id_incorrect_role(self, role, user_id):
        expected_status_code = 200

        client = UsersApiClient(VP.get_base_api_url(), self.accessToken)
        response = client.get_users_by_id(user_id, role)
        self.assertEqual(expected_status_code, response.status_code)
        self.assertIsNone(response.json())

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/404",
                     "Create test for api/users Find user by ID ")
    def test_find_user_by_id_invalid_id(self):
        expected_status_code = 400
        expected_code = "INVALID_ID"
        expected_message = "ID is invalid."
        user_id = "abcdefg"

        client = UsersApiClient(VP.get_base_api_url(), self.accessToken)
        response = client.get_users_by_id(user_id)
        self.assertEqual(expected_status_code, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_ERRORS)
        self.assertEqual(expected_code, response.json().get('code'))
        self.assertEqual(expected_message, response.json().get('message'))

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/404",
                     "Create test for api/users Find user by ID ")
    def test_find_user_by_id_not_found_id(self):
        expected_status_code = 404
        expected_code = "DOCUMENT_NOT_FOUND"
        expected_message = "User with the specified ID was not found."
        user_id = "004f6f1777e2551b87786650"

        client = UsersApiClient(VP.get_base_api_url(), self.accessToken)
        response = client.get_users_by_id(user_id)
        self.assertEqual(expected_status_code, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_ERRORS)
        self.assertEqual(expected_code, response.json().get('code'))
        self.assertEqual(expected_message, response.json().get('message'))

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/416",
                     "Create test for API GET /users/{id}/reviews Find all reviews for a user with the specified ID "
                     "and role role:{role} user_id:{user_id}")
    @parameterized.expand([
        ("tutor", "644f6f1777e2551b87786650", None, None, None),
        ("tutor", "644f6f1777e2551b87786650", 4, None, None),
        ("tutor", "644f6f1777e2551b87786650", 4, 2, None),
        ("tutor", "644f6f1777e2551b87786650", 4, 2, 6),
        ("student", "650023e50eeb49de31750c84", None, None, None),
        (None, "644f6f1777e2551b87786650", 3, 1, 5),
        (None, "650023e50eeb49de31750c84", None, None, None),
        ("cat", "650023e50eeb49de31750c84", None, "abc", "abc"),
        ("cat", "644f6f1777e2551b87786650", 3.5, 2.5, 2.5),
    ])
    def test_get_reviews_for_user_by_id(self, role, user_id, rating, skip, limit):
        expected_status_code = 200

        client = UsersApiClient(VP.get_base_api_url(), self.accessToken)
        response = client.get_reviews_for_user_by_id(user_id, role, rating, skip, limit)
        self.assertEqual(expected_status_code, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_REVIEWS_BY_USER_ID)

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/416",
                     "Create test for API GET /users/{id}/reviews Find all reviews for a user with the specified ID "
                     "and role")
    def test_get_reviews_for_user_by_id_invalid_id(self):
        expected_status_code = 400
        expected_code = "INVALID_ID"
        expected_message = "ID is invalid."
        user_id = "abcdefg"

        client = UsersApiClient(VP.get_base_api_url(), self.accessToken)
        response = client.get_reviews_for_user_by_id(user_id, "student")
        self.assertEqual(expected_status_code, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_ERRORS)
        self.assertEqual(expected_code, response.json().get('code'))
        self.assertEqual(expected_message, response.json().get('message'))

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

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/416",
                     "Create test for API GET /users/{id}/reviews Find all reviews for a user with the specified ID "
                     "and role")
    def test_get_reviews_for_user_by_id_not_found_id(self):
        expected_status_code = 404
        expected_code = "DOCUMENT_NOT_FOUND"
        expected_message = "User with the specified ID was not found."
        user_id = "004f6f1777e2551b87786650"

        client = UsersApiClient(VP.get_base_api_url(), self.accessToken)
        response = client.get_reviews_for_user_by_id(user_id, "student")
        self.assertEqual(expected_status_code, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_ERRORS)
        self.assertEqual(expected_code, response.json().get('code'))
        self.assertEqual(expected_message, response.json().get('message'))
