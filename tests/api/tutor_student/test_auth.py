import allure
from parameterized import parameterized_class

from SpaceToStudy.api.auth_client import AuthApiClient
from tests.api.api_test_runners import BaseAPITestRunner, get_access_token
from tests.utils.value_provider import ValueProvider


@parameterized_class([
    {"name:": ValueProvider.get_student_first_name(),
     "accessToken": get_access_token(ValueProvider.get_student_email(), ValueProvider.get_student_password())},
    {"name:": ValueProvider.get_tutor_first_name(),
     "accessToken": get_access_token(ValueProvider.get_tutor_email(), ValueProvider.get_tutor_password())},
])
class TestAPIAuth(BaseAPITestRunner):
    @allure.testcase('https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/415')
    def test_logout(self):
        user = AuthApiClient(ValueProvider.get_base_api_url(), self.accessToken)
        response = user.logout()
        self.assertEqual(response.status_code, 204)
