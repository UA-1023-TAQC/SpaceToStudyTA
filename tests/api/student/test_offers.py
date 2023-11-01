import allure
from jsonschema import validate

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
    def test_find_offer_invalid_id(self):
        client = OffersApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_offers_by_id("123")
        self.assertEqual(400, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_ERRORS)
        self.assertEqual("ID is invalid.", response.json().get('message'))
        self.assertEqual("INVALID_ID", response.json().get('code'))

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/405#issue-1945106730")
    def test_find_offers_by_id(self):
        client = OffersApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_offers_by_id("652ea7336fc04ef55bb462cf")
        self.assertEqual(200, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_OFFERS_ID)

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/454#issue-1963038140")
    def test_delete_offer_invalid_id(self):
        client = OffersApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.delete_offer("12345")
        self.assertEqual(400, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_ERRORS)
        self.assertEqual("ID is invalid.", response.json().get('message'))
        self.assertEqual("INVALID_ID", response.json().get('code'))

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/455#issue-1963040501")
    def test_delete_offer_invalid_id(self):
        client = OffersApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.delete_offer("64954e34650b0c52c50d597e")
        self.assertEqual(404, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_ERRORS)
        self.assertEqual("Offer with the specified ID was not found.", response.json().get('message'))
        self.assertEqual("DOCUMENT_NOT_FOUND", response.json().get('code'))

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/450#issue-1962909192")
    def test_patch_offer_incorrect_id(self):
        client = OffersApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.patch_offer("652ea7336fc04ef55", {"firstName": "Oleksandra"})
        self.assertEqual(400, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_ERRORS)
        self.assertEqual("ID is invalid.", response.json().get('message'))
        self.assertEqual("INVALID_ID", response.json().get('code'))

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/450#issue-1962909192")
    def test_patch_offer_forbidden_action(self):
        client = OffersApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.patch_offer("652ea7336fc04ef55bb462cf", {"firstName": "Oleksandra"})
        self.assertEqual(403, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_ERRORS)
        self.assertEqual("You do not have permission to perform this action.", response.json().get('message'))
        self.assertEqual("FORBIDDEN", response.json().get('code'))


