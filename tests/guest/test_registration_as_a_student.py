import unittest
from time import sleep

import allure

from SpaceToStudy.ui.pages.email_confirmation_modal.email_confirmation_modal import EmailConfirmationModal
from SpaceToStudy.ui.pages.first_login_student_modal.general_step import GeneralStepStudent
from SpaceToStudy.ui.pages.home_page.home_guest import HomePageGuest
from tests.test_runners import BaseTestRunner
from tests.value_provider import ValueProvider
from utils.api_for_emails import MailBox, TemporaryMailGenerator


class RegistrationAsAStudentTestCase(BaseTestRunner):
    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/100")
    def test_registration_as_a_student(self):
        mailbox_address = TemporaryMailGenerator().generate_email_address()

        # Registration
        (HomePageGuest(self.driver)
         .click_become_a_student()
         .set_first_name(ValueProvider.get_student_first_name())
         .set_last_name(ValueProvider.get_student_last_name())
         .set_email(mailbox_address)
         .set_password(ValueProvider.get_student_password())
         .set_confirm_password(ValueProvider.get_student_password())
         .click_i_agree_checkbox()
         .click_sign_up_btn())

        # Sleep to wait for email
        sleep(5)

        # Email confirmation and first login
        mailbox = MailBox(mailbox_address).get_letters()
        self.assertEqual(1, len(mailbox))
        letter = mailbox[0]
        sender = letter.get_sender_email()
        self.assertEqual("space2study.info@gmail.com", sender)
        link = letter.get_link_from_letter()
        self.driver.get(link)
        (EmailConfirmationModal(self.driver)
         .click_go_to_login_button()
         .set_email(mailbox_address)
         .set_password(ValueProvider.get_student_password())
         .click_login_button())

        first_login_as_student = GeneralStepStudent(self.driver)
        self.assertEqual(ValueProvider.get_student_first_name(),
                         first_login_as_student.get_first_name_input().get_attribute("value"))
        self.assertEqual(ValueProvider.get_student_last_name(),
                         first_login_as_student.get_last_name_input().get_attribute("value"))
