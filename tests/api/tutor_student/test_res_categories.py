import allure
from jsonschema import validate
from parameterized import parameterized_class

from SpaceToStudy.api.res_categories.client import ResoursesCategoriesApiClient
from SpaceToStudy.api.schema_for_errors import SCHEMA_FOR_ERRORS
from tests.api.api_test_runners import BaseAPITestRunner, APITestRunnerWithStudent, APITestRunnerWithTutor, \
    get_access_token
from tests.utils.value_provider import ValueProvider as VP, ValueProvider

@parameterized_class([
    {"name:": VP.get_student_first_name(),
     "accessToken": get_access_token(VP.get_student_email(), VP.get_student_password())},
    {"name:": VP.get_tutor_first_name(),
     "accessToken": get_access_token(VP.get_tutor_email(), VP.get_tutor_password())},
])

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
