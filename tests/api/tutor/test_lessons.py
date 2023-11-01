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

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/487")
    def test_post_and_delete_lesson(self):
        data_for_post = {
          "title": "Test POST for API",
          "description": "With this lesson I test POST for API",
          "content": "<h1>POST successful. Content cannot be shorter than 50 symbol. "
                     "Content cannot be shorter than 50 symbol.</h1>",
          "author": "64d90c1b22b6575c0af37c1f",
          "attachments": [],
          "category": "64884f21fdc2d1a130c24ac0"
        }
        client = LessonsApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        # post
        response = client.post_lesson(data_for_post)
        self.assertEqual(201, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_POST_LESSON)
        # delete
        new_response = client.delete_lesson_by_id(response.json()["_id"])
        self.assertEqual(204, new_response.status_code)

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/485")
    def test_get_lesson_by_id(self):
        client = LessonsApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_lesson_by_id("64e24191c46e2c44c5bc387f")
        self.assertEqual(200, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_LESSON_BY_ID)
        self.assertIn("Guitar", response.json()["title"])

    # CURRENTLY PATCH IS NOT WORKING. DEVELOPERS ARE INFORMED.
    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/488")
    def test_patch_lesson_by_id(self):
        # test data
        data_for_patch = {
            "title": "new title"
        }
        test_lesson_id = "64e24191c46e2c44c5bc387f"
        # get current title value
        client = LessonsApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        current_title = client.get_lesson_by_id(test_lesson_id).json()["title"]
        # patch
        response = client.patch_lesson_by_id(test_lesson_id, data_for_patch)
        self.assertEqual(204, response.status_code)
        self.assertNotEqual(current_title, response.json()["title"])
        # return to original value
        response = client.patch_lesson_by_id(test_lesson_id, {"title": current_title})
        self.assertEqual(204, response.status_code)
