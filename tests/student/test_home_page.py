from SpaceToStudy.ui.pages.explore_offers.explore_offers_page import ExploreOffersPage
from SpaceToStudy.ui.pages.home_page.home_student import HomePageStudent
from tests.test_runners import TestRunnerWithStudent


class TestHomePageStudent(TestRunnerWithStudent):

    def test_search_field(self):
        search_result = (HomePageStudent(self.driver)
                         .get_search_input()
                         .set_text("Tutor F")
                         .click_find_tutor_btn()
                         .get_list_of_filtered_offers())
        for result in search_result:
            self.assertIn("Tutor F", result.get_person_name())