import allure
import requests

from SpaceToStudy.api.base_api_client import BaseAPIClient


class ChatsAPIClient(BaseAPIClient):
    def __init__(self, url, access_token=None):
        super().__init__(url, access_token)
        self.url += "chats"

    @allure.step("Post chat")
    def post_chat(self, chat_data):
        url = f"{self.url}"
        response = requests.post(url, json=chat_data, headers={"Authorization": f"Bearer {self.access_token}"})
        return response

    @allure.step("Get all chats for current user")
    def get_chats(self):
        url = f"{self.url}"
        response = requests.get(url, headers={"Authorization": f"Bearer {self.access_token}"})
        return response

    @allure.step("Get messages in chat by its {chat_id}")
    def get_messages_in_chat_by_id(self, chat_id):
        url = f"{self.url}/{chat_id}/messages"
        response = requests.get(url, headers={"Authorization": f"Bearer {self.access_token}"})
        return response

    @allure.step("Delete messages from the chat by its {id}")
    def delete_messages_from_chat_by_id(self, chat_id):
        url = f"{self.url}/{chat_id}/messages"
        response = requests.delete(url, headers={"Authorization": f"Bearer {self.access_token}"})
        return response

    @allure.step("Delete chat by its {id}")
    def delete_chat_by_id(self, chat_id):
        url = f"{self.url}/{chat_id}"
        response = requests.delete(url, headers={"Authorization": f"Bearer {self.access_token}"})
        return response
