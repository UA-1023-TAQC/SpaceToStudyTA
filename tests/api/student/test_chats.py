import allure
from jsonschema import validate

from SpaceToStudy.api.chats.client_chats import ChatsAPIClient
from SpaceToStudy.api.chats.schemas import SCHEMA_FOR_ALL_MESSAGES_IN_CHAT
from SpaceToStudy.api.schema_for_errors import SCHEMA_FOR_ERRORS
from tests.api.api_test_runners import APITestRunnerWithStudent
from tests.utils.value_provider import ValueProvider


class TestAPIChats(APITestRunnerWithStudent):

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/458",
                     "Create test get messages in chat by its")
    def test_get_messages_in_chat_by_its_id(self):
        client = ChatsAPIClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_messages_in_chat_by_id("6532415104a61848c1e6a99b")
        self.assertEqual(response.status_code, 200)
        validate(instance=response.json(), schema=SCHEMA_FOR_ALL_MESSAGES_IN_CHAT)

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/519",
                     "Create a negative test get messages from chat by its id (403:FORBIDDEN)")
    def test_negative_test_get_messages_from_chat_by_id_forbidden(self):
        client = ChatsAPIClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_messages_in_chat_by_id("650df5a9c5694d1d9d4643cd")
        self.assertEqual(response.status_code, 403)
        validate(instance=response.json(), schema=SCHEMA_FOR_ERRORS)

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/520",
                     "Create a negative test get messages from chat by its id (404:NOT FOUND)")
    def test_negative_test_get_messages_from_chat_by_id_not_found(self):
        client = ChatsAPIClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_messages_in_chat_by_id("650df5a9c5694d1d9d46439b")
        self.assertEqual(response.status_code, 404)
        validate(instance=response.json(), schema=SCHEMA_FOR_ERRORS)