import requests

from SpaceToStudy.api.base_api_client import BaseAPIClient


class SubjectsApiClient(BaseAPIClient):
    def __init__(self, url, access_token=None):
        super().__init__(url, access_token)
        self.url += "subjects"

    def get_subjects(self):
        response = requests.get(self.url, headers={"Authorization": f"Bearer {self.access_token}"})
        return response
