from SpaceToStudy.ui.pages.home_page.home_guest import HomePageGuest
from tests.test_runners import BaseTestRunner


class LoginModalTestCase(BaseTestRunner):

    def test_login_modal_outside_click(self):
        login_modal = (HomePageGuest(self.driver)
                       .get_header()
                       .click_login_btn())
        self.assertTrue(login_modal.is_open())
        login_modal.outside_click()
        self.assertTrue(login_modal.is_open())
