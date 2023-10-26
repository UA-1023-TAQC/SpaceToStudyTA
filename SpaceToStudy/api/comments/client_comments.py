import allure
import requests

from SpaceToStudy.api.base_api_client import BaseAPIClient


class CommentsAPIClient(BaseAPIClient):
    def __init__(self, url, access_token=None):
        super().__init__(url, access_token)
        self.url += "cooperations"

    @allure.step("Receiving cooperation comments")
    def get_comments(self, cooperation_id):
        """
        Gets comments to collaborate with the specified ID.
        :param cooperation_id: ID of the collaboration for which you want to get comments.
        :return: A response object from the server with a list of comments.
        """
        url = f"{self.url}/{cooperation_id}/comments"
        response = requests.get(url, headers={"Authorization": f"Bearer {self.access_token}"})
        return response
