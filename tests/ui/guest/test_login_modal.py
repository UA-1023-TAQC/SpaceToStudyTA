from time import sleep

import allure

from SpaceToStudy.ui.pages.header.header_authorized_component import HeaderAuthorizedComponent
from SpaceToStudy.ui.pages.header.header_unauthorized_component import HeaderUnauthorizedComponent
from SpaceToStudy.ui.pages.home_page.home_guest import HomePageGuest
from SpaceToStudy.ui.pages.login_modal.login_modal import LoginModal
from tests.ui.test_runners import BaseTestRunner
from tests.utils.value_provider import ValueProvider


class LoginModalTestCase(BaseTestRunner):

    @allure.testcase('https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/97')
    @allure.title('Verify that the user cannot close the login modal by clicking outside of it.')
    def test_login_modal_outside_click(self):
        login_modal = (HomePageGuest(self.driver)
                       .get_header()
                       .click_login_btn())
        self.assertTrue(login_modal.get_title_text, "Welcome back")
        login_modal.outside_click()
        self.assertTrue(login_modal.get_title_text, "Welcome back")

    def test_login_button_greyed_out_and_non_clickable(self):
        HeaderUnauthorizedComponent(self.driver).click_login_btn()
        button = LoginModal(self.driver).get_login_button()
        self.assertEqual("rgba(0, 0, 0, 0.12)",
                         button.get_value_css_property("background-color"),
                         "Button background color is not as expected")
        self.assertFalse(button.is_enabled_button(), "The button must be disabled")

    @allure.testcase('https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/114')
    @allure.title('Verify that the registered user can access the personal cabinet')
    def test_user_access_to_personal_cabinet(self):
        login_modal = (HomePageGuest(self.driver)
                       .get_header()
                       .click_login_btn())
        self.assertTrue(login_modal.get_title_text, "Welcome back")
        authorize = (LoginModal(self.driver)
                     .set_email(ValueProvider.get_tutor_email())
                     .set_password(ValueProvider.get_tutor_password())
                     )
        sleep(1)
        self.assertEqual("rgba(38, 50, 56, 1)",
                         authorize.get_login_button().get_value_css_property("background-color"))
        authorize.click_login_button()
        name_surname = (HeaderAuthorizedComponent(self.driver)
                        .get_user_menu()
                        .click_account()
                        .click_menu_items_my_profile()
                        .get_name_surname_text())
        full_name = ValueProvider.get_tutor_first_name() + " " + ValueProvider.get_tutor_last_name()
        self.assertEqual(full_name, name_surname)
