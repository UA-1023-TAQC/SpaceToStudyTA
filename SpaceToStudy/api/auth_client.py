import requests

from SpaceToStudy.api.base_api_client import BaseAPIClient


class AuthApiClient(BaseAPIClient):
    def __init__(self, url, access_token=None):
        super().__init__(url, access_token)

    def login(self, email, password):
        user_data = {
            "email": email,
            "password": password
        }

        response = requests.post(f"{self.url}auth/login", data=user_data)
        rdata = response.json()
        self.accessToken = rdata.get("accessToken")

    def logout(self):
        logout_url = f"{self.url}auth/logout"
        response = requests.post(logout_url, cookies={"refreshToken": self.access_token})
        return response
