import allure
import requests

from SpaceToStudy.api.base_api_client import BaseAPIClient


class UsersApiClient(BaseAPIClient):
    def __init__(self, url, access_token=None):
        super().__init__(url, access_token)
        self.url += "users"

    def get_users(self):
        url = f"{self.url}"
        response = requests.get(url, headers={"Authorization": f"Bearer {self.access_token}"})
        return response

    def get_users_by_id(self, user_id, role=None):
        url = f"{self.url}/{user_id}"
        params = {
            "role": role
        }
        response = requests.get(url, params=params, headers={"Authorization": f"Bearer {self.access_token}"})
        return response

    def get_reviews_for_user_by_id(self, user_id, role, rating: int = None, skip: int = 0, limit: int = 5):
        url = f"{self.url}/{user_id}/reviews"
        params = {
            "role": role,
            "rating": rating,
            "skip": skip,
            "limit": limit
        }
        response = requests.get(url, params=params, headers={"Authorization": f"Bearer {self.access_token}"})
        return response

    def get_review_statistics_for_user_by_id(self, user_id, role):
        "/ users / {id} / reviews / stats"
        pass

    @allure.step("Get all cooperations for a user with the specified ID")
    def get_cooperations_for_user_by_id(self, user_id):
        url = f"{self.url}/{user_id}/cooperations"
        response = requests.get(url, headers={"Authorization": f"Bearer {self.access_token}"})
        return response

    def get_offers_for_user_by_id(self, user_id):
        "/ users / {id} / offers"
        pass
