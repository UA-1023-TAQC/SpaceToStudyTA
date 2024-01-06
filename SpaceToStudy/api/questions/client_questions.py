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
