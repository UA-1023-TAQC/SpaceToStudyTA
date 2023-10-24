from SpaceToStudy.api.subjects.subjects import SubjectsAPIClient
from tests.api.api_test_runners import BaseAPITestRunner
from tests.utils.value_provider import ValueProvider


class TestAPISubjects(BaseAPITestRunner):

    def test_find_all_subjects_unauthorized(self):
        expected_status_code = 401
        expected_code = "UNAUTHORIZED"
        expected_message = "The requested URL requires user authorization."
        subjects = SubjectsAPIClient(ValueProvider.get_base_api_url())
        response = subjects.get_subjects()
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_code, response.json().get('code'))
        self.assertEqual(expected_message, response.json().get('message'))
