import allure

from SpaceToStudy.api.quizzes.client_quizzes import QuizzesAPIClient
from api.questions.client_questions import QuestionsAPIClient
from api.questions.schemas import ALL_QUESTIONS_SCHEMA
from tests.api.api_test_runners import APITestRunnerWithTutor
from tests.utils.value_provider import ValueProvider
from jsonschema import validate


class TestAPIQuestions(APITestRunnerWithTutor):
    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/544")
    def test_find_all_questions(self):
        client = QuestionsAPIClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_questions()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["count"], len(response.json()["items"]))
        validate(instance=response.json(), schema=ALL_QUESTIONS_SCHEMA)