import requests

from SpaceToStudy.api.base_api_client import BaseAPIClient


class LessonsApiClient(BaseAPIClient):
    def __init__(self, url, access_token=None):
        super().__init__(url, access_token)
        self.url += "lessons"

    def get_lessons(self, title=None, sort=None, limit=None, skip=None):
        url = f"{self.url}"
        params = {
            "title": title,
            "sort": sort,
            "limit": limit,
            "skip": skip
        }
        if any(params.values()):
            _params = "&".join([f"{key}={value}" for key, value in params.items() if value is not None])
            url += f"?{_params}"

        response = requests.get(url, headers={"Authorization": f"Bearer {self.access_token}"})
        return response

    def post_lesson(self, data):
        response = requests.post(self.url, headers={"Authorization": f"Bearer {self.access_token}"}, json=data)
        return response

    def get_lesson_by_id(self, lesson_id):
        url = f"{self.url}/{lesson_id}"
        response = requests.get(url, headers={"Authorization": f"Bearer {self.access_token}"})
        return response

    def patch_lesson_by_id(self, lesson_id, data):
        url = f"{self.url}/{lesson_id}"
        response = requests.patch(url, headers={"Authorization": f"Bearer {self.access_token}"}, json=data)
        return response

    def delete_lesson_by_id(self, lesson_id):
        url = f"{self.url}/{lesson_id}"
        response = requests.delete(url, headers={"Authorization": f"Bearer {self.access_token}"})
        return response
