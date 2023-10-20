import allure
from jsonschema import validate

from SpaceToStudy.api.offers.client_offers import OffersApiClient
from SpaceToStudy.api.schema_for_errors import SCHEMA_FOR_ERRORS
from tests.api.api_test_runners import BaseAPITestRunner
from tests.utils.value_provider import ValueProvider


class TestOffersApi(BaseAPITestRunner):

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/394")
    def test_unauthorized_user(self):
        client = OffersApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_offers()
        self.assertEqual(401, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_ERRORS)
        self.assertEqual("The requested URL requires user authorization.", response.json().get('message'))
        self.assertEqual("UNAUTHORIZED", response.json().get('code'))
