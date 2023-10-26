import allure
import requests

from SpaceToStudy.api.base_api_client import BaseAPIClient


class CooperationsApiClient(BaseAPIClient):
    def __init__(self, url, access_token=None):
        super().__init__(url, access_token)
        self.url += "cooperations"

    @allure.step("Get cooperations")
    def get_cooperations(self):
        url = f"{self.url}"
        response = requests.get(url, headers={"Authorization": f"Bearer {self.access_token}"})
        return response