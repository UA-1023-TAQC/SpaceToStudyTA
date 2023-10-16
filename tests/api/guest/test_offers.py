import allure
from jsonschema import validate

from SpaceToStudy.api.offers.schemas import UNAUTHORIZED_SCHEMA

from tests.api.api_test_runners import BaseAPITestRunner
from tests.utils.value_provider import ValueProvider
import requests


class TestOffersApi(BaseAPITestRunner):

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/394")
    def test_unauthorized_user(self):
        url = f'{ValueProvider.get_base_api_url()}offers'
        response = requests.get(url)
        assert response.status_code == 401
        assert response.json().get('message') == "The requested URL requires user authorization."
        assert response.json().get('code') == "UNAUTHORIZED"
        validate(instance=response.json(), schema=UNAUTHORIZED_SCHEMA)

