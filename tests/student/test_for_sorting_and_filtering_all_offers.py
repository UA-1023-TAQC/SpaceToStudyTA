from time import sleep

from selenium.webdriver.common.by import By

from SpaceToStudy.ui.pages.explore_offers.explore_offers_page import ExploreOffersPage, LIST_OF_OFFERS
from SpaceToStudy.ui.pages.explore_offers.search_by_tutor_name_component import SearchByTutorNameComponent
from SpaceToStudy.ui.pages.home_page.home_student import HomePageStudent

from tests.test_runners import TestRunnerWithStudent


class SortingAndFilteringAllOffersTestCase(TestRunnerWithStudent):

    def setUp(self):
        super().setUp()
        home_page_student = HomePageStudent(self.driver)
        (home_page_student.click_button_go_to_categories()
                          .click_show_all_offers_btn())

    def test_filters_by_category_subject_and_tutors_name(self):
        explore_offers_page = ExploreOffersPage(self.driver)
        (explore_offers_page.get_search_by_tutor_name_block()
                            .set_categories_input("Music")
                            .navigate_categories_input_down()
                            .choose_categories_item()
                            .set_subjects_input("Guitar")
                            .navigate_subjects_input_down()
                            .choose_subjects_item()
                            .set_search_by_tutor_name_input("Yura")
                            .click_search_btn())

        list_of_filtered_offers = ExploreOffersPage(self.driver.find_element(*LIST_OF_OFFERS))
        self.assertEqual(len(list_of_filtered_offers.get_list_of_filtered_offers()), 2)
        for offer in list_of_filtered_offers.get_list_of_filtered_offers():
            self.assertEqual("GUITAR", offer.get_subject_label())
            self.assertIn("Yura", offer.get_person_name())
