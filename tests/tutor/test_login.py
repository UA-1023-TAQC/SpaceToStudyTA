
from SpaceToStudy.ui.pages.home_page.home_guest import HomePageGuest
from SpaceToStudy.ui.pages.sign_up_modal.sign_up_modal import RegistrationModal
from tests.test_runners import BaseTestRunner


class LoginTestCase(BaseTestRunner):

    def test_login_password_without_alphabetic_numeric_character(self):
        home = HomePageGuest(self.driver)
        registration = RegistrationModal(self.driver)  # NODE OR DRIVER?
        home.get_button_get_started_for_free().click()
        (home
            .get_card_share_your_experience()
            .click_btn())
        registration.set_first_name("Nata")
        registration.set_last_name("Nata")
        registration.set_email("rozdilska.n@gmail.com")
        registration.set_password("@#$%//////")
        registration.click_password_icon()
        message = registration.get_password_error_message()
        self.assertEquals(message, "Password must contain at least one alphabetic and one numeric character")



