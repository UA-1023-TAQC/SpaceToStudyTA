import unittest

from tests.test_runners import BaseTestRunner
from tests.value_provider import ValueProvider


class RegistrationAsAStudentTestCase(BaseTestRunner):
    def test_registration_as_a_student(self):
        from utils.api_for_emails import ApiForEmails
        api_for_emails = ApiForEmails()
        registration = (HomePageGuest(self.driver)
                        .click_started_for_free()
                        .click_become_a_student()
                        .set_first_name(ValueProvider.get_student_first_name())
                        .set_last_name(ValueProvider.get_student_last_name())
                        .set_email(api_for_emails.generate_email())
                        .set_password(ValueProvider.get_student_password())
                        .set_confirm_password(ValueProvider.get_student_password())
                        .click_i_agree_checkbox()
                        .click_sign_up_btn())