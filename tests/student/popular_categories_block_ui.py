import allure

from SpaceToStudy.ui.pages.home_page.home_student import (HomePageStudent,
                                                          BUTTON_GO_TO_CATEGORIES,
                                                          CATEGORY_MUSIC,
                                                          CATEGORY_DESIGN,
                                                          CATEGORY_COMPUTER,
                                                          CATEGORY_MATH,
                                                          CATEGORY_DANCE,
                                                          CATEGORY_LANGUAGES)
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

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/352")
    def test_popular_categories_block_ui_hover(self):
        get_music_el = self.driver.find_element(*CATEGORY_MUSIC)
        hover_music_el = (HomePageStudent(self.driver).hover(get_music_el).value_of_css_property("box-shadow"))
        cursor_music_el = (HomePageStudent(self.driver).hover(get_music_el).value_of_css_property("cursor"))
        self.assertEqual("rgba(144, 164, 174, 0.56) 0px 3px 16px 2px", hover_music_el)
        self.assertEqual("pointer", cursor_music_el)

        get_computer_el = self.driver.find_element(*CATEGORY_COMPUTER)
        hover_computer_el = (HomePageStudent(self.driver).hover(get_computer_el).value_of_css_property("box-shadow"))
        cursor_computer_el = (HomePageStudent(self.driver).hover(get_computer_el).value_of_css_property("cursor"))
        self.assertEqual("rgba(144, 164, 174, 0.56) 0px 3px 16px 2px", hover_computer_el)
        self.assertEqual("pointer", cursor_computer_el)

        get_design_el = self.driver.find_element(*CATEGORY_DESIGN)
        hover_design_el = (HomePageStudent(self.driver).hover(get_design_el).value_of_css_property("box-shadow"))
        cursor_design_el = (HomePageStudent(self.driver).hover(get_design_el).value_of_css_property("cursor"))
        self.assertEqual("rgba(144, 164, 174, 0.56) 0px 3px 16px 2px", hover_design_el)
        self.assertEqual("pointer", cursor_design_el)

        get_dance_el = self.driver.find_element(*CATEGORY_DANCE)
        hover_dance_el = (HomePageStudent(self.driver).hover(get_dance_el).value_of_css_property("box-shadow"))
        cursor_dance_el = (HomePageStudent(self.driver).hover(get_dance_el).value_of_css_property("cursor"))
        self.assertEqual("rgba(144, 164, 174, 0.56) 0px 3px 16px 2px", hover_dance_el)
        self.assertEqual("pointer", cursor_dance_el)

        get_math_el = self.driver.find_element(*CATEGORY_MATH)
        hover_math_el = (HomePageStudent(self.driver).hover(get_math_el).value_of_css_property("box-shadow"))
        cursor_math_el = (HomePageStudent(self.driver).hover(get_math_el).value_of_css_property("cursor"))
        self.assertEqual("rgba(144, 164, 174, 0.56) 0px 3px 16px 2px", hover_math_el)
        self.assertEqual("pointer", cursor_math_el)

        get_languages_el = self.driver.find_element(*CATEGORY_LANGUAGES)
        hover_languages_el = (HomePageStudent(self.driver).hover(get_languages_el).value_of_css_property("box-shadow"))
        cursor_languages_el = (HomePageStudent(self.driver).hover(get_languages_el).value_of_css_property("cursor"))
        self.assertEqual("rgba(144, 164, 174, 0.56) 0px 3px 16px 2px", hover_languages_el)
        self.assertEqual("pointer", cursor_languages_el)

