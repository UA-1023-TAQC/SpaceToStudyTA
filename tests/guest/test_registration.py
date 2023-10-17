import unittest

import allure

from SpaceToStudy.ui.pages.header.header_unauthorized_component import HeaderUnauthorizedComponent
from SpaceToStudy.ui.pages.home_page.home_guest import HomePageGuest
from SpaceToStudy.ui.pages.sign_up_modal.sign_up_modal import RegistrationModal
from tests.ui.test_runners import BaseTestRunner
from tests.utils.value_provider import ValueProvider


class RegistrationTestCase(BaseTestRunner):

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/110")
    def test_registration_password_without_alphabetic_numeric_character(self):
        registration = (HomePageGuest(self.driver)
                        .click_started_for_free()
                        .click_become_a_tutor())
        (registration.set_first_name("test")
                     .set_last_name("test")
                     .set_email("test@gmail.com")
                     .set_password("@#$%//////")
                     .click_sign_up_btn())
        message = (registration.get_password_error_message())
        self.assertEqual(message, "Password must contain at least one alphabetic and one numeric character")

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/104")
    def test_registration_modal_student_is_shown_for_guest(self):
        is_displayed = (HomePageGuest(self.driver)
                        .click_started_for_free()
                        .click_become_a_tutor()
                        .is_displayed())
        self.assertTrue(is_displayed, "Element not displayed!")

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/109")
    def test_registration_tutor_too_long_password(self):
        registration = (HomePageGuest(self.driver)
                        .click_started_for_free()
                        .click_become_a_tutor())
        (registration.set_first_name("test")
                     .set_last_name("test")
                     .set_email("test@gmail.com")
                     .set_password("11111111111111111111111111q")
                     .click_sign_up_btn())
        message = (registration.get_password_error_message())
        self.assertEqual(message, "Password cannot be shorter than 8 and longer than 25 characters")

    def test_tutor_signUp_button_is_active(self):
        (HeaderUnauthorizedComponent(self.driver)
                                .click_login_btn()
                                .get_join_us_for_free()
                                .click_link())
        registration_modal = (HomePageGuest(self.driver)
                              .click_become_a_tutor()
                              .set_first_name(ValueProvider.get_tutor_first_name())
                              .set_last_name(ValueProvider.get_tutor_last_name())
                              .set_email(ValueProvider.get_tutor_email())
                              .set_password(ValueProvider.get_tutor_password())
                              .set_confirm_password(ValueProvider.get_tutor_password())
                              .click_i_agree_checkbox())
        self.assertEqual('0', registration_modal.get_sign_up_btn().get_attribute("tabindex"))
        self.assertEqual("rgba(38, 50, 56, 1)",
                         registration_modal.get_sign_up_btn().value_of_css_property("background-color"))

    def test_open_student_form_via_what_can_u_do_block(self):
        HeaderUnauthorizedComponent(self.driver).get_navigate_links()[1].click()
        HomePageGuest(self.driver).click_button_become_a_student_tutor()
        modal = RegistrationModal(self.driver).get_title_text()
        self.assertTrue(modal, "Sign up as a student")

    def test_guest_can_open_the_student_registration_popup(self):
        (HomePageGuest(self.driver)
         .get_how_it_works_block()
         .get_checkbox_learn_from_experts()
         .click()
        )
        HomePageGuest(self.driver).click_button_become_a_student_tutor()
        modal = RegistrationModal(self.driver).get_title_text()
        self.assertTrue(modal, "Sign up as a student")

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/181",
                     "Verify that a Guest can open the tutor registration pop-up at the How it works block")
    def test_guest_can_open_the_tutor_registration_popup(self):
        how_it_works_block_is_displayed = (HomePageGuest(self.driver)
                                           .get_how_it_works_block()
                                           .is_displayed_how_it_works_block())
        self.assertTrue(how_it_works_block_is_displayed, "'How it works' block isn't displayed")

        share_your_experience_title_color = (HomePageGuest(self.driver)
                                             .click_checkbox_switch_how_it_works_block()
                                             .get_share_your_experience_how_it_works_block()
                                             .value_of_css_property("color"))
        self.assertEqual("rgba(38, 50, 56, 1)", share_your_experience_title_color,
                         "'Share your Experience' option isn't active")

        button_become_a_tutor_text = (HomePageGuest(self.driver)
                                      .get_text_button_become_a_student_tutor())
        self.assertEqual(button_become_a_tutor_text, "Become a tutor",
                         "Button's name differs from 'Become a tutor'")

        registration_modal_title = (HomePageGuest(self.driver)
                                    .click_button_become_a_student_tutor().get_text_title_modal())
        self.assertEqual(registration_modal_title, "Sign up as a tutor",
                         "Modal's name differs from 'Sign up as a tutor'")

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/171")
    def test_open_tutor_registration_modal_at_what_can_you_do_block(self):
        block_is_displayed = (HomePageGuest(self.driver)
                              .get_header()
                              .get_navigate_links()[0]
                              .click()
                              .click_become_a_tutor()
                              .is_displayed())
        self.assertTrue(block_is_displayed, "Element not displayed!")

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/177")
    def test_open_student_registration_modal_at_what_can_you_do_block(self):
        block_is_displayed = (HomePageGuest(self.driver)
                              .get_header()
                              .get_navigate_links()[0]
                              .click()
                              .click_become_a_student()
                              .is_displayed())
        self.assertTrue(block_is_displayed, "Element not displayed!")

    @allure.testcase('https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/174')
    def test_opening_of_modal_registration_window_for_tutor_and_student(self):
        get_started_for_free = (HomePageGuest(self.driver)
                                .click_started_for_free())
        start_student = get_started_for_free\
            .get_card_learn_from_experts()\
            .click_btn()
        title_student = start_student.get_text_title_modal()
        self.assertEqual(title_student, "Sign up as a student")
        start_student.click_close_btn()
        title_tutor = get_started_for_free\
            .get_card_share_your_experience()\
            .click_btn()\
            .get_text_title_modal()
        self.assertEqual(title_tutor, "Sign up as a tutor")


    @allure.testcase('https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/189')
    def test_visability_of_the_all_elements_after_resizing_for_who_we_are_block(self):
        window_width = 600
        window_height = 1000
        who_we_are = (HomePageGuest(self.driver)
                              .get_header()
                              .get_navigate_links()[2]
                              .click())
        HomePageGuest(self.driver).set_size_window(window_width, window_height)
        who_we_are_elements = (HomePageGuest(who_we_are)
                               .get_who_we_are_block()
                               .get_who_we_are_elements())
        for element in who_we_are_elements.values():
            self.assertTrue(element.is_displayed())

if __name__ == '__main__':
    unittest.main(verbosity=2)

