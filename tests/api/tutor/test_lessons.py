import allure
from jsonschema import validate

from SpaceToStudy.api.lessons.client import LessonsApiClient
from SpaceToStudy.api.lessons.schemas import SCHEMA_FOR_ALL_LESSONS, SCHEMA_FOR_POST_LESSON, SCHEMA_FOR_LESSON_BY_ID
from tests.api.api_test_runners import APITestRunnerWithTutor
from tests.utils.value_provider import ValueProvider


class TestAPILessons(APITestRunnerWithTutor):

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/475")
    def test_find_all_lessons(self):
        client = LessonsApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_lessons()
        self.assertEqual(200, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_ALL_LESSONS)

    # def post_and_delete_lesson(self):
    #     data_for_post = {
    #       TBD
    #     }
    #     client = LessonsApiClient(ValueProvider.get_base_api_url(), self.accessToken)
    #     response = client.post_lesson(data_for_post)
    #     self.assertEqual(201, response.status_code)
    #     validate(instance=response.json(), schema=SCHEMA_FOR_POST_LESSON)

    def test_get_lesson_by_id(self):
        client = LessonsApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_lesson_by_id("64e24191c46e2c44c5bc387f")
        self.assertEqual(200, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_LESSON_BY_ID)
        self.assertIn("Guitar", response.json()["title"])

    # CURRENTLY EDITING LESSON IS NOT WORKING ON WEBSITE
    # def test_patch_lesson_by_id(self):
    #     data_for_patch = {
    #         "title": "new title"
    #     }
    #     client = LessonsApiClient(ValueProvider.get_base_api_url(), self.accessToken)
    #     # get current title value
    #     current_title = client.get_lesson_by_id("64e24191c46e2c44c5bc387f").json()["title"]
    #     # patch
    #     response = client.patch_lesson_by_id("64e24191c46e2c44c5bc387f", data_for_patch)
    #     self.assertEqual(204, response.status_code)
    #     self.assertNotEqual(current_title, response.json()["title"])
    #     # return to original value
    #     response = client.patch_lesson_by_id("64e24191c46e2c44c5bc387f", {"title": current_title})
    #     self.assertEqual(204, response.status_code)
