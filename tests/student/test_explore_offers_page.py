import allure

from SpaceToStudy.ui.pages.home_page.home_student import HomePageStudent
from tests.test_runners import TestRunnerWithStudent
from tests.value_provider import ValueProvider


class TestExploreOffersPageStudent(TestRunnerWithStudent):

    @allure.testcase('https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/215')
    def test_find_tutor_or_category_by_name(self):
        part = " ".join([ValueProvider.get_tutor_first_name(), ValueProvider.get_tutor_last_name()])
        name_tutor = (HomePageStudent(self.driver)
                      .get_search_input()
                      .set_text(part)
                      .click_find_tutor_btn()
                      .get_filtering_and_sorting_block()
                      .click_grid_card_btn()
                      .get_list_of_offers_grid_card()
                      )
        for result in name_tutor:
            self.assertIn(part, result.get_person_name_text())
