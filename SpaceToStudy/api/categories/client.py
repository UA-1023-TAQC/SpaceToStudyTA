import allure
import requests

from SpaceToStudy.api.base_api_client import BaseAPIClient

class CategoriesApiClient(BaseAPIClient):
    def __init__(self, url, access_token=None):
        super().__init__(url, access_token)
        self.url += "categories"

    @allure.step("Get all categories")
    def get_categories(self, match=None, skip=None, limit=None):
        url = f"{self.url}"
        params = {
            "match": match,
            "skip": skip,
            "limit": limit
        }
        if any(params.values()):
            _params = "&".join([f"{key}={value}" for key, value in params.items() if value is not None])
            url += f"?{_params}"

        response = requests.get(url, headers={"Authorization": f"Bearer {self.access_token}"})
        return response

    @allure.step("Get subjects names by id")
    def get_subjects_names_by_id(self, category_id):
        "/ categories / {id} / subjects / names"
        url = f"{self.url}/{category_id}/subjects/names"
        response = requests.get(url, headers={"Authorization": f"Bearer {self.access_token}"})
        return response

    @allure.step("Get categories by id")
    def get_categories_by_id(self, category_id):
        "/ categories / {id}"
        url = f"{self.url}/{category_id}"
        response = requests.get(url, headers={"Authorization": f"Bearer {self.access_token}"})
        return response

    @allure.step("Get subjects by category id")
    def get_subjects_by_category_id(self, category_id, name=None):
        url = f"{self.url}/{category_id}/subjects"
        if name:
            url += f"?name={name}"
        response = requests.get(url, headers={"Authorization": f"Bearer {self.access_token}"})
        return response
