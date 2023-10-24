import requests

from SpaceToStudy.api.base_api_client import BaseAPIClient


class ReviewsApiClient(BaseAPIClient):
    def __init__(self, url, access_token=None):
        super().__init__(url, access_token)
        self.url += "reviews"

    def get_all_reviews(self, rating=None, skip=None, limit=None):
        url = f"{self.url}"
        params = {
            "rating": rating,
            "skip": skip,
            "limit": limit
        }
        if any(params.values()):
            _params = "&".join([f"{key}={value}" for key, value in params.items() if value is not None])
            url += f"?{_params}"
        response = requests.get(url, headers={"Authorization": f"Bearer {self.access_token}"})
        return response
