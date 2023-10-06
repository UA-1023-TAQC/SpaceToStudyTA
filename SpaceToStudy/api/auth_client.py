import requests

from SpaceToStudy.api.base_api_client import BaseAPIClient


class AuthApiClient(BaseAPIClient):
    def login(self, email, password):
        user_data = {
            "email": email,
            "password": password
        }

        response = requests.post(f"{self.url}auth/login", data=user_data)
        rdata = response.json()
        self.accessToken = rdata.get("accessToken")
