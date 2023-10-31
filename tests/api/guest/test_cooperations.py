from SpaceToStudy.api.schema_for_errors import SCHEMA_FOR_ERRORS
from tests.api.api_test_runners import BaseAPITestRunner

import allure
from jsonschema import validate

from tests.utils.value_provider import ValueProvider


class TestCooperationApi(BaseAPITestRunner):

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/505#issue-1970511199")
    def test_get_cooperation_unauthorized_user(self):
        client = CooperationApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_cooperation()
        self.assertEqual(401, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_ERRORS)
        self.assertEqual("The requested URL requires user authorization.", response.json().get('message'))
        self.assertEqual("UNAUTHORIZED", response.json().get('code'))

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/507#issue-1970518247")
    def test_post_cooperation_unauthorized_user(self):
        data = {
            "_id": "8755bc080a00adr9243df104",
            "offer": "63ebc6fbd2f34037d0aba791",
            "initiator": "6255bc080a75adf9223df212",
            "initiatorRole": "tutor",
            "receiver": "6255bc080a75adf9223df100",
            "receiverRole": "student",
            "price": 300,
            "status": "pending",
            "needAction": "student",
            "createdAt": "2021-04-09T11:34:53.243+00:00",
            "updatedAt": "2022-09-02T11:59:53.243+00:00"
        }
        client = CooperationApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.post_cooperation(data=data)
        self.assertEqual(401, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_ERRORS)
        self.assertEqual("The requested URL requires user authorization.", response.json().get('message'))
        self.assertEqual("UNAUTHORIZED", response.json().get('code'))

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/506#issue-1970512704")
    def test_get_cooperation_by_id_unauthorized_user(self):
        client = CooperationApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_cooperation_by_id("8755bc080a00adr9243df104")
        self.assertEqual(401, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_ERRORS)
        self.assertEqual("The requested URL requires user authorization.", response.json().get('message'))
        self.assertEqual("UNAUTHORIZED", response.json().get('code'))

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/508#issue-1970520060")
    def test_patch_cooperation_by_id_unauthorized_user(self):
        client = CooperationApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.patch_cooperation("8755bc080a00adr9243df104", {"status": "closed"})
        self.assertEqual(401, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_ERRORS)
        self.assertEqual("The requested URL requires user authorization.", response.json().get('message'))
        self.assertEqual("UNAUTHORIZED", response.json().get('code'))
