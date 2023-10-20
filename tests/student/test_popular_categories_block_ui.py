from time import sleep

import allure

from SpaceToStudy.ui.pages.header.header_component import HeaderComponent
from SpaceToStudy.ui.pages.home_page.home_student import HomePageStudent, BUTTON_GO_TO_CATEGORIES
from SpaceToStudy.ui.pages.subjects.subjects_page import SubjectsPage
from tests.test_runners import TestRunnerWithStudent


class PopularCategoriesBlockUI(TestRunnerWithStudent):

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/203")
    def test_popular_categories_block_ui_button(self):
        button_is_displayed = (HomePageStudent(self.driver)
                               .get_button_go_to_categories()
                               .is_displayed())
        button_text = (HomePageStudent(self.driver)
                       .get_text_button_go_to_categories())
        button = self.driver.find_element(*BUTTON_GO_TO_CATEGORIES)
        button_hover = (HomePageStudent(self.driver)
                        .hover(button)
                        .value_of_css_property("background-color"))
        self.assertEqual("rgba(0, 0, 0, 0.04)", button_hover)
        page_is_displayed = (HomePageStudent(self.driver)
                             .click_button_go_to_categories()
                             .get_categories_block()
                             .is_displayed())
        self.assertEqual("Go to categories", button_text)
        self.assertTrue(button_is_displayed, "Button is not displayed")
        self.assertTrue(page_is_displayed, "Page is not displayed")

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/361")
    def test_popular_categories_block_ui_interaction(self):
        title_music = HomePageStudent(self.driver).click_category_el(0).get_text_subjects_title()

        self.assertEqual("Music Subjects", title_music)
        self.driver.back()
        self.driver.refresh()
        is_displayed_music = HomePageStudent(self.driver).click_category_el(0).get_subjects_title().is_displayed()
        self.assertTrue(is_displayed_music)
        self.driver.back()
        self.driver.refresh()

        title_computer = HomePageStudent(self.driver).click_category_el(1).get_text_subjects_title()
        self.assertEqual("Computer science Subjects", title_computer)
        self.driver.back()
        self.driver.refresh()
        is_displayed_computer = HomePageStudent(self.driver).click_category_el(1).get_subjects_title().is_displayed()
        self.assertTrue(is_displayed_computer)
        self.driver.back()
        self.driver.refresh()

        title_design = HomePageStudent(self.driver).click_category_el(2).get_text_subjects_title()
        self.assertEqual("Dance Subjects", title_design)
        self.driver.back()
        self.driver.refresh()
        is_displayed_design = HomePageStudent(self.driver).click_category_el(2).get_subjects_title().is_displayed()
        self.assertTrue(is_displayed_design)
        self.driver.back()
        self.driver.refresh()

        title_dance = HomePageStudent(self.driver).click_category_el(3).get_text_subjects_title()
        self.assertEqual("Mathematics Subjects", title_dance)
        self.driver.back()
        self.driver.refresh()
        is_displayed_dance = HomePageStudent(self.driver).click_category_el(3).get_subjects_title().is_displayed()
        self.assertTrue(is_displayed_dance)
        self.driver.back()
        self.driver.refresh()

        title_math = HomePageStudent(self.driver).click_category_el(4).get_text_subjects_title()
        self.assertEqual("Design Subjects", title_math)
        self.driver.back()
        self.driver.refresh()
        is_displayed_math = HomePageStudent(self.driver).click_category_el(4).get_subjects_title().is_displayed()
        self.assertTrue(is_displayed_math)
        self.driver.back()
        self.driver.refresh()

        title_language = HomePageStudent(self.driver).click_category_el(5).get_text_subjects_title()
        self.assertEqual("Languages Subjects", title_language)
        self.driver.back()
        self.driver.refresh()
        is_displayed_language = HomePageStudent(self.driver).click_category_el(5).get_subjects_title().is_displayed()
        self.assertTrue(is_displayed_language)


