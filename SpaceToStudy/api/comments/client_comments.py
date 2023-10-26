import allure
import requests

from SpaceToStudy.api.base_api_client import BaseAPIClient


class CommentsAPIClient(BaseAPIClient):
    def __init__(self, url, access_token=None):
        super().__init__(url, access_token)
        self.url += "cooperations"

    def get_comments(self, cooperation_id):
        url = f"{self.url}/{cooperation_id}/comments"
        response = requests.get(url, headers={"Authorization": f"Bearer {self.access_token}"})
        return response

    @allure.step("Create a new comment")
    def post_new_comment(self, cooperation_id, data):
        """
        :param cooperation_id: ID of the collaboration to add a comment to.
        :param data: Data for a new comment in JSON format.
        :return: The object of the response from the server.
        """
        url = f"{self.url}/{cooperation_id}/comments"
        response = requests.post(url, headers={"Authorization": f"Bearer {self.access_token}"}, json=data)
        return response
