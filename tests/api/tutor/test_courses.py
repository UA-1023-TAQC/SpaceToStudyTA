import allure

from SpaceToStudy.api.courses.client_courses import CoursesApiClient
from SpaceToStudy.api.courses.schemas import SCHEMA_FOR_ALL_COURSES
from tests.api.api_test_runners import APITestRunnerWithTutor
from tests.utils.value_provider import ValueProvider
from jsonschema import validate


class TestAPICourses(APITestRunnerWithTutor):
    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/474")
    def test_get_courses(self):
        client = CoursesApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_courses()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["count"], len(response.json()["items"]))
        validate(instance=response.json(), schema=SCHEMA_FOR_ALL_COURSES)

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/474")
    def test_get_courses_by_id(self):
        client = CoursesApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_courses_by_id()  # There should be an ID here when it appears
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["count"], len(response.json()["items"]))
        self.assertEqual(response.json()["title"], "Test title")
        validate(instance=response.json(), schema=SCHEMA_FOR_ALL_COURSES)
