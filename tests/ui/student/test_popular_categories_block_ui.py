import re

import allure
from selenium.webdriver import Keys

from SpaceToStudy.ui.pages.home_page.home_student import (HomePageStudent,
                                                          BUTTON_GO_TO_CATEGORIES,
                                                          CATEGORY_MUSIC,
                                                          CATEGORY_DESIGN,
                                                          CATEGORY_COMPUTER,
                                                          CATEGORY_MATH,
                                                          CATEGORY_DANCE,
                                                          CATEGORY_LANGUAGES)
from tests.ui.test_runners import TestRunnerWithStudent


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

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/347")
    def test_popular_categories_block_ui_tab(self):
        (HomePageStudent(self.driver)
         .get_button_go_to_categories()
         .send_keys(Keys.TAB))
        get_flash = (HomePageStudent(self.driver).get_tub_animation())
        self.assertTrue(get_flash, "There is no flash")

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/345")
    def test_popular_categories_block_ui_text(self):
        music = "Music"
        computer = "Computer science"
        design = "Design"
        dance = "Dance"
        mathematics = "Mathematics"
        languages = "Languages"
        title_block = "Popular Categories"
        descriptions_block = "Explore tutoring categories you're passionate about."
        home = HomePageStudent(self.driver)
        get_title_block = home.get_title_categories_block()
        get_descriptions_block = home.get_description_categories_block()
        category_music = home.get_categories()[0].get_name()
        category_computer = home.get_categories()[1].get_name()
        category_design = home.get_categories()[2].get_name()
        category_dance = home.get_categories()[3].get_name()
        category_mathematics = home.get_categories()[4].get_name()
        category_languages = home.get_categories()[5].get_name()
        self.assertEqual(title_block, get_title_block)
        self.assertEqual(descriptions_block, get_descriptions_block)
        self.assertEqual(music, category_music)
        self.assertEqual(computer, category_computer)
        self.assertEqual(design, category_design)
        self.assertEqual(dance, category_dance)
        self.assertEqual(mathematics, category_mathematics)
        self.assertEqual(languages, category_languages)

        offers = (HomePageStudent(self.driver).get_categories())
        self.list_offers_without_digits = []
        for i in offers:
            text_offers = i.get_offers()
            text_offers_without_digits = re.sub(r"[^A-Za-z]", "", text_offers)
            self.list_offers_without_digits.append(text_offers_without_digits)
        for element in self.list_offers_without_digits:
            self.assertEqual("offers", element)

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

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/340")
    def test_popular_categories_block_ui_alignment(self):
        home = HomePageStudent(self.driver)
        delta = 13
        gap = home.get_gap_value_css_property_categories_block()
        size_window = self.driver.get_window_size()
        get_block = home.get_categories_block()
        get_width_window = size_window['width']
        get_width_block = get_block.size['width']
        left_margin = get_block.location['x'] + delta
        right_margin = get_width_window - get_width_block - left_margin
        width_one_element = home.get_categories()[0].node.size['width']
        height_one_element = home.get_categories()[0].node.size['height']
        horizontal_margin_between_elements = gap + width_one_element
        vertical_margin_between_elements = gap + height_one_element
        start_coordinate_x = (get_width_window - get_width_block) / 2 - delta
        start_coordinate_y = home.get_categories_block().location['y']

        location_x = home.get_categories()
        for result in location_x[:4]:
            self.assertEqual(start_coordinate_x, result.node.location['x'])
            start_coordinate_x = start_coordinate_x + horizontal_margin_between_elements

        location_y = (HomePageStudent(self.driver).get_categories())
        first_row = [value for index, value in enumerate(location_y) if index < 4]
        second_row = [value for index, value in enumerate(location_y) if 3 < index < 8]
        for result in first_row:
            self.assertEqual(start_coordinate_y, result.node.location['y'])
        for result in second_row:
            self.assertEqual(start_coordinate_y + vertical_margin_between_elements, result.node.location['y'])

        self.assertEqual(right_margin, left_margin)

