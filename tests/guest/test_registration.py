import unittest

import allure

from SpaceToStudy.ui.pages.header.header_unauthorized_component import HeaderUnauthorizedComponent
from SpaceToStudy.ui.pages.home_page.home_guest import HomePageGuest
from SpaceToStudy.ui.pages.sign_up_modal.sign_up_modal import RegistrationModal
from tests.test_runners import BaseTestRunner
from tests.value_provider import ValueProvider


class RegistrationTestCase(BaseTestRunner):

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

    def test_registration_modal_student_is_shown_for_guest(self):
        is_displayed = (HomePageGuest(self.driver)
                        .click_started_for_free()
                        .click_become_a_tutor()
                        .is_displayed())
        self.assertTrue(is_displayed, "Element not displayed!")

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

    def test_open_tutor_registration_modal_at_what_can_you_do_block(self):
        block_is_displayed = (HomePageGuest(self.driver)
                              .get_header()
                              .get_navigate_links()[0]
                              .click()
                              .click_become_a_tutor()
                              .is_displayed())
        self.assertTrue(block_is_displayed, "Element not displayed!")

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

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/107",
                     "Verify that 'Sign up as a tutor' pop-up contains all UI components")
    def test_tutor_registration_modal_contains_all_UI_components(self):
        registration_modal = (HomePageGuest(self.driver).click_started_for_free().click_become_a_tutor())
        registration_modal_title = registration_modal.get_text_title_modal()
        self.assertEqual(registration_modal_title, "Sign up as a tutor",
                         "Modal name differs from 'Sign up as a tutor'")

        first_name_exist = registration_modal.get_first_name_input().is_displayed()
        self.assertTrue(first_name_exist, "First name input doesn't exist")
        first_name_label = registration_modal.get_first_name_label_text()
        self.assertEqual("First name\u2009*", first_name_label,
                         "Input name differs from 'First name'")

        last_name_exist = registration_modal.get_last_name_input().is_displayed()
        self.assertTrue(last_name_exist, "last name input doesn't exist")
        last_name_label = registration_modal.get_last_name_label_text()
        self.assertEqual("Last name\u2009*", last_name_label,
                         "Input name differs from 'Last name'")

        email_exist = registration_modal.get_email_input().is_displayed()
        self.assertTrue(email_exist, "Email input doesn't exist")
        email_label = registration_modal.get_email_label_text()
        self.assertEqual("Email\u2009*", email_label,
                         "Input name differs from 'Email'")

        password_exist = registration_modal.get_password_input().is_displayed()
        self.assertTrue(password_exist, "Password input doesn't exist")
        password_label = registration_modal.get_password_label_text()
        self.assertEqual("Password\u2009*", password_label,
                         "Input name differs from 'Password'")

        confirm_password_exist = registration_modal.get_confirm_password_input().is_displayed()
        self.assertTrue(confirm_password_exist, "Confirm password input doesn't exist")
        confirm_password_label = registration_modal.get_confirm_password_label_text()
        self.assertEqual("Confirm password\u2009*", confirm_password_label,
                         "Input name differs from 'Confirm password'")

        i_agree_checkbox_exist = registration_modal.get_i_agree_checkbox().is_displayed()
        self.assertTrue(i_agree_checkbox_exist, "'I agree' checkbox doesn't exist")
        i_agree_checkbox_empty = registration_modal.get_i_agree_checkbox().is_checked()
        self.assertFalse(i_agree_checkbox_empty, "'I agree' checkbox is checked by default")

        terms_link_text = registration_modal.get_terms_link_text()
        self.assertEqual(terms_link_text, "Terms",
                         "Link name differs from 'Terms'")
        terms_is_underlined = registration_modal.get_terms_link().get_value_css_property("text-decoration")
        self.assertEqual("underline solid rgb(38, 50, 56)", terms_is_underlined, "'Terms' link isn't underlined")
        terms_is_bold = registration_modal.get_terms_link().get_value_css_property("font-weight")
        self.assertEqual("500", terms_is_bold, "'Terms' link isn't bold")
        terms_link_href = registration_modal.get_terms_link().get_link_href()
        self.assertEqual("https://s2s-front-stage.azurewebsites.net/", terms_link_href,
                         f"'Terms' refers on {terms_link_href}, "
                         f"but expected URL 'https://s2s-front-stage.azurewebsites.net/'.")

        privacy_policy_link_text = registration_modal.get_privacy_policy_link_text()
        self.assertEqual("Privacy Policy", privacy_policy_link_text,
                         "Link name differs from 'Privacy policy'")
        privacy_policy_is_underlined = (registration_modal.get_privacy_policy_link()
                                        .get_value_css_property("text-decoration"))
        self.assertEqual("underline solid rgb(38, 50, 56)", privacy_policy_is_underlined,
                         "'Privacy policy' link isn't underlined")
        privacy_policy_is_bold = registration_modal.get_privacy_policy_link().get_value_css_property("font-weight")
        self.assertEqual("500", privacy_policy_is_bold, "'Privacy policy' link isn't bold")
        privacy_policy_link_href = registration_modal.get_privacy_policy_link().get_link_href()
        self.assertEqual("https://s2s-front-stage.azurewebsites.net/privacy-policy", privacy_policy_link_href,
                         f"'Privacy policy' refers on {privacy_policy_link_href},"
                         f" but expected URL 'https://s2s-front-stage.azurewebsites.net/privacy-policy'.'")

        sign_up_btn_exist = registration_modal.get_sign_up_btn().is_displayed()
        self.assertTrue(sign_up_btn_exist, "'Sign up' button doesn't exist")
        sign_up_btn_title = registration_modal.get_sign_up_btn().text
        self.assertEqual(sign_up_btn_title, "Sign up",
                         f"Button name is {sign_up_btn_title}, but expected 'Sign up'")

        or_continue_exist = registration_modal.get_or_continue_text().is_displayed()
        self.assertTrue(or_continue_exist, "'or continue' text doesn't exist")
        or_continue_text = registration_modal.get_or_continue_text().text
        self.assertEqual(or_continue_text, "or continue", "Text differs from 'or continue'")

        sign_up_with_google_btn_exist = registration_modal.get_sign_up_with_google_iframe().is_displayed()
        self.assertTrue(sign_up_with_google_btn_exist, "'Sign up with Google' button doesn't exist")
        sign_up_with_google_btn_title = registration_modal.get_sign_up_with_google_btn_text()
        print(sign_up_btn_title)
        self.assertEqual("Sign up with Google", sign_up_with_google_btn_title,
                         f"Button name is {sign_up_with_google_btn_title}, but expected 'Sign up with Google'")
        # CONTINUE..

if __name__ == '__main__':
    unittest.main(verbosity=2)
