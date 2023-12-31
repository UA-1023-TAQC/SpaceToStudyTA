import allure
from jsonschema import validate

from SpaceToStudy.api.categories.client import CategoriesApiClient
from SpaceToStudy.api.categories.schemas import (SCHEMA_FOR_ALL_CATEGORIES,
                                                 SCHEMA_CATEGORIES_BY_ID,
                                                 SCHEMA_FOR_SUBJECTS_BY_CATEGORY_ID,
                                                 SCHEMA_FOR_SUBJECTS_NAMES_BY_CATEGORY_ID)
from tests.api.api_test_runners import APITestRunnerWithStudent
from tests.utils.value_provider import ValueProvider


class TestAPICategories(APITestRunnerWithStudent):

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/388")
    def test_find_all_categories(self):
        client = CategoriesApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_categories()
        self.assertEqual(response.status_code, 200)
        validate(instance=response.json(), schema=SCHEMA_FOR_ALL_CATEGORIES)

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/423")
    def test_get_subjects_by_category_id(self):
        client = CategoriesApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_subjects_by_category_id("64884f21fdc2d1a130c24ac0")
        self.assertEqual(response.status_code, 200)
        validate(instance=response.json(), schema=SCHEMA_FOR_SUBJECTS_BY_CATEGORY_ID)
        self.assertEqual(response.json()["count"], len(response.json()["items"]))

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/408")
    def test_get_categories_by_id(self):
        client = CategoriesApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_categories_by_id("64884f21fdc2d1a130c24ac0")
        self.assertEqual(response.status_code, 200)
        validate(instance=response.json(), schema=SCHEMA_CATEGORIES_BY_ID)
        self.assertEquals(response.json()["name"], "Music")

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/418")
    def test_get_subjects_names_by_category_id(self):
        client = CategoriesApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = client.get_subjects_names_by_id("64884f21fdc2d1a130c24ac0")
        self.assertEquals(response.status_code, 200)
        validate(instance=response.json(), schema=SCHEMA_FOR_SUBJECTS_NAMES_BY_CATEGORY_ID)
        names = [item["name"] for item in response.json()]
        self.assertIn("Guitar", names)
        self.assertIn("Piano", names)
