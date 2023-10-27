import allure
import requests

from SpaceToStudy.api.base_api_client import BaseAPIClient


class QuizzesAPIClient(BaseAPIClient):
    def __init__(self, url, access_token=None):
        super().__init__(url, access_token)
        self.url += "quizzes"

    @allure.step("Obtaining a list of quizzes")
    def get_quizzes(self):
        url = f"{self.url}"
        response = requests.get(url, headers={"Authorization": f"Bearer {self.access_token}"})
        return response

    @allure.step("Getting a quizzes by ID")
    def get_quizzes_by_id(self, quizzes_id):
        url = f"{self.url}/{quizzes_id}"
        response = requests.get(url, headers={"Authorization": f"Bearer {self.access_token}"})
        return response
