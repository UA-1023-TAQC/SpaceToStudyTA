import allure

from SpaceToStudy.ui.pages.explore_offers.explore_offers_page import ExploreOffersPage
from SpaceToStudy.ui.pages.home_page.home_tutor import HomePageTutor
from tests.test_runners import TestRunnerWithTutor


class ExploreOffersTest(TestRunnerWithTutor):

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/372")
    def test_explore_offers_is_available(self):

        explore_offers_title = HomePageTutor(self.driver).click_find_student_btn().get_title()
        self.assertTrue(explore_offers_title.is_displayed())
        offers_list = ExploreOffersPage(self.driver).get_list_of_offers_inline_card()
        self.assertTrue(len(offers_list) > 0)

