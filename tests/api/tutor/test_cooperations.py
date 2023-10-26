import allure

from SpaceToStudy.api.cooperations.client_cooperations import CooperationsApiClient
from SpaceToStudy.api.cooperations.schemas import ALL_COOPERATIONS_SCHEMA
from tests.api.api_test_runners import APITestRunnerWithTutor
from tests.utils.value_provider import ValueProvider

from jsonschema import validate


class TestCooperationsApi(APITestRunnerWithTutor):

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/463#issue-1963185501")
    def test_find_all_cooperations(self):
        client = CooperationsApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_cooperations()
        self.assertEqual(200, response.status_code)
        validate(instance=response.json(), schema=ALL_COOPERATIONS_SCHEMA)
