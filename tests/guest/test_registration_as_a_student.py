import unittest

from SpaceToStudy.ui.pages.home_page.home_guest import HomePageGuest
from tests.test_runners import BaseTestRunner
from tests.value_provider import ValueProvider
from utils.api_for_emails import MailBox, TemporaryMailGenerator


class RegistrationAsAStudentTestCase(BaseTestRunner):
    def test_registration_as_a_student(self):
        mailbox_address = TemporaryMailGenerator().generate_email_address()

        registration = (HomePageGuest(self.driver)
                        .click_started_for_free()
                        .click_become_a_student()
                        .set_first_name(ValueProvider.get_student_first_name())
                        .set_last_name(ValueProvider.get_student_last_name())
                        .set_email(mailbox_address)
                        .set_password(ValueProvider.get_student_password())
                        .set_confirm_password(ValueProvider.get_student_password())
                        .click_i_agree_checkbox()
                        .click_sign_up_btn())

        mailbox = MailBox(mailbox_address).get_letters()
        self.assertEqual(len(mailbox), 1)
        letter = mailbox[0]
        sender = letter.get_sender()
        self.assertEqual(sender, "space2study.info@gmail.com")
        link = letter.get_link()
        self.driver.get(link)
        logging_in_as_student = (HomePageGuest(self.driver)
                                 .get_header()
                                 .click_login_btn()
                                 .set_email(mailbox_address)
                                 .set_password(ValueProvider.get_student_password())
                                 .click_login_button())

