import allure
from jsonschema import validate

from SpaceToStudy.api.offers.client_offers import OffersApiClient
from SpaceToStudy.api.offers.schemas import ALL_OFFERS_SCHEMA, SCHEMA_OFFERS_ID, SCHEMA_POST_OFFER
from SpaceToStudy.api.schema_for_errors import SCHEMA_FOR_ERRORS
from tests.api.api_test_runners import APITestRunnerWithStudent
from tests.utils.value_provider import ValueProvider


class TestOffersApi(APITestRunnerWithStudent):

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/405#issue-1945106730")
    def test_find_all_offers(self):
        client = OffersApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_offers()
        self.assertEqual(200, response.status_code)
        validate(instance=response.json(), schema=ALL_OFFERS_SCHEMA)

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/422#issue-1947831861")
    def test_find_all_offers(self):
        client = OffersApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_offers_by_id("123")
        self.assertEqual(400, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_ERRORS)
        self.assertEqual("ID is invalid.", response.json().get('message'))
        self.assertEqual("INVALID_ID", response.json().get('code'))

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/405#issue-1945106730")
    def test_find_all_offers(self):
        client = OffersApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_offers_by_id("652ea7336fc04ef55bb462cf")
        self.assertEqual(200, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_OFFERS_ID)

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/452#issue-1962971089")
    def test_post_offer(self):
        # post offer
        data = {
            "price": "399",
            "proficiencyLevel": [
                "Advanced"
            ],
            "title": "I hope to improve my skills and gain new knowledge",
            "languages": [
                "English",
                "Ukrainian"
            ],
            "subject": "6488509cfdc2d1a130c24ae4",
            "category": "64884fb0fdc2d1a130c24ad8",
        }
        client = OffersApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.post_offer(data=data)
        self.assertEqual(201, response.status_code)
        data_id = response.json()["_id"]

        # delete offer
        client = OffersApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.delete_offer(data_id)
        self.assertEqual(204, response.status_code)

