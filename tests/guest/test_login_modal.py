from SpaceToStudy.ui.pages.header.header_unauthorized_component import HeaderUnauthorizedComponent
from SpaceToStudy.ui.pages.login_modal.login_modal import LoginModal
from tests.test_runners import BaseTestRunner


class LoginModalTestCase(BaseTestRunner):

    def test_login_button_greyed_out_and_non_clickable(self):
        HeaderUnauthorizedComponent(self.driver).click_login_btn()
        button = LoginModal(self.driver).get_login_button()
        self.assertEqual("rgba(0, 0, 0, 0.12)",
                         button.get_value_css_property("background-color"),
                         "Button background color is not as expected")
        self.assertFalse(button.is_enabled_button(), "The button must be disabled")
