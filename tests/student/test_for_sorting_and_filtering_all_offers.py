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
        for offer in list_of_filtered_offers.get_list_of_offers_inline_card():
            self.assertEqual("GUITAR", offer.get_subject_label())
            self.assertIn("Yura", offer.get_person_name())

    def test_change_offers_view_to_card_and_to_list(self):
        # Change offers view to grid card view
        list_of_offers = ExploreOffersPage(self.driver)\
            .get_filtering_and_sorting_block()\
            .click_grid_card_btn()\
            .get_list_of_offers_grid_card()
        for offer in list_of_offers:
            self.assertTrue(offer.check_grid_card_is_displayed())

        # Change offers view to inline card view
        list_of_offers = ExploreOffersPage(self.driver)\
            .get_filtering_and_sorting_block()\
            .click_inline_card_btn()\
            .get_list_of_offers_inline_card()
        for offer in list_of_offers:
            self.assertTrue(offer.check_inline_card_is_displayed())

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

    def test_filter_by_level_in_sidebar(self):
        explore_offers_page = ExploreOffersPage(self.driver)\
            .get_filtering_and_sorting_block()\
            .click_filter_title()\
            .get_filters_sidebar_component()\
            .click_level_beginner_checkbox()\
            .click_apply_filters_btn()

        filter_quantity = explore_offers_page\
            .get_filtering_and_sorting_block()\
            .get_filter_quantity_number()
        self.assertEqual(filter_quantity, 1)

        list_of_filtered_offers = explore_offers_page.get_list_of_offers_inline_card()
        for offer in list_of_filtered_offers:
            self.assertIn("BEGINNER", offer.get_level_label())

    def test_price_drag_filter_in_sidebar(self):
        explore_offers_page = ExploreOffersPage(self.driver) \
            .get_filtering_and_sorting_block() \
            .click_filter_title() \
            .get_filters_sidebar_component()

        # Get current lowest and highest prices
        lowest_price = explore_offers_page.get_lowest_value_input()
        highest_price = explore_offers_page.get_highest_value_input()

        # Drag sliders to increase the lowest price
        # and decrease the highest price
        applied_filter = explore_offers_page\
            .drag_left_slider(10)\
            .drag_right_slider(10) \
            .click_apply_filters_btn()

        # Get new lowest and highest prices
        sidebar = applied_filter.get_filtering_and_sorting_block()\
            .click_filter_title()\
            .get_filters_sidebar_component()
        new_lowest_price = sidebar.get_lowest_value_input()
        new_highest_price = sidebar.get_highest_value_input()

        self.assertGreater(new_lowest_price, lowest_price, "Lowest price is not increased")
        self.assertLess(new_highest_price, highest_price, "Highest price is not decreased")

        # Get the number of filtered offers
        filter_quantity = sidebar.click_close_button() \
            .get_filtering_and_sorting_block() \
            .get_filter_quantity_number()
        self.assertEqual(filter_quantity, 1)

        # Check the prices of all filtered offers
        list_of_filtered_offers = applied_filter.get_list_of_filtered_offers()
        for offer in list_of_filtered_offers:
            self.assertTrue((new_lowest_price <= offer.get_price_value()) and
                            (new_highest_price >= offer.get_price_value()))
