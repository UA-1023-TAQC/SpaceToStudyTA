import allure
import requests

from SpaceToStudy.api.base_api_client import BaseAPIClient


class UsersApiClient(BaseAPIClient):
    def __init__(self, url, access_token=None):
        super().__init__(url, access_token)
        self.url += "users"

    @allure.step("Get all users")
    def get_users(self):
        url = f"{self.url}"
        response = requests.get(url, headers={"Authorization": f"Bearer {self.access_token}"})
        return response

    @allure.step("Get user by ID")
    def get_users_by_id(self, user_id, role=None):
        url = f"{self.url}/{user_id}"
        params = {
            "role": role
        }
        response = requests.get(url, params=params, headers={"Authorization": f"Bearer {self.access_token}"})
        return response

    @allure.step("Get reviews for user by ID and role")
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

    @allure.step("Get review statistics for user by ID and role")
    def get_review_statistics_for_user_by_id(self, user_id, role=None):
        url = f"{self.url}/{user_id}/reviews/stats"
        params = {
            "role": role
        }
        response = requests.get(url, params=params, headers={"Authorization": f"Bearer {self.access_token}"})
        return response

    @allure.step("Get all cooperations for a user with the specified ID")
    def get_cooperations_for_user_by_id(self, user_id):
        url = f"{self.url}/{user_id}/cooperations"
        response = requests.get(url, headers={"Authorization": f"Bearer {self.access_token}"})
        return response

    @allure.step("Get all offers for a user with the specified ID")
    def get_offers_for_user_by_id(self, user_id):
        url = f"{self.url}/{user_id}/offers"
        response = requests.get(url, headers={"Authorization": f"Bearer {self.access_token}"})
        return response

    @allure.step("Patch current user info by ID")
    def patch_current_user_info_by_id(self, user_id, data):
        url = f"{self.url}/{user_id}"
        response = requests.patch(url, headers={"Authorization": f"Bearer {self.access_token}"}, json=data)
        return response

    @allure.step("Patch update user status by id")
    def patch_update_user_status_by_id(self, user_id, data):
        url = f"{self.url}/{user_id}/change-status"
        response = requests.patch(url, headers={"Authorization": f"Bearer {self.access_token}"}, json=data)
        return response
