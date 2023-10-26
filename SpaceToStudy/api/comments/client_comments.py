import requests

from SpaceToStudy.api.base_api_client import BaseAPIClient


class CommentsAPIClient(BaseAPIClient):
    def __init__(self, url, access_token=None):
        super().__init__(url, access_token)
        self.url += "cooperations"

    def get_comments(self, cooperation_id):
        url = f"{self.url}/{cooperation_id}/comments"
        response = requests.get(url, headers={"Authorization": f"Bearer {self.access_token}"})
        return response
