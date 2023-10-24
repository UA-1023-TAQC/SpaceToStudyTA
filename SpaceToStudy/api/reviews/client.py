import requests

from SpaceToStudy.api.base_api_client import BaseAPIClient


class ReviewsApiClient(BaseAPIClient):
    def __init__(self, url, access_token=None):
        super().__init__(url, access_token)
        self.url += "reviews"

    def get_all_reviews(self):
        url = f"{self.url}"
        response = requests.get(url, headers={"Authorization": f"Bearer {self.access_token}"})
        return response
