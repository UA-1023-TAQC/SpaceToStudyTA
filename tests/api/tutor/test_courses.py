from SpaceToStudy.api.courses.client_courses import CoursesApiClient
from SpaceToStudy.api.courses.schemas import SCHEMA_FOR_ALL_COURSES
from tests.api.api_test_runners import APITestRunnerWithTutor
from tests.utils.value_provider import ValueProvider
from jsonschema import validate


class TestAPICourses(APITestRunnerWithTutor):

    def test_get_courses(self):
        client = CoursesApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_courses()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["count"], len(response.json()["items"]))
        validate(instance=response.json(), schema=SCHEMA_FOR_ALL_COURSES)

    def test_get_courses_by_id(self):
        client = CoursesApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_courses_by_id()

    def test_post_course(self):
        data = {
            "title": "Test title",
            "description": "Advanced english course with 5 modules and separated lessons for improving speaking, listening and reading.",
            "author": "63da8767c9ad4c9a0b0eacd3",
            "attachments": [
                "63ed1cd25e9d781cdb6a6b15"
            ],
            "lessons": [
                "63ed1cd25e9d781cdb6a6b17",
                "63ac1ad47e9d526cdb6f4n51"
            ]
        }
        client = CoursesApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.post_new_course(data=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["title"], "Test title")
