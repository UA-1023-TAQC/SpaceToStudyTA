import requests

from SpaceToStudy.api.base_api_client import BaseAPIClient


class SubjectsApiClient(BaseAPIClient):
    def __init__(self, url, access_token=None):
        super().__init__(url, access_token)
        self.subject_id = None
        self.url += "subjects"

    def get_subjects(self):
        response = requests.get(self.url, headers={"Authorization": f"Bearer {self.access_token}"})
        return response

    def post_subjects(self, data):
        response = requests.post(self.url, headers={"Authorization": f"Bearer {self.access_token}"}, json=data)
        return response

    def delete_subject(self, subject_id):
        response = requests.delete(f"{self.url}/{subject_id}", headers={"Authorization": f"Bearer {self.access_token}"})
        return response

    def delete_subject_by_name(self, name):
        self.find_subject_id_by_name(name)
        response = requests.delete(f"{self.url}/{self.subject_id}", headers={"Authorization": f"Bearer {self.access_token}"})
        return response

    def find_subject_id_by_name(self, name):
        response = requests.get(f"{self.url}", headers={"Authorization": f"Bearer {self.access_token}"})
        if response.status_code == 200:
            for item in response.json().get("items", []):
                if item.get("name") == name:
                    self.subject_id = item.get("_id")
            return self.subject_id
