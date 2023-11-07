import requests
from SpaceToStudy.api.base_api_client import BaseAPIClient

class ResoursesCategoriesApiClient(BaseAPIClient):
    def __init__(self, url, access_token=None):
        super().__init__(url, access_token)
        self.url += "resources-categories"

    def get_res_categories(self, name=None, sort=None, limit=None, skip=None):
        url = f"{self.url}"
        params = {
            "name": name,
            "sort": sort,
            "limit": limit,
            "skip": skip
        }
        if any(params.values()):
            _params = "&".join([f"{key}={value}" for key, value in params.items() if value is not None])
            url += f"?{_params}"

        response = requests.get(url, headers={"Authorization": f"Bearer {self.access_token}"})
        return response

    def post_res_categories(self, data):
        response = requests.post(self.url, headers={"Authorization": f"Bearer {self.access_token}"}, json=data)
        return response

    def delete_res_categories(self, rc_id):
        response = requests.delete(f"{self.url}/{rc_id}", headers={"Authorization": f"Bearer {self.access_token}"})
        return response

    def patch_res_categories(self, rc_id, data):
        response = requests.patch(f"{self.url}/{rc_id}", headers={"Authorization": f"Bearer {self.access_token}"}, json=data)
        return response

    def get_res_categories_names(self):
        response = requests.get(f"{self.url}/names", headers={"Authorization": f"Bearer {self.access_token}"})
        return response