import unittest
import re

import allure

from SpaceToStudy.ui.pages.home_page.home_student import HomePageStudent
from SpaceToStudy.ui.pages.offer_details.enroll_offer_modal import EnrollOfferModal
from SpaceToStudy.ui.pages.offer_details.offer_details import OfferDetailsPage

from tests.test_runners import TestRunnerWithStudent


class EnrollTutorsOffer(TestRunnerWithStudent):

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
                              .click_your_required_level_dropdown()
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

        new_price = EnrollOfferModal(self.driver).set_lowest_price().get_current_price_slider_value()
        lowest_price = EnrollOfferModal(self.driver).get_lowest_price_value()
        self.assertEqual(lowest_price, new_price, "Min prices not equal!")

        changed_price = EnrollOfferModal(self.driver).set_highest_price().get_current_price_slider_value()
        highest_price = EnrollOfferModal(self.driver).get_highest_price_value()
        self.assertEqual(highest_price, changed_price, "Max prices not equal!")

    def test_set_price_using_slider(self):
        offer_details = (HomePageStudent(self.driver)
                         .click_button_find_tutor()
                         .get_search_by_tutor_name_block()
                         .set_subjects_input("Guitar")
                         .navigate_subjects_input_down()
                         .choose_subjects_item()
                         .set_search_by_tutor_name_input("Diana")
                         .click_search_btn()
                         .get_list_of_offers_inline_card()[0]
                         .click_view_details_btn())

        new_price = (OfferDetailsPage(self.driver)
                     .get_offer_inline_card_component()
                     .click_enroll_offer_btn()
                     .drag_price_slider_to_value(600)
                     .get_current_price_slider_value())
        self.assertEqual(new_price, 600, "Actual prices not equal!")

    def test_set_price_moving_slider_left(self):
        offer_details = (HomePageStudent(self.driver)
                         .click_button_find_tutor()
                         .get_search_by_tutor_name_block()
                         .set_subjects_input("Guitar")
                         .navigate_subjects_input_down()
                         .choose_subjects_item()
                         .set_search_by_tutor_name_input("Diana")
                         .click_search_btn()
                         .get_list_of_offers_inline_card()[0]
                         .click_view_details_btn())

        new_price = (OfferDetailsPage(self.driver)
                     .get_offer_inline_card_component()
                     .click_enroll_offer_btn()
                     .drag_price_slider_left(10)
                     .get_current_price_slider_value())
        self.assertEqual(new_price, 770, "Actual prices not equal!")

    def test_set_price_moving_slider_right(self):
        offer_details = (HomePageStudent(self.driver)
                         .click_button_find_tutor()
                         .get_search_by_tutor_name_block()
                         .set_subjects_input("Guitar")
                         .navigate_subjects_input_down()
                         .choose_subjects_item()
                         .set_search_by_tutor_name_input("Diana")
                         .click_search_btn()
                         .get_list_of_offers_inline_card()[0]
                         .click_view_details_btn())

        new_price = (OfferDetailsPage(self.driver)
                     .get_offer_inline_card_component()
                     .click_enroll_offer_btn()
                     .drag_price_slider_right(60)
                     .get_current_price_slider_value())
        self.assertEqual(new_price, 840, "Actual prices not equal!")

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/98",
                     "Enroll offer as a Student")
    def test_enroll_offer_as_a_student(self):
        offer_details = (HomePageStudent(self.driver)
                         .click_button_find_tutor()
                         .get_search_by_tutor_name_block()
                         .set_subjects_input("Guitar")
                         .navigate_subjects_input_down()
                         .choose_subjects_item()
                         .click_search_btn()
                         .get_list_of_offers_inline_card()[4]
                         .click_view_details_btn())

        enroll_offer_modal = (OfferDetailsPage(self.driver).get_offer_inline_card_component()
                              .click_enroll_offer_btn())

        tutors_name_exist = enroll_offer_modal.get_grid_card_component().get_person_name().is_displayed()
        self.assertTrue(tutors_name_exist, "Name text doesn't displayed")

        language_info_exist = enroll_offer_modal.get_grid_card_component().get_languages_webelement().is_displayed()
        self.assertTrue(language_info_exist, "Language text doesn't displayed")

        subject_info_exist = enroll_offer_modal.get_grid_card_component().get_subject_label_webelement().is_displayed()
        self.assertTrue(subject_info_exist, "Subject text doesn't displayed")

        level_info_exist = enroll_offer_modal.get_grid_card_component().get_level_label_webelement().is_displayed()
        self.assertTrue(level_info_exist, "Level text doesn't displayed")

        price_info_exist = enroll_offer_modal.get_grid_card_component().get_price_value_webelement().is_displayed()
        self.assertTrue(price_info_exist, "Price text doesn't displayed")

        rating_info_exist = enroll_offer_modal.get_grid_card_component().get_rating_webelement().is_displayed()
        self.assertTrue(rating_info_exist, "Rating text doesn't displayed")

        reviews_info_exist = enroll_offer_modal.get_grid_card_component().get_reviews_webelement().is_displayed()
        self.assertTrue(reviews_info_exist, "Reviews text doesn't displayed")

        required_level = enroll_offer_modal.get_your_required_level_text().lower()
        tutor_level = enroll_offer_modal.get_grid_card_component().get_level_label().lower()
        self.assertEqual(tutor_level, required_level,
                         f"Required level is: {required_level}, but expected is: {tutor_level}")

        preferred_price_textbox = enroll_offer_modal.get_current_price_textbox_value()
        tutor_price_string = enroll_offer_modal.get_grid_card_component().get_price_value()

        tutor_price_float = float(re.sub(r'[^0-9.]', '', tutor_price_string))
        self.assertEqual(tutor_price_float, preferred_price_textbox,
                         f"Price in textbox is: {preferred_price_textbox}, but expected is: {tutor_price_float}")

        preferred_price_slider = enroll_offer_modal.get_current_price_slider_value()
        self.assertEqual(tutor_price_float, preferred_price_slider,
                         f"Price on slider is: {preferred_price_slider}, but expected is: {tutor_price_float}")

        additional_info_is_empty = enroll_offer_modal.get_additional_information().text
        self.assertEqual("", additional_info_is_empty,
                         f"Additional info is: {additional_info_is_empty}, but expected to be empty")

        EnrollOfferModal(self.driver).drag_price_slider_left(10)
        slider_price = enroll_offer_modal.get_current_price_slider_value()
        textbox_price = enroll_offer_modal.get_current_price_textbox_value()
        self.assertEqual(textbox_price, slider_price,
                         f"Preferred price in slider is: {slider_price}, but in textbox is: {textbox_price}")

        new_price = int(textbox_price - 10)
        enroll_offer_modal.set_preferred_price_input(new_price)
        slider_price = enroll_offer_modal.get_current_price_slider_value()
        textbox_price = enroll_offer_modal.get_current_price_textbox_value()
        self.assertEqual(textbox_price, slider_price,
                         f"Preferred price in slider is: {slider_price}, but in textbox is: {textbox_price}")

        text_for_additional_info = "Hello! I want to take a couple of lessons."
        enroll_offer_modal.add_additional_information(text_for_additional_info)
        additional_info = enroll_offer_modal.get_additional_information().text
        self.assertEqual(text_for_additional_info, additional_info,
                         f"Additional info is: {additional_info}, but expected to be: {text_for_additional_info}")

        successful_request = (EnrollOfferModal(self.driver).click_send_cooperation_request_btn()
                              .is_request_sent_successfully())
        self.assertTrue(successful_request, "Flashbox 'Request for cooperation sent successfully' didn't appear")

    if __name__ == '__main__':
        unittest.main(verbosity=2)
