import allure
from jsonschema import validate

from SpaceToStudy.api.chats.client_chats import ChatsAPIClient
from SpaceToStudy.api.schema_for_errors import SCHEMA_FOR_ERRORS
from tests.api.api_test_runners import BaseAPITestRunner
from tests.utils.value_provider import ValueProvider


class TestAPIChats(BaseAPITestRunner):

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/459",
                     "Create a negative test for finding messages in chat by id of the chat (401:UNAUTHORIZED)")
    def test_unauthorized_user_find_messages_in_chat_by_id(self):
        client = ChatsAPIClient(ValueProvider.get_base_api_url())
        response = client.get_messages_in_chat_by_id("6532415104a61848c1e6a99b")
        self.assertEqual(response.status_code, 401)
        validate(instance=response.json(), schema=SCHEMA_FOR_ERRORS)
