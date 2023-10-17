import allure

from SpaceToStudy.api.offers.client_offers import OffersApiClient
from SpaceToStudy.api.offers.schemas import ALL_OFFERS_SCHEMA
from tests.api.api_test_runners import APITestRunnerWithStudent
from tests.utils.value_provider import ValueProvider
from jsonschema import validate


class TestOffersApi(APITestRunnerWithStudent):

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/405#issue-1945106730")
    def test_find_all_offers(self):
        client = OffersApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_offers()
        self.assertEqual(200, response.status_code)
        validate(instance=response.json(), schema=ALL_OFFERS_SCHEMA)