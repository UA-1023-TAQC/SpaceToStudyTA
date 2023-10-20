import allure
from jsonschema import validate

from SpaceToStudy.api.chats.client_chats import ChatsAPIClient
from SpaceToStudy.api.chats.schemas import SCHEMA_FOR_ALL_CHATS
from tests.api.api_test_runners import APITestRunnerWithStudent
from tests.utils.value_provider import ValueProvider


class TestAPIChats(APITestRunnerWithStudent):

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/428")
    def test_get_all_chats(self):
        client = ChatsAPIClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_chats()
        self.assertEqual(response.status_code, 200)
        validate(instance=response.json(), schema=SCHEMA_FOR_ALL_CHATS)
