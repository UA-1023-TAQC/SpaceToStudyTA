import allure

from SpaceToStudy.ui.pages.home_page.home_tutor import HomePageTutor
from tests.ui.test_runners import TestRunnerWithTutor


class HomePageTestCase(TestRunnerWithTutor):
    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/373")
    def test_welcoming_block_ui(self):
        home = HomePageTutor(self.driver)
        self.assertTrue(home.get_find_student_btn().is_displayed())