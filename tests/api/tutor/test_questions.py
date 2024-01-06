import allure
from api.questions.client_questions import QuestionsAPIClient
from api.questions.schemas import ALL_QUESTIONS_SCHEMA, POST_QUESTIONS_SCHEMA
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

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/545")
    def test_find_questions_by_id(self):
        client = QuestionsAPIClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_questions_by_id("6599b0dd671d6db6ce5f2b70")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('_id'), "6599b0dd671d6db6ce5f2b70")
        self.assertEqual(response.json().get('title'), "Test")

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/546")
    def test_post_new_question(self):
        data = {
            "title": "Test",
            "text": "What is the chemical symbol for water?",
            "answers": [
                {
                    "text": "First answer2",
                    "isCorrect": True
                },
                {
                    "text": "Second answer",
                    "isCorrect": False
                }
            ],
            "type": "multipleChoice",
            "category": "6477007a6fa4d05e1a800ce1"
        }
        client = QuestionsAPIClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.post_question(data=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json().get('title'), "Test")
        validate(instance=response.json(), schema=POST_QUESTIONS_SCHEMA)

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/547")
    def test_patch_quizzes(self):
        data = {
            "title": "Test update title"
        }
        client = QuestionsAPIClient(ValueProvider.get_base_api_url(), self.accessToken)
        quizzes_response = client.get_questions().json()['items'][0]['_id']
        print(quizzes_response)
        response = client.patch_questions(quizzes_response, data=data)
        self.assertEqual(response.status_code, 204)

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/548")
    def test_delete_quizzes(self):
        client = QuestionsAPIClient(ValueProvider.get_base_api_url(), self.accessToken)
        question_response = client.get_questions().json()['items'][0]['_id']
        response = client.delete_question(question_response)
        self.assertEqual(response.status_code, 204)
