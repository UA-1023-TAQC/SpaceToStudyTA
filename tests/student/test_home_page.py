import allure

from selenium.webdriver import Keys

from SpaceToStudy.ui.pages.categories.categories_page import CategoriesPage
from tests.test_runners import TestRunnerWithStudent
from SpaceToStudy.ui.pages.explore_offers.explore_offers_page import ExploreOffersPage
from SpaceToStudy.ui.pages.home_page.home_student import HomePageStudent


class TestHomePageStudent(TestRunnerWithStudent):

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

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/218")
    def test_student_can_see_tutors_offers_at_the_home_page(self):
        (HomePageStudent(self.driver)
         .get_search_input()
         .click_find_tutor_btn())
        list_of_offers = (ExploreOffersPage(self.driver)
                          .get_list_of_offers_grid_card())
        self.assertIsNotNone(list_of_offers, "There are no offers")

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/283")
    def test_the_ui_welcoming_block(self):
        get_input_line = (HomePageStudent(self.driver)
                          .get_search_input()
                          .get_input()
                          .get_attribute("placeholder"))
        get_find_tutor = (HomePageStudent(self.driver)
                          .get_text_button_find_tutor)
        self.assertTrue("What would you like to learn ?", get_input_line)
        self.assertTrue("Find tutor", get_find_tutor)

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/284")
    def test_the_welcoming_block_controls_active_after_navigating_to_them(self):
        find_tutor_btn = (HomePageStudent(self.driver)
                          .get_button_find_tutor())
        before_hover = find_tutor_btn.value_of_css_property("background-color")
        after_hover = (HomePageStudent(self.driver)
                       .hover(find_tutor_btn)
                       .value_of_css_property("background-color"))
        self.assertNotEqual(before_hover, after_hover, "The button hasn't changed")

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/284")
    def test_the_welcoming_block_controls_active_after_navigating_to_them_by_tab(self):
        (HomePageStudent(self.driver)
         .get_search_input()
         .get_input()
         .send_keys(Keys.TAB))
        after_hover = (HomePageStudent(self.driver).get_tub_animation())
        self.assertTrue(after_hover, "There is no animation")

    @allure.testcase('https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/305')
    @allure.title('Verify that a Student can find popular learning categories and choose one at the home page')
    def test_verify_student_can_find_popular_categories(self):
        card_element = (HomePageStudent(self.driver).get_categories())[1]
        name = card_element.get_name()
        self.assertEqual("Computer science", name)
        card_element.click()
        title = CategoriesPage(self.driver).get_categories_title()
        self.assertEqual("Computer science Subjects", title)
        sub_category_name = (CategoriesPage(self.driver).get_cards())[0].get_title()
        self.assertEqual("Cybersecurity", sub_category_name)

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/219")
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
