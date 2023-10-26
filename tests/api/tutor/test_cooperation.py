import allure

from SpaceToStudy.api.cooperations.client_cooperations import CooperationsApiClient
from SpaceToStudy.api.cooperations.schemas import ALL_COOPERATIONS_SCHEMA, SCHEMA_COOPERATIONS_ID
from SpaceToStudy.api.schema_for_errors import SCHEMA_FOR_ERRORS
from tests.api.api_test_runners import APITestRunnerWithTutor
from tests.utils.value_provider import ValueProvider

from jsonschema import validate
from parameterized import parameterized, parameterized_class


class TestCooperationApi(APITestRunnerWithTutor):

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/470#issue-1963642535")
    @parameterized.expand([
        (299),
        (999),
        (599),
    ])
    def test_patch_ocooperations(self, data_price):
        client = CooperationsApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.patch_cooperations("6523cd18c296ee19b5a192f9", {"price": data_price})
        self.assertEqual(204, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_COOPERATIONS_ID)

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/471#issue-1963647597")
    def test_patch_cooperations_invalid_id(self):
        client = CooperationsApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.patch_cooperations("652ea7336fc04ef55", {"price": 123})
        self.assertEqual(400, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_ERRORS)
        self.assertEqual("ID is invalid.", response.json().get('message'))
        self.assertEqual("INVALID_ID", response.json().get('code'))

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/472#issue-1963650643")
    @parameterized.expand([
        ("652ea7336fc04ef55bb462cf"),
        ("652ea2345fc04ef55bb462cf"),
        ("652ea6789fc04ef55bb462cf"),
        ("652ea1263fc04ef55bb462cf")
    ])
    def test_patch_cooperations_document_not_found(self, data_id):
        client = CooperationsApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.patch_cooperations(data_id, {"price": 321})
        self.assertEqual(404, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_ERRORS)
        self.assertEqual("Cooperation with the specified ID was not found.", response.json().get('message'))
        self.assertEqual("DOCUMENT_NOT_FOUND", response.json().get('code'))
