import allure

from SpaceToStudy.api.comments.client_comments import CommentsAPIClient
from SpaceToStudy.api.comments.schemas import SCHEMA_FOR_ALL_COMMENTS, SCHEMA_FOR_COMMENTS

from tests.api.api_test_runners import APITestRunnerWithStudent
from tests.utils.value_provider import ValueProvider
from jsonschema import validate


class TestAPIComments(APITestRunnerWithStudent):

    def test_get_comments(self):
        client = CommentsAPIClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_comments("65097f598f5d654793fed7ef")
        self.assertEqual(response.status_code, 200)
        validate(instance=response.json(), schema=SCHEMA_FOR_ALL_COMMENTS)

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/462")
    def test_post_comment(self):
        data = {
            "text": "Test comment"
        }
        client = CommentsAPIClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.post_new_comment("65097f598f5d654793fed7ef", data=data)
        self.assertEqual(201, response.status_code)
        self.assertEqual(response.json()["text"], "Test comment")
        validate(instance=response.json(), schema=SCHEMA_FOR_COMMENTS)
