
import allure

from SpaceToStudy.ui.pages.explore_offers.explore_offers_page import ExploreOffersPage
from SpaceToStudy.ui.pages.home_page.home_student import HomePageStudent
from tests.test_runners import TestRunnerWithStudent

TEST_CASE_219 = "https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/219"


class TestHomePageStudent(TestRunnerWithStudent):

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/282")
    def test_search_field_find_by_name(self):
        search_result = (HomePageStudent(self.driver)
                         .get_search_input()
                         .set_text("Tutor F")
                         .click_find_tutor_btn()
                         .get_list_of_offers_grid_card())
        for result in search_result:
            self.assertIn("Tutor F", result.get_person_name())
        tutors_offers_is_active = (ExploreOffersPage(self.driver)
                                   .get_filtering_and_sorting_block()
                                   .get_tutors_offers()
                                   .value_of_css_property("color"))
        students_requests_is_not_active = (ExploreOffersPage(self.driver)
                                           .get_filtering_and_sorting_block()
                                           .get_students_requests()
                                           .value_of_css_property("color"))
        self.assertEqual(tutors_offers_is_active, "rgba(38, 50, 56, 1)")
        self.assertEqual(students_requests_is_not_active,"rgba(96, 125, 139, 1)")

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/217")
    def test_search_field_with_invalid_data(self):
        search_result = (HomePageStudent(self.driver)
                         .get_search_input()
                         .set_text("AN2$")
                         .click_find_tutor_btn()
                         .get_notification_block_with_no_results()
                         .get_notifications_text())
        self.assertEqual(search_result, "Sorry, no results found")
        count_of_filters = (ExploreOffersPage(self.driver)
                            .get_filtering_and_sorting_block()
                            .get_filter_quantity_number())
        tutors_offers_is_active = (ExploreOffersPage(self.driver)
                                   .get_filtering_and_sorting_block()
                                   .get_tutors_offers()
                                   .value_of_css_property("color"))
        students_requests_is_not_active = (ExploreOffersPage(self.driver)
                                           .get_filtering_and_sorting_block()
                                           .get_students_requests()
                                           .value_of_css_property("color"))
        self.assertEqual(count_of_filters, 1)
        self.assertEqual(tutors_offers_is_active, "rgba(38, 50, 56, 1)")
        self.assertEqual(students_requests_is_not_active,"rgba(96, 125, 139, 1)")

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/168")
    def test_search_field_find_by_category(self):
        search_result = (HomePageStudent(self.driver)
                         .get_search_input()
                         .set_text("CYBERSECURITY")
                         .click_find_tutor_btn()
                         .get_list_of_offers_grid_card())
        for result in search_result:
            self.assertIn("CYBERSECURITY", result.get_subject_label())
        count_of_filters = (ExploreOffersPage(self.driver)
                                   .get_filtering_and_sorting_block()
                                   .get_filter_quantity_number())
        tutors_offers_is_active = (ExploreOffersPage(self.driver)
                                   .get_filtering_and_sorting_block()
                                   .get_tutors_offers()
                                   .value_of_css_property("color"))
        students_requests_is_not_active = (ExploreOffersPage(self.driver)
                                           .get_filtering_and_sorting_block()
                                           .get_students_requests()
                                           .value_of_css_property("color"))
        self.assertEqual(count_of_filters, 1)
        self.assertEqual(tutors_offers_is_active, "rgba(38, 50, 56, 1)")
        self.assertEqual(students_requests_is_not_active,"rgba(96, 125, 139, 1)")

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/281")
    def test_search_field_find_by_title(self):
        search_result = (HomePageStudent(self.driver)
                         .get_search_input()
                         .set_text("Freestyle and breakdance")
                         .click_find_tutor_btn()
                         .get_list_of_offers_inline_card())
        for result in search_result:
            self.assertIn("Freestyle and breakdance", result.get_offer_title())
        count_of_filters = (ExploreOffersPage(self.driver)
                            .get_filtering_and_sorting_block()
                            .get_filter_quantity_number())
        tutors_offers_is_active = (ExploreOffersPage(self.driver)
                                   .get_filtering_and_sorting_block()
                                   .get_tutors_offers()
                                   .value_of_css_property("color"))
        students_requests_is_not_active = (ExploreOffersPage(self.driver)
                                           .get_filtering_and_sorting_block()
                                           .get_students_requests()
                                           .value_of_css_property("color"))
        self.assertEqual(count_of_filters, 1)
        self.assertEqual(tutors_offers_is_active, "rgba(38, 50, 56, 1)")
        self.assertEqual(students_requests_is_not_active, "rgba(96, 125, 139, 1)")

    def test_student_can_see_tutors_offers_at_the_home_page(self):
        (HomePageStudent(self.driver)
         .get_search_input()
         .click_find_tutor_btn())
        list_of_offers = (ExploreOffersPage(self.driver)
                          .get_list_of_offers_grid_card())
        self.assertIsNotNone(list_of_offers, "There are no offers")

    @allure.testcase(TEST_CASE_219)
    def test_the_ui_welcoming_block_resize(self):
        HomePageStudent(self.driver).set_size_window(899, 1080)
        tablet_input_block = (HomePageStudent(self.driver).get_search_input().node.size['width'])
        tablet_input = (HomePageStudent(self.driver).get_search_input().get_input().size['width'])
        tablet_find_tutor_btn = (HomePageStudent(self.driver).get_search_input().get_find_tutor_btn().size['width'])
        self.assertEqual(777, tablet_input_block, "The item is not the right size")
        self.assertEqual(563, tablet_input, "The item is not the right size")
        self.assertEqual(130, tablet_find_tutor_btn, "The item is not the right size")
        HomePageStudent(self.driver).set_size_window(599, 1080)
        mobile_input_block = (HomePageStudent(self.driver).get_search_input().node.size['width'])
        mobile_input = (HomePageStudent(self.driver).get_search_input().get_input().size['width'])
        mobile_find_tutor_btn = (HomePageStudent(self.driver).get_search_input().get_find_tutor_btn().size['width'])
        self.assertEqual(493, mobile_input_block, "The item is not the right size")
        self.assertEqual(445, mobile_input, "The item is not the right size")
        self.assertEqual(493, mobile_find_tutor_btn, "The item is not the right size")
