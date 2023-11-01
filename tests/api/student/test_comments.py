import allure

from SpaceToStudy.api.comments.client_comments import CommentsAPIClient
from SpaceToStudy.api.comments.schemas import SCHEMA_FOR_COMMENTS
from tests.api.api_test_runners import APITestRunnerWithStudent
from tests.utils.value_provider import ValueProvider
from jsonschema import validate


class TestAPIComments(APITestRunnerWithStudent):
    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/461")
    def test_get_comments(self):
        client = CommentsAPIClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_comments("65097f598f5d654793fed7ef")
        self.assertEqual(response.status_code, 200)
        validate(instance=response.json(), schema=SCHEMA_FOR_COMMENTS)
