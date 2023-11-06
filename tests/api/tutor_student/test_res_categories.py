import unittest

import allure
from jsonschema import validate
from parameterized import parameterized_class

from SpaceToStudy.api.res_categories.client import ResoursesCategoriesApiClient
from SpaceToStudy.api.schema_for_errors import SCHEMA_FOR_ERRORS
from tests.api.api_test_runners import BaseAPITestRunner, get_access_token
from tests.utils.value_provider import ValueProvider as VP
from parameterized import parameterized


class TestResCategoriesApiWithAuthorizedUser(BaseAPITestRunner):
    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/436")
    @parameterized.expand([
        (VP.get_student_first_name(), get_access_token(VP.get_student_email(), VP.get_student_password()), 403),
        (VP.get_tutor_first_name(),   get_access_token(VP.get_tutor_email(), VP.get_tutor_password()), 200),
    ])
    def test_get_res_categories_authorized_user(self, name, token, exp_status_code):
        client = ResoursesCategoriesApiClient(VP.get_base_api_url(), token)
        response = client.get_res_categories()
        self.assertEqual(exp_status_code, response.status_code)
