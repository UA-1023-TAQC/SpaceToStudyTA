import allure
from jsonschema import validate

from SpaceToStudy.api.subjects.client import SubjectsApiClient
from SpaceToStudy.api.subjects.schemas import SCHEMA_FOR_ALL_SUBJECTS
from tests.api.api_test_runners import APITestRunnerWithStudent
from tests.utils.value_provider import ValueProvider


class TestAPISubjects(APITestRunnerWithStudent):

    def test_find_all_subjects(self):
        client = SubjectsApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_subjects()
        self.assertEqual(response.status_code, 200)
        validate(instance=response.json(), schema=SCHEMA_FOR_ALL_SUBJECTS)