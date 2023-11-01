import allure
from jsonschema import validate

from SpaceToStudy.api.res_categories.client import ResoursesCategoriesApiClient
from SpaceToStudy.api.schema_for_errors import SCHEMA_FOR_ERRORS
from tests.api.api_test_runners import BaseAPITestRunner, APITestRunnerWithStudent, APITestRunnerWithTutor
from tests.utils.value_provider import ValueProvider


class TestResCategoriesApi(BaseAPITestRunner):

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/436")
    def test_get_res_categories_unauthorized_user(self):
        client = ResoursesCategoriesApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_res_categories()
        self.assertEqual(401, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_ERRORS)
        self.assertEqual("The requested URL requires user authorization.", response.json().get('message'))
        self.assertEqual("UNAUTHORIZED", response.json().get('code'))

class TestResCategoriesApiWithStudent(APITestRunnerWithStudent):
    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/436")
    def test_get_res_categories_authorized_user_student(self):
        client = ResoursesCategoriesApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_res_categories()
        self.assertEqual(403, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_ERRORS)
        self.assertEqual("You do not have permission to perform this action.", response.json().get('message'))
        self.assertEqual("FORBIDDEN", response.json().get('code'))

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/436")
    def test_post_res_categories_authorized_user_student(self):
        client = ResoursesCategoriesApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        data = {
            "name": "Chemical Category"
        }
        response = client.post_res_categories(data)
        self.assertEqual(403, response.status_code)
        self.assertEqual("You do not have permission to perform this action.", response.json().get('message'))
        self.assertEqual("FORBIDDEN", response.json().get('code'))

class TestResCategoriesApiWithTutor(APITestRunnerWithTutor):
    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/436")
    def test_get_res_categories_authorized_user_tutor(self):
        client = ResoursesCategoriesApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_res_categories()
        self.assertEqual(200, response.status_code)
        print(response.json())

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/436")
    def test_post_res_categories_authorized_user_tutor(self):
        client = ResoursesCategoriesApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        data = {
            "name": "Chemical Category"
        }
        response = client.post_res_categories(data)
        self.assertEqual(201, response.status_code)

        response = client.get_res_categories()
        for i in range (response.json()["count"]):
            for item in response.json()["items"]:
                self.assertEqual(item["name"], data["name"])
                resp_del = client.delete_res_categories(rc_id=item["_id"])
                self.assertEqual(204, resp_del.status_code)

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/436")
    def test_delete_res_categories_authorized_user_tutor(self):
        client = ResoursesCategoriesApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.delete_res_categories('654285f3a226df4d38cd72d5')
        print(response)
        self.assertEqual(200, response.status_code)
