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