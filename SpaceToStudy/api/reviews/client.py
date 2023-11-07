import allure
import requests

from SpaceToStudy.api.base_api_client import BaseAPIClient


class ReviewsApiClient(BaseAPIClient):
    def __init__(self, url, access_token=None):
        super().__init__(url, access_token)
        self.url += "reviews"

    @allure.step("Get all reviews")
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

    @allure.step("Get review by id")
    def get_reviews_by_id(self, review_id):
        url = f"{self.url}/{review_id}"
        response = requests.get(url, headers={"Authorization": f"Bearer {self.access_token}"})
        return response

    @allure.step("Post new review")
    def post_review(self, data):
        url = f"{self.url}"
        response = requests.post(url, data, headers={"Authorization": f"Bearer {self.access_token}"})
        return response

    @allure.step("Patch review by id")
    def patch_review(self, review_id, data):
        url = f"{self.url}/{review_id}"
        response = requests.patch(url, data, headers={"Authorization": f"Bearer {self.access_token}"})
        return response

    @allure.step("Delete review by id")
    def delete_review(self, review_id):
        url = f"{self.url}/{review_id}"
        response = requests.delete(url, headers={"Authorization": f"Bearer {self.access_token}"})
        return response
