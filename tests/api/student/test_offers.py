import allure
from jsonschema import validate
from parameterized import parameterized

from SpaceToStudy.api.offers.client_offers import OffersApiClient
from SpaceToStudy.api.offers.schemas import ALL_OFFERS_SCHEMA, SCHEMA_OFFERS_ID
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

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/491#issue-1966961096")
    @parameterized.expand([
        ("64944a54e874088383fdfb84", "64884f33fdc2d1a130c24ac2", "64885108fdc2d1a130c24af9"),
        ("64ac054c137130e45017f841", "64884f21fdc2d1a130c24ac0", "648850c4fdc2d1a130c24aea"),
    ])
    def test_find_offers_by_id_with_correct_category_and_subject_id(self, offer_id, category_id, subject_id):
        client = OffersApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_offers_by_id(offer_id)
        category_id_of_offer = response.json()["category"]["_id"]
        subject_id_of_offer = response.json()["subject"]["_id"]
        self.assertEqual(200, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_OFFERS_ID)
        self.assertEqual(category_id, category_id_of_offer)
        self.assertEqual(subject_id, subject_id_of_offer)