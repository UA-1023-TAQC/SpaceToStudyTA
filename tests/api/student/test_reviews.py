import allure
from jsonschema import validate

from SpaceToStudy.api.reviews.client import ReviewsApiClient
from SpaceToStudy.api.reviews.schemas import SCHEMA_FOR_ALL_REVIEWS
from tests.api.api_test_runners import APITestRunnerWithStudent
from tests.utils.value_provider import ValueProvider


class TestAPIReviews(APITestRunnerWithStudent):

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/444")
    def test_get_all_reviews(self):
        client = ReviewsApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_all_reviews(rating=5, skip=1, limit=5)
        self.assertEqual(200, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_ALL_REVIEWS)
        self.assertTrue(all(item["rating"] == 5 for item in response.json()["reviews"]))
