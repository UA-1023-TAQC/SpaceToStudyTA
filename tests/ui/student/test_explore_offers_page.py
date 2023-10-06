import allure

from SpaceToStudy.ui.pages.explore_offers.explore_offers_page import ExploreOffersPage
from SpaceToStudy.ui.pages.home_page.home_student import HomePageStudent
from tests.ui.test_runners import TestRunnerWithStudent
from tests.utils.value_provider import ValueProvider


class TestExploreOffersPageStudent(TestRunnerWithStudent):

    @allure.testcase('https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/215')
    @allure.title('Verify that a Student can find a tutor by name at the welcoming block')
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

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/282")
    def test_search_field_find_by_name(self):
        search_result = (HomePageStudent(self.driver)
                         .get_search_input()
                         .set_text("Bruno M")
                         .click_find_tutor_btn()
                         .get_list_of_offers_inline_card())
        for result in search_result:
            self.assertIn("Bruno M", result.get_person_name())
        tutors_offers_is_active = (ExploreOffersPage(self.driver)
                                   .get_filtering_and_sorting_block()
                                   .get_tutors_offers()
                                   .value_of_css_property("color"))
        students_requests_is_not_active = (ExploreOffersPage(self.driver)
                                           .get_filtering_and_sorting_block()
                                           .get_students_requests()
                                           .value_of_css_property("color"))
        self.assertEqual(tutors_offers_is_active, "rgba(38, 50, 56, 1)")
        self.assertEqual(students_requests_is_not_active, "rgba(96, 125, 139, 1)")

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
        self.assertEqual(students_requests_is_not_active, "rgba(96, 125, 139, 1)")

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/168")
    def test_search_field_find_by_subject(self):
        search_result = (HomePageStudent(self.driver)
                         .get_search_input()
                         .set_text("CYBERSECURITY")
                         .click_find_tutor_btn()
                         .get_list_of_offers_inline_card())
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
        self.assertEqual(students_requests_is_not_active, "rgba(96, 125, 139, 1)")

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
