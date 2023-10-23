import requests

from SpaceToStudy.api.base_api_client import BaseAPIClient


class SubjectsAPIClient(BaseAPIClient):
    def __init__(self, url, access_token=None):
        super().__init__(url, access_token)
        self.url += "subjects"

    def get_subjects(self):
        url = f"{self.url}"
        response = requests.get(url, headers={"Authorization": f"Bearer {self.access_token}"})
        return response

    def get_subjects_names_by_id(self, category_id):
        "/ categories / {id} / subjects / names"
        url = f"{self.url}/{category_id}/subjects/names"
        response = requests.get(url, headers={"Authorization": f"Bearer {self.access_token}"})
        return response

    def get_categories_by_id(self, category_id):
        "/ categories / {id}"
        url = f"{self.url}/{category_id}"
        response = requests.get(url, headers={"Authorization": f"Bearer {self.access_token}"})
        return response

    def get_subjects_by_category_id(self, category_id, name=None):
        url = f"{self.url}/{category_id}/subjects"
        if name:
            url += f"?name={name}"
        response = requests.get(url, headers={"Authorization": f"Bearer {self.access_token}"})
        return response
