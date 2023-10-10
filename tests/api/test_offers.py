import unittest
from jsonschema import validate
from SpaceToStudy.api.auth_client import AuthApiClient

from tests.utils.value_provider import ValueProvider
import requests


class TestOffersApi(BaseAPITestRunner):

    def test_offers(self):

        unauthorized_schema = {
            "type": "object",
            "properties": {
                "code": {
                    "type": "string"
                },
                "message": {
                    "type": "string"
                },
                "status": {
                    "type": "integer"
                }
            },
            "required": ["code", "message"],
        }

        url = f'{ValueProvider.get_base_api_url()}offers'
        response = requests.get(url)
        assert response.status_code == 401
        assert response.json().get('message') == "The requested URL requires user authorization."
        assert response.json().get('code') == "UNAUTHORIZED"
        validate(instance=response.json(), schema=unauthorized_schema)