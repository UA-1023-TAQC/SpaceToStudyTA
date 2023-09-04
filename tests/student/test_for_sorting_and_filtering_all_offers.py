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

    def test_toggle_between_tutors_offers_and_students_requests(self):
        explore_offers_page = ExploreOffersPage(self.driver)
        filtering_sorting_block = explore_offers_page\
            .get_filtering_and_sorting_block()

        # Toggle to students' requests
        filtering_sorting_block.click_toggle()
        self.assertIn("authorRole=student", self.driver.current_url)

        # Check the text color
        tutors_offers_text_color = filtering_sorting_block\
            .get_tutors_offers()\
            .value_of_css_property("color")
        students_requests_text_color = filtering_sorting_block\
            .get_students_requests()\
            .value_of_css_property("color")
        self.assertEqual(tutors_offers_text_color, "rgba(96, 125, 139, 1)")
        self.assertEqual(students_requests_text_color, "rgba(38, 50, 56, 1)")

        # Toggle back to tutors' offers
        filtering_sorting_block.click_toggle()
        self.assertIn("authorRole=tutor", self.driver.current_url)

        # Check the text color again
        tutors_offers_text_color = filtering_sorting_block\
            .get_tutors_offers()\
            .value_of_css_property("color")
        students_requests_text_color = filtering_sorting_block\
            .get_students_requests()\
            .value_of_css_property("color")
        self.assertEqual(tutors_offers_text_color, "rgba(38, 50, 56, 1)")
        self.assertEqual(students_requests_text_color, "rgba(96, 125, 139, 1)")