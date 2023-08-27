import unittest

from SpaceToStudy.ui.pages.home_page.home_guest import HomePageGuest
from SpaceToStudy.ui.pages.login_modal.login_modal import LoginModal
from SpaceToStudy.ui.pages.sign_up_modal.sign_up_modal import RegistrationModal
from tests.test_runners import BaseTestRunner


class HomePageTestCase(BaseTestRunner):
    def test_switched_modals(self):
        home_page_guest = HomePageGuest(self.driver)
        home_page_guest.click_checkbox_how_it_works_block()
        button_become_a_student_text = home_page_guest.get_how_it_works_block_become_a_tutor_or_student_button().text
        self.assertEquals(button_become_a_student_text, "Become a tutor")
        home_page_guest.click_how_it_works_block_become_a_tutor_or_student_button()
        registration_modal = RegistrationModal(self.driver)
        registration_modal_title = registration_modal.get_title_text()
        self.assertTrue(registration_modal_title, "Sign up as a tutor")
        registration_modal.click_login_link()
        login_modal = LoginModal(self.driver)
        title = login_modal.get_title().text
        self.assertEquals(title, "Welcome back")

