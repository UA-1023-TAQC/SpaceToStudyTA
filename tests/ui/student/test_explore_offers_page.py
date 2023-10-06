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

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/334",
                     "Check the student’s home page How it works block UI Test 1")
    def test_how_it_works_ui_find_tutor_btn(self):
        find_tutor_btn = (HomePageStudent(self.driver)
                          .click_navigate_link_in_header_by_name("How it works")
                          .get_how_it_works_block_student()
                          .get_button_find_tutor_in_how_it_works())
        find_tutor_is_displayed = find_tutor_btn.is_displayed()
        self.assertTrue(find_tutor_is_displayed, "'Find tutor' button isn't displayed on the page")

        find_tutor_background_color = find_tutor_btn.value_of_css_property("background-color")
        hover_find_tutor_background_color = (HomePageStudent(self.driver)
                                             .hover(find_tutor_btn)
                                             .value_of_css_property("background-color"))
        self.assertNotEqual(find_tutor_background_color, hover_find_tutor_background_color,
                            "'Find tutor' button doesn't changes color when hovered over")

        button_class_with_tab_animation = "Mui-focusVisible"
        find_tutor_class = find_tutor_btn.get_attribute("class")
        self.assertTrue(button_class_with_tab_animation not in find_tutor_class,
                        "'Find tutor' button is flashing without being hovered over or pressed with TAB key")

        (HomePageStudent(self.driver).get_button_go_to_categories().send_keys(Keys.TAB))
        tab_find_tutor_class = find_tutor_btn.get_attribute("class")
        self.assertTrue(button_class_with_tab_animation in tab_find_tutor_class,
                        "'Find tutor' button is not flashing when hovered over by pressing TAB key")
