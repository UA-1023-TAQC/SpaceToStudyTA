import unittest

from SpaceToStudy.ui.pages.categories.categories_page import CategoriesPage
from SpaceToStudy.ui.pages.header.header_component import HeaderComponent
from SpaceToStudy.ui.pages.header.header_unauthorized_component import HeaderUnauthorizedComponent
from tests.test_runners import BaseTestRunner
from tests.value_provider import ValueProvider


class CategoriesPageTestCase(BaseTestRunner):

    def test_searching_categories_page(self):
        category = "Design"
        (HeaderUnauthorizedComponent(self.driver).click_login_btn()
         .set_email(ValueProvider.get_tutor_email())
         .set_password(ValueProvider.get_tutor_password())
         .click_login_button())
        (HeaderComponent(self.driver)
         .get_navigate_links()[0]
         .click())

        search_input = CategoriesPage(self.driver).get_search_input()
        search_input.set_text(category)
        search_input.press_down_button(1).press_enter_button()

        card_name = (CategoriesPage(self.driver).get_cards()[0]
                     .click_card()
                     .get_cards()[0]
                     .get_title())
        self.assertEqual("Web design", card_name)

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

        result_text = CategoriesPage(self.driver).get_no_result_title()
        self.assertEqual("Sorry, no results found", result_text)

if __name__ == '__main__':
    unittest.main(verbosity=2)