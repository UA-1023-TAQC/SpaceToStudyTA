import allure

from SpaceToStudy.ui.pages.home_page.home_student import HomePageStudent, BUTTON_GO_TO_CATEGORIES
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

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/340")
    def test_popular_categories_block_ui_alignment(self):
        home = HomePageStudent(self.driver)
        delta = 13
        gap = 24
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
        second_row = [value for index, value in enumerate(location_y) if index > 3 & index < 8]
        for result in first_row:
            self.assertEqual(start_coordinate_y, result.node.location['y'])
        for result in second_row:
            self.assertEqual(start_coordinate_y + vertical_margin_between_elements, result.node.location['y'])

        self.assertEqual(right_margin, left_margin)
