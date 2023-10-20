from jsonschema import validate
from parameterized.parameterized import parameterized_class

from SpaceToStudy.api.users.client import UsersApiClient
from SpaceToStudy.api.users.schemas import SCHEMA_FOR_ALL_USERS
from tests.api.api_test_runners import BaseAPITestRunner, get_access_token
from tests.utils.value_provider import ValueProvider as VP


@parameterized_class([
    {"accessToken": get_access_token(VP.get_student_email(), VP.get_student_password())},
    {"accessToken": get_access_token(VP.get_tutor_email(), VP.get_tutor_password())},
])
class TestAPIUsers(BaseAPITestRunner):
    def test_find_all_users(self):
        expected_status_code = 200
        client = UsersApiClient(VP.get_base_api_url(), self.accessToken)
        response = client.get_users()
        self.assertEqual(expected_status_code, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_ALL_USERS)
