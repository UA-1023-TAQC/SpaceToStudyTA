import unittest

from selenium.webdriver.common.by import By

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

        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div[4]/div/a").click()
        card_name = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div[5]/div/a/div/p").text
        self.assertEqual("Web design", card_name)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)