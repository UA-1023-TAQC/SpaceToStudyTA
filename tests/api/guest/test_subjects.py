import allure

from SpaceToStudy.api.subjects.client import SubjectsApiClient
from tests.api.api_test_runners import BaseAPITestRunner
from tests.utils.value_provider import ValueProvider


class TestAPISubjects(BaseAPITestRunner):
    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/496")
    def test_get_subject_by_id_unauthorized(self):
        client = SubjectsApiClient(ValueProvider.get_base_api_url())
        response = client.get_subject_by_id("648850c4fdc2d1a130c24aea")
        expected_response = {
            "status": 401,
            "code": "UNAUTHORIZED",
            "message": "The requested URL requires user authorization."
        }
        self.assertEqual(401, response.status_code)
        self.assertEqual(expected_response, response.json())

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/497")
    def test_get_all_subjects_unauthorized(self):
        client = SubjectsApiClient(ValueProvider.get_base_api_url())
        response = client.get_subjects()
        expected_response = {
          "status": 401,
          "code": "UNAUTHORIZED",
          "message": "The requested URL requires user authorization."
        }
        self.assertEqual(401, response.status_code)
        self.assertEqual(expected_response, response.json())

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/498")
    def test_post_subject_unauthorized(self):
        client = SubjectsApiClient(ValueProvider.get_base_api_url())
        response = client.post_subjects({"name": "Klingon", "category": "64884fedfdc2d1a130c24ade"})
        expected_response = {
          "status": 401,
          "code": "UNAUTHORIZED",
          "message": "The requested URL requires user authorization."
        }
        self.assertEqual(401, response.status_code)
        self.assertEqual(expected_response, response.json())