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

    @allure.step("Creating a new quizzes")
    def post_quizzes(self, data):
        url = f"{self.url}"
        response = requests.post(url, headers={"Authorization": f"Bearer {self.access_token}"}, json=data)
        allure.attach(f"Request: POST {url}\nData: {data}\n"
                      f"Response: {response.status_code} - {response.text}")
        return response

    @allure.step("Updating the quizzes by ID")
    def patch_quizzes(self, quizzes_id, data):
        url = f"{self.url}/{quizzes_id}"
        response = requests.patch(url, headers={"Authorization": f"Bearer {self.access_token}"}, json=data)
        return response
