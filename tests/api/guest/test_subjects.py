from SpaceToStudy.api.subjects.subjects import SubjectsAPIClient
from tests.api.api_test_runners import BaseAPITestRunner, APITestRunnerWithStudent
from tests.utils.value_provider import ValueProvider


class TestAPISubjectsUnAthorized(BaseAPITestRunner):

    def test_find_all_subjects_unauthorized(self):
        expected_status_code = 401
        expected_code = "UNAUTHORIZED"
        expected_message = "The requested URL requires user authorization."
        subjects = SubjectsAPIClient(ValueProvider.get_base_api_url())
        response = subjects.get_subjects()
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_code, response.json().get('code'))
        self.assertEqual(expected_message, response.json().get('message'))
        print(response.status_code)
        print(response.json().get('code'))
        print(response.json().get('message'))

class TestAPISubjectsAthorized(APITestRunnerWithStudent):

    def test_find_all_subjects_student(self):
        client = SubjectsAPIClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_subjects()
        self.assertEqual(response.status_code, 200)
        print(response.status_code)
        for i in range(len(response.json().get('items'))):
            print(response.json().get('items')[i].get('name'))