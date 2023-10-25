import allure
from jsonschema import validate

from SpaceToStudy.api.reviews.client import ReviewsApiClient
from SpaceToStudy.api.reviews.schemas import SCHEMA_FOR_ALL_REVIEWS, SCHEMA_FOR_REVIEW_BY_ID
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

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/445")
    def test_get_reviews_by_id(self):
        client = ReviewsApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_reviews_by_id("642d3dcac160fddf141253ba")
        self.assertEqual(200, response.status_code)
        validate(instance=response.json(), schema=SCHEMA_FOR_REVIEW_BY_ID)
        self.assertEqual(response.json()["comment"], "cool")

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/446")
    def test_post_patch_delete_reviews(self):
        test_data_for_post = {
          "comment": "API POST works!",
          "rating": 5,
          "author": "64d525d214232a210a0c7dd9",
          "targetUserId": "65219063e763fa892a0a1e88",
          "targetUserRole": "tutor",
          "offer": "6526e2cbe947d115f1a5dc25"
        }

        # Post
        client = ReviewsApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.post_review(test_data_for_post)
        self.assertEqual(201, response.status_code)
        review_id = response.json()["_id"]

        # Patch
        test_data_for_patch = {
          "comment": "API PATCH works!",
        }
        client = ReviewsApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.patch_review(review_id, test_data_for_patch)
        self.assertEqual(204, response.status_code)
        check_patch_worked = client.get_reviews_by_id(review_id).json()["comment"] == test_data_for_patch["comment"]
        self.assertTrue(check_patch_worked)

        # Delete
        client = ReviewsApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.delete_review(review_id)
        self.assertEqual(204, response.status_code)
