import allure
from jsonschema import validate

from SpaceToStudy.api.res_categories.client import ResoursesCategoriesApiClient
from SpaceToStudy.api.schema_for_errors import SCHEMA_FOR_ERRORS
from tests.api.api_test_runners import BaseAPITestRunner, APITestRunnerWithStudent, APITestRunnerWithTutor
from tests.utils.value_provider import ValueProvider


class TestResCategoriesApi(BaseAPITestRunner):

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/436")
    def test_unauthorized_user(self):
        client = ResoursesCategoriesApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_res_categories()
        self.assertEqual(401, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_ERRORS)
        self.assertEqual("The requested URL requires user authorization.", response.json().get('message'))
        self.assertEqual("UNAUTHORIZED", response.json().get('code'))

class TestResCategoriesApi(APITestRunnerWithStudent):
    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/436")
    def test_authorized_user(self):
        client = ResoursesCategoriesApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        data = {
            "name": "Chemical Category"
        }
        response = client.post_res_categories(data)
        self.assertEqual(403, response.status_code)
        self.assertEqual("You do not have permission to perform this action.", response.json().get('message'))
        self.assertEqual("FORBIDDEN", response.json().get('code'))

class TestResCategoriesApi(APITestRunnerWithTutor):
    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/436")
    def test_authorized_user(self):
        client = ResoursesCategoriesApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        data = {
            "name": "Chemical Category"
        }
        response = client.post_res_categories(data)
        self.assertEqual(201, response.status_code)

        response = client.get_res_categories(name=data["name"])
        for i in range (response.json()["count"]):
            for item in response.json()["items"]:
                self.assertEqual(item["name"], data["name"])
        print(response.json())