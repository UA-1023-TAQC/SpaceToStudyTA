import allure
import requests

from SpaceToStudy.api.base_api_client import BaseAPIClient


class QuestionsAPIClient(BaseAPIClient):
    def __init__(self, url, access_token=None):
        super().__init__(url, access_token)
        self.url += "questions"

    @allure.step("Obtaining a list of questions")
    def get_questions(self):
        url = f"{self.url}"
        response = requests.get(url, cookies={'accessToken': self.access_token})
        return response

    @allure.step("Getting a questions by ID")
    def get_questions_by_id(self, questions_id):
        url = f"{self.url}/{questions_id}"
        response = requests.get(url, cookies={'accessToken': self.access_token})
        return response

    @allure.step("Post a new question")
    def post_question(self, data):
        url = f"{self.url}"
        response = requests.post(url, cookies={'accessToken': self.access_token}, json=data)
        return response
