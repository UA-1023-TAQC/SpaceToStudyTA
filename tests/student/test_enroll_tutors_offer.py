import unittest

from SpaceToStudy.ui.pages.home_page.home_student import HomePageStudent
from SpaceToStudy.ui.pages.offer_details.enroll_offer_modal import EnrollOfferModal
from SpaceToStudy.ui.pages.offer_details.offer_details import OfferDetailsPage

from tests.test_runners import TestRunnerWithStudent


class EnrollStudentsOffer(TestRunnerWithStudent):

    def test_enroll_tutors_offer_with_default_level(self):
        list_of_offers = (HomePageStudent(self.driver)
                          .click_button_go_to_categories()  # main Student -> Categories
                          .click_show_all_offers_btn()  # Categories -> Find offers (explore offers)
                          .get_list_of_offers_inline_card())  # returns list

        list_of_offers[2].click_view_details_btn()
        (OfferDetailsPage(self.driver).get_offer_inline_card_component()
         .click_enroll_offer_btn())

        successful_request = (EnrollOfferModal(self.driver)
                              .set_preferred_price_input(400)
                              .add_additional_information("Hello!")
                              .click_send_cooperation_request_btn()
                              .is_request_sent_successfully())
        self.assertTrue(successful_request, "Element not displayed!")

    def test_enroll_tutors_offer_with_selected_level(self):
        list_of_offers = (HomePageStudent(self.driver)
                          .click_button_go_to_categories()
                          .click_show_all_offers_btn()
                          .get_list_of_offers_inline_card())

        list_of_offers[5].click_view_details_btn()
        (OfferDetailsPage(self.driver).get_offer_inline_card_component()
         .click_enroll_offer_btn())

        successful_request = (EnrollOfferModal(self.driver)
                              .get_your_required_level_dropdown()
                              .select_required_level_option("Intermediate")
                              .set_preferred_price_input(128)
                              .add_additional_information("Hello!")
                              .click_send_cooperation_request_btn()
                              .is_request_sent_successfully())
        self.assertTrue(successful_request, "Element not displayed!")

    def test_change_default_price_to_min_and_max(self):
        list_of_offers = (HomePageStudent(self.driver)
                          .click_button_go_to_categories()
                          .click_show_all_offers_btn()
                          .get_list_of_offers_inline_card())

        list_of_offers[5].click_view_details_btn()
        (OfferDetailsPage(self.driver).get_offer_inline_card_component()
         .click_enroll_offer_btn())

        default_price = EnrollOfferModal(self.driver).get_current_price_label()
        self.assertEqual(default_price, 500.1, "Actual prices not equal!")

        EnrollOfferModal(self.driver).set_lowest_price()
        lowest_price = EnrollOfferModal(self.driver).get_current_price_label()
        self.assertEqual(lowest_price, 375, "Min prices not equal!")

        EnrollOfferModal(self.driver).set_highest_price()
        highest_price = EnrollOfferModal(self.driver).get_current_price_label()
        self.assertEqual(highest_price, 625, "Max prices not equal!")

    def test_set_price_using_slider(self):
        list_of_offers = (HomePageStudent(self.driver)
                          .click_button_go_to_categories()
                          .click_show_all_offers_btn()
                          .get_list_of_offers_inline_card())

        list_of_offers[5].click_view_details_btn()
        (OfferDetailsPage(self.driver).get_offer_inline_card_component()
         .click_enroll_offer_btn())

        EnrollOfferModal(self.driver).drag_price_slider_to_value(600)
        default_price = EnrollOfferModal(self.driver).get_current_price_label()
        self.assertEqual(default_price, 600, "Actual prices not equal!")

    def test_set_price_moving_slider_left(self):
        list_of_offers = (HomePageStudent(self.driver)
                          .click_button_go_to_categories()
                          .click_show_all_offers_btn()
                          .get_list_of_offers_inline_card())

        list_of_offers[5].click_view_details_btn()
        (OfferDetailsPage(self.driver).get_offer_inline_card_component()
         .click_enroll_offer_btn())

        EnrollOfferModal(self.driver).drag_price_slider_left(10)
        default_price = EnrollOfferModal(self.driver).get_current_price_label()
        self.assertEqual(default_price, 490, "Actual prices not equal!")

    def test_set_price_moving_slider_right(self):
        list_of_offers = (HomePageStudent(self.driver)
                          .click_button_go_to_categories()
                          .click_show_all_offers_btn()
                          .get_list_of_offers_inline_card())

        list_of_offers[5].click_view_details_btn()
        (OfferDetailsPage(self.driver).get_offer_inline_card_component()
         .click_enroll_offer_btn())

        EnrollOfferModal(self.driver).drag_price_slider_right(60)
        default_price = EnrollOfferModal(self.driver).get_current_price_label()
        self.assertEqual(default_price, 560, "Actual prices not equal!")

    if __name__ == '__main__':
        unittest.main(verbosity=2)
