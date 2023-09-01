import unittest

from selenium.webdriver.common.by import By

from SpaceToStudy.ui.pages.header.header_authorized_component import HeaderAuthorizedComponent
from SpaceToStudy.ui.pages.header.header_unauthorized_component import HeaderUnauthorizedComponent
from tests.test_runners import BaseTestRunner
from tests.value_provider import ValueProvider


class CreateRequestTestCase(BaseTestRunner):

    def test_offer_details(self):
        (HeaderUnauthorizedComponent(self.driver).click_login_btn()
            .set_email(ValueProvider.get_student_email())
            .set_password(ValueProvider.get_student_password())
            .click_login_button())
        (HeaderAuthorizedComponent(self.driver)
            .get_navigate_links()[0]
            .click())
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Create request')]").click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
