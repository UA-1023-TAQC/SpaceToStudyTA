import allure
from jsonschema import validate

from SpaceToStudy.api.categories.client import CategoriesApiClient
from SpaceToStudy.api.subjects.client import SubjectsApiClient
from SpaceToStudy.api.subjects.schemas import SCHEMA_FOR_ALL_SUBJECTS, SCHEMA_FOR_SUBJECTS_BY_ID
from tests.api.api_test_runners import APITestRunnerWithStudent
from tests.utils.value_provider import ValueProvider


class TestAPISubjects(APITestRunnerWithStudent):

    def test_find_all_subjects(self):
        client = SubjectsApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_subjects()
        self.assertEqual(200, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_ALL_SUBJECTS)

    def test_post_and_delete_subject(self):
        test_data = {"name": "Klingon", "category": "64884fedfdc2d1a130c24ade"}

        # Check that initial list doesn't contain test data
        client = CategoriesApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_subjects_names_by_id(test_data["category"])
        self.assertEqual(200, response.status_code)
        names = [item["name"] for item in response.json()]
        self.assertNotIn(test_data["name"], names)

        # Create new subject with test data
        client = SubjectsApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.post_subjects(test_data)
        self.assertEqual(201, response.status_code)

        # Check that the subject name from test data is in the list for category
        client = CategoriesApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_subjects_names_by_id(test_data["category"])
        self.assertEqual(200, response.status_code)
        names = [item["name"] for item in response.json()]
        self.assertIn(test_data["name"], names)

        # Delete the subject
        client = SubjectsApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.delete_subject_by_name(test_data["name"])
        self.assertEqual(204, response.status_code)

    def test_get_subject_by_id(self):
        test_data = {"name": "Guitar", "category": "648850c4fdc2d1a130c24aea"}
        client = SubjectsApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_subject_by_id(test_data["category"])
        self.assertEqual(200, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_SUBJECTS_BY_ID)
        self.assertEqual(test_data["name"], response.json()["name"])
