import allure

from SpaceToStudy.api.cooperations.client_cooperations import CooperationApiClient
from SpaceToStudy.api.cooperations.schemas import ALL_COOPERATIONS_SCHEMA, SCHEMA_COOPERATIONS_ID
from SpaceToStudy.api.offers.client_offers import OffersApiClient
from SpaceToStudy.api.offers.schemas import SCHEMA_OFFERS_ID
from tests.api.api_test_runners import APITestRunnerWithTutor
from tests.utils.value_provider import ValueProvider

from jsonschema import validate
from parameterized import parameterized, parameterized_class


class TestCooperationApi(APITestRunnerWithTutor):

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/463#issue-1963185501")
    def test_find_all_cooperation(self):
        client = CooperationApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_cooperation()
        self.assertEqual(200, response.status_code)
        validate(instance=response.json(), schema=ALL_COOPERATIONS_SCHEMA)

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/465#issue-1963247682")
    @parameterized.expand([
        ("6523cd18c296ee19b5a192f9"),
        ("6521d1d778dda5147a2b31fd"),
        ("652142ab78dda5147a2b2f8c"),
        ("651fe46d78dda5147a2b2c50"),
    ])
    def test_find_cooperation_by_id(self, cooperation_id):
        client = CooperationApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_cooperation_by_id(cooperation_id)
        self.assertEqual(200, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_COOPERATIONS_ID)

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/465#issue-1963247682")
    @parameterized.expand([
        ("650878a78f5d654793fed5ff", "64eeef6e253a3ff15b9c7380"),
        ("650187bc3497ec836ef90a32", "65009c71f5cf153436e8a17d"),
        ("65005ca9f5cf153436e89d9c", "6500596af5cf153436e89c93"),
    ])
    def test_cooperation_by_id_with_correct_offer_id(self, cooperation_id, offer_id_of_cooperation):
        client = CooperationApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_cooperation_by_id(cooperation_id)
        self.assertEqual(200, response.status_code)
        offer_id = response.json()["offer"]["_id"]
        self.assertEqual(offer_id_of_cooperation, offer_id)
        validate(instance=response.json(), schema=SCHEMA_COOPERATIONS_ID)