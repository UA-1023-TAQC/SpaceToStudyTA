import allure

from SpaceToStudy.api.quizzes.client_quizzes import QuizzesAPIClient
from SpaceToStudy.api.quizzes.schemas import ALL_QUIZZES_SCHEMA
from tests.api.api_test_runners import APITestRunnerWithTutor
from tests.utils.value_provider import ValueProvider
from jsonschema import validate


class TestAPIQuizzes(APITestRunnerWithTutor):
    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/480")
    def test_find_all_quizzes(self):
        client = QuizzesAPIClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_quizzes()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["count"], len(response.json()["items"]))
        validate(instance=response.json(), schema=ALL_QUIZZES_SCHEMA)

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/480")
    def test_find_quizzes_by_id(self):
        client = QuizzesAPIClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_quizzes_by_id("653b92fdc74d71b4d2d7efb0")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('_id'), "653b92fdc74d71b4d2d7efb0")
        self.assertEqual(response.json().get('title'), "Assembly")
