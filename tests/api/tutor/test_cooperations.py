import allure

from SpaceToStudy.api.cooperations.client_cooperations import CooperationsApiClient
from SpaceToStudy.api.cooperations.schemas import ALL_COOPERATIONS_SCHEMA, SCHEMA_COOPERATIONS_ID
from SpaceToStudy.api.schema_for_errors import SCHEMA_FOR_ERRORS
from tests.api.api_test_runners import APITestRunnerWithTutor
from tests.utils.value_provider import ValueProvider

from jsonschema import validate
from parameterized import parameterized, parameterized_class


class TestCooperationsApi(APITestRunnerWithTutor):

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/463#issue-1963185501")
    def test_find_all_cooperations(self):
        client = CooperationsApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_cooperations()
        self.assertEqual(200, response.status_code)
        validate(instance=response.json(), schema=ALL_COOPERATIONS_SCHEMA)

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/465#issue-1963247682")
    @parameterized.expand([
        ("6523cd18c296ee19b5a192f9"),
        ("6521d1d778dda5147a2b31fd"),
        ("652142ab78dda5147a2b2f8c"),
        ("651fe46d78dda5147a2b2c50"),
    ])
    def test_find_cooperations_by_id(self, cooperations_id):
        client = CooperationsApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_cooperations_by_id(cooperations_id)
        self.assertEqual(200, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_COOPERATIONS_ID)

    # @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/470#issue-1963642535")
    # @parameterized.expand([
    #     (299),
    #     (999),
    #     (599),
    # ])
    # def test_patch_offer_forbidden_action(self):
    #     client = CooperationsApiClient(ValueProvider.get_base_api_url(), self.accessToken)
    #     response = client.patch_cooperations("6523cd18c296ee19b5a192f9", {"price": 5})
    #     self.assertEqual(204, response.status_code)
    #     validate(instance=response.json(), schema=SCHEMA_COOPERATIONS_ID)