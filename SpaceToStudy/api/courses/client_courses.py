import allure
import requests

from SpaceToStudy.api.base_api_client import BaseAPIClient


class CoursesApiClient(BaseAPIClient):
    def __init__(self, url, access_token=None):
        super().__init__(url, access_token)
        self.url += "courses"

    def get_courses(self, skip=None, limit=None):
        url = f"{self.url}"
        params = {
            "skip": skip,
            "limit": limit
        }
        if any(params.values()):
            _params = "&".join([f"{key}={value}" for key, value in params.items() if value is not None])
            url += f"?{_params}"
        response = requests.get(url, headers={"Authorization": f"Bearer {self.access_token}"})
        return response

    def get_courses_by_id(self, courses_id):
        url = f"{self.url}/{courses_id}"
        response = requests.get(url, headers={"Authorization": f"Bearer {self.access_token}"})
        return response

    @allure.step("Create a new course")
    def post_new_course(self, data):
        url = f"{self.url}"
        response = requests.post(url, json=data, headers={"Authorization": f"Bearer {self.access_token}"})
        return response
