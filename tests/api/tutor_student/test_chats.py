import allure
from jsonschema import validate
from parameterized.parameterized import parameterized_class

from SpaceToStudy.api.chats.client_chats import ChatsAPIClient
from SpaceToStudy.api.chats.schemas import SCHEMA_FOR_ALL_CHATS

from tests.api.api_test_runners import BaseAPITestRunner, get_access_token
from tests.utils.value_provider import ValueProvider as VP


@parameterized_class([
    {"name:": VP.get_student_first_name(),
     "accessToken": get_access_token(VP.get_student_email(), VP.get_student_password())},
    {"name:": VP.get_tutor_first_name(),
     "accessToken": get_access_token(VP.get_tutor_email(), VP.get_tutor_password())},
])
class TestAPIChats(BaseAPITestRunner):

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/428",
                     "Create test for finding all chats for current user")
    def test_get_all_chats(self):
        client = ChatsAPIClient(VP.get_base_api_url(), self.accessToken)
        response = client.get_chats()
        validate(instance=response.json(), schema=SCHEMA_FOR_ALL_CHATS)
        self.assertEqual(response.status_code, 200)

