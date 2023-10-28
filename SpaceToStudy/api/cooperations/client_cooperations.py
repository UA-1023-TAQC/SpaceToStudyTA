import allure
import requests

from SpaceToStudy.api.base_api_client import BaseAPIClient


class CooperationApiClient(BaseAPIClient):
    def __init__(self, url, access_token=None):
        super().__init__(url, access_token)
        self.url += "cooperations"

    @allure.step("Get cooperation")
    def get_cooperation(self):
        url = f"{self.url}"
        response = requests.get(url, headers={"Authorization": f"Bearer {self.access_token}"})
        return response

    @allure.step("Get cooperation by id")
    def get_cooperation_by_id(self, cooperation_id):
        url = f"{self.url}/{cooperation_id}"
        response = requests.get(url, headers={"Authorization": f"Bearer {self.access_token}"})
        return response

    @allure.step("Post cooperation")
    def post_cooperation(self, data):
        response = requests.post(self.url, headers={"Authorization": f"Bearer {self.access_token}"}, json=data)
        return response

    @allure.step("Patch cooperation")
    def patch_cooperation(self, cooperation_id, data):
        url = f"{self.url}/{cooperation_id}"
        response = requests.patch(url, headers={"Authorization": f"Bearer {self.access_token}"}, json=data)
        return response