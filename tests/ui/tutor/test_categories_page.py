import unittest

import allure

from SpaceToStudy.ui.pages.categories.categories_page import CategoriesPage
from SpaceToStudy.ui.pages.header.header_component import HeaderComponent
from SpaceToStudy.ui.pages.home_page.home_tutor import HomePageTutor
from tests.ui.test_runners import TestRunnerWithTutor


class CategoriesPageTestCase(TestRunnerWithTutor):

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/159")
    def test_searching_categories_page(self):
        category = "Design"
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

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/162")
    def test_no_result_categories_page(self):
        category = "Drawing"

        (HeaderComponent(self.driver)
         .get_navigate_links()[0]
         .click())

        search_input = CategoriesPage(self.driver).get_search_input()
        search_input.set_text(category)
        search_input.press_enter_button()

        result_text = CategoriesPage(self.driver).get_no_result_title()
        self.assertEqual("Sorry, no results found", result_text)

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/378")
    def test_verify_tutor_can_find_all_categories(self):
        categories = HomePageTutor(self.driver).click_go_to_categories_btn()
        self.assertEqual("Categories", categories.get_categories_title())
        self.assertIn("/categories", self.driver.current_url)

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/376")
    def test_verify_tutor_can_find_popular_categories(self):
        categories = HomePageTutor(self.driver).click_music_btn()
        self.assertEqual("Music Subjects", categories.get_music_subjects())


if __name__ == '__main__':
    unittest.main(verbosity=2)
