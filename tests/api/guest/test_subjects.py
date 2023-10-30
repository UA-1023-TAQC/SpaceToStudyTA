import allure

from SpaceToStudy.api.subjects.client import SubjectsApiClient
from tests.api.api_test_runners import BaseAPITestRunner
from tests.utils.value_provider import ValueProvider

UNAUTHORIZED_RESPONSE = {
    "status": 401,
    "code": "UNAUTHORIZED",
    "message": "The requested URL requires user authorization."
}


class TestAPISubjects(BaseAPITestRunner):
    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/496")
    def test_get_subject_by_id_unauthorized(self):
        client = SubjectsApiClient(ValueProvider.get_base_api_url())
        response = client.get_subject_by_id("648850c4fdc2d1a130c24aea")
        self.assertEqual(401, response.status_code)
        self.assertEqual(UNAUTHORIZED_RESPONSE, response.json())

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/497")
    def test_get_all_subjects_unauthorized(self):
        client = SubjectsApiClient(ValueProvider.get_base_api_url())
        response = client.get_subjects()
        self.assertEqual(401, response.status_code)
        self.assertEqual(UNAUTHORIZED_RESPONSE, response.json())

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/498")
    def test_post_subject_unauthorized(self):
        client = SubjectsApiClient(ValueProvider.get_base_api_url())
        response = client.post_subjects({"name": "Klingon", "category": "64884fedfdc2d1a130c24ade"})
        self.assertEqual(401, response.status_code)
        self.assertEqual(UNAUTHORIZED_RESPONSE, response.json())

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/499")
    def test_patch_subject_unauthorized(self):
        client = SubjectsApiClient(ValueProvider.get_base_api_url())
        response = client.patch_subject_by_id("64885121fdc2d1a130c24afc", {"name": "Klingon"})
        self.assertEqual(401, response.status_code)
        self.assertEqual(UNAUTHORIZED_RESPONSE, response.json())
