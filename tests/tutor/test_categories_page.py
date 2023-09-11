import unittest

from selenium.webdriver.common.by import By

from SpaceToStudy.ui.pages.categories.categories_page import CategoriesPage
from SpaceToStudy.ui.pages.header.header_component import HeaderComponent
from SpaceToStudy.ui.pages.header.header_unauthorized_component import HeaderUnauthorizedComponent
from tests.test_runners import BaseTestRunner
from tests.value_provider import ValueProvider


class CategoriesPageTestCase(BaseTestRunner):

    def test_no_result_categories_page(self):
        category = "Drawing"
        (HeaderUnauthorizedComponent(self.driver).click_login_btn()
         .set_email(ValueProvider.get_tutor_email())
         .set_password(ValueProvider.get_tutor_password())
         .click_login_button())
        (HeaderComponent(self.driver)
         .get_navigate_links()[0]
         .click())

        search_input = CategoriesPage(self.driver).get_search_input()
        search_input.set_text(category)
        search_input.press_enter_button()

        result_text = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div[4]/div/div/p").text
        self.assertEqual("Sorry, no results found", result_text)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)