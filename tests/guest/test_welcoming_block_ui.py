from time import sleep

import allure
from selenium.webdriver import Keys

from SpaceToStudy.ui.pages.header.header_unauthorized_component import HeaderUnauthorizedComponent
from SpaceToStudy.ui.pages.home_page.home_guest import (HomePageGuest,
                                                        COLLAPSE_BLOCK_FREE_CHOICE_OF_TUTORS,
                                                        COLLAPSE_BLOCK_DIGITAL_COMMUNICATION,
                                                        COLLAPSE_BLOCK_INDIVIDUAL_TIME,
                                                        COLLAPSE_BLOCK_FLEXIBLE_LOCATION,
                                                        BUTTON_GET_STARTED_FOR_FREE)
from tests.test_runners import BaseTestRunner


class WelcomingBlockUI(BaseTestRunner):

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/209")
    def test_the_collapse_block_ui_interaction(self):
        # check if first element is opened by default
        default_el = (HomePageGuest(self.driver).get_collapse_list_items_block()[0].is_expanded())
        individual_time_el = (HomePageGuest(self.driver).get_collapse_list_items_block()[1].is_expanded())
        individual_free_choice_el = (HomePageGuest(self.driver).get_collapse_list_items_block()[2].is_expanded())
        digital_communication_el = (HomePageGuest(self.driver).get_collapse_list_items_block()[3].is_expanded())
        self.assertTrue(default_el, "Element is not opened")
        self.assertFalse(individual_time_el, "Element is opened")
        self.assertFalse(individual_free_choice_el, "Element is opened")
        self.assertFalse(digital_communication_el, "Element is opened")

        # check if guest can open a description to any of four items in the list and change text color and background
        (HomePageGuest(self.driver).click_individual_time())
        background_color = (HomePageGuest(self.driver).get_individual_time().node
                            .value_of_css_property("background-color"))
        self.assertEqual("rgba(55, 71, 79, 1)", background_color)

        color_description = (HomePageGuest(self.driver)
                             .get_individual_time()
                             .get_description_value_of_css("color"))
        self.assertEqual("rgba(255, 255, 255, 1)", color_description)
        color_title = (HomePageGuest(self.driver)
                       .get_individual_time()
                       .get_color_of_title())
        self.assertEqual("rgba(255, 255, 255, 1)", color_title)
        is_second_el_open = (HomePageGuest(self.driver).get_collapse_list_items_block())
        for result in is_second_el_open[:1] + is_second_el_open[2:]:
            self.assertFalse(result.is_expanded(), "Element is selected")

        (HomePageGuest(self.driver).click_free_choice_of_tutors())

        background_color = (HomePageGuest(self.driver).get_free_choice_of_tutors().node
                            .value_of_css_property("background-color"))
        self.assertEqual("rgba(55, 71, 79, 1)", background_color)
        color_description = (HomePageGuest(self.driver)
                             .get_free_choice_of_tutors()
                             .get_description_value_of_css("color"))
        self.assertEqual("rgba(255, 255, 255, 1)", color_description)
        color_title = (HomePageGuest(self.driver)
                       .get_free_choice_of_tutors()
                       .get_color_of_title())
        self.assertEqual("rgba(255, 255, 255, 1)", color_title)
        is_third_el_open = (HomePageGuest(self.driver).get_collapse_list_items_block())
        for result in is_third_el_open[:2] + is_third_el_open[3:]:
            self.assertFalse(result.is_expanded(), "Element is selected")

        (HomePageGuest(self.driver).click_digital_communication())

        background_color = (HomePageGuest(self.driver).get_digital_communication().node
                            .value_of_css_property("background-color"))
        self.assertEqual("rgba(55, 71, 79, 1)", background_color)
        color_description = (HomePageGuest(self.driver)
                             .get_digital_communication()
                             .get_description_value_of_css("color"))
        self.assertEqual("rgba(255, 255, 255, 1)", color_description)
        color_title = (HomePageGuest(self.driver)
                       .get_digital_communication()
                       .get_color_of_title())
        self.assertEqual("rgba(255, 255, 255, 1)", color_title)
        is_fourth_el_open = (HomePageGuest(self.driver).get_collapse_list_items_block())
        for result in is_fourth_el_open[:3]:
            self.assertFalse(result.is_expanded(), "Element is selected")

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/206")
    def test_the_collapse_block_ui_alignment(self):
        # check the coordinates of X
        margin_between_elements = 68
        location_x = (HomePageGuest(self.driver).get_collapse_list_items_block())
        for result in location_x:
            self.assertEqual(969, result.get_title().location['x'])

        location_y = (HomePageGuest(self.driver).get_collapse_list_items_block())
        start_coordinate_y = 922
        # check the coordinates of Y starting from the second element
        for result in location_y[1:]:
            sleep(2)
            start_coordinate_y = start_coordinate_y + margin_between_elements
            self.assertEqual(start_coordinate_y, result.get_title().location['y'])
        # check the width block
        width_block = (HomePageGuest(self.driver).get_collapse_block())
        width = width_block.size['width']
        self.assertEqual(540, width)

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/203")
    def test_the_collapse_block_ui_text(self):
        home = HomePageGuest(self.driver)
        flexible_location = "Flexible Location"
        individual_time = "Individual Time"
        free_choice = "Free Choice of Tutors"
        digital_communication = "Digital Communication"
        description_flexible_location = ("Space2Study platform has no boundaries and can be used anywhere in the"
                                         " world, all you need is aspiration.")
        description_individual_time = ("Space2Study platform provides the opportunity to study lessons at "
                                       "any time convenient for you, pause and continue again.")
        description_free_choice_of_tutors = ("Space2Study platform has a wide range of criteria and will help you "
                                             "find the best tutor for education.")
        description_digital_communication = ("Space2Study platform offers extensive opportunities for meaningful "
                                             "communication not only with tutors but also with students.")
        title_fl = home.get_flexible_location().get_title_text()
        self.assertEqual(flexible_location, title_fl)
        description_fl = (HomePageGuest(self.driver)
                          .get_flexible_location()
                          .get_description_text())
        self.assertEqual(description_flexible_location, description_fl)

        title_it = home.get_individual_time().get_title_text()
        self.assertEqual(individual_time, title_it)
        home.click_individual_time()
        description_it = home.get_individual_time().get_description_text()
        self.assertEqual(description_individual_time, description_it)

        title_fc = home.get_free_choice_of_tutors().get_title_text()
        self.assertEqual(free_choice, title_fc)
        home.click_free_choice_of_tutors()
        description_fc = home.get_free_choice_of_tutors().get_description_text()
        self.assertIn(description_free_choice_of_tutors, description_fc)

        title_dc = home.get_digital_communication().get_title_text()
        self.assertEqual(digital_communication, title_dc)
        home.click_digital_communication()
        description_dc = home.get_digital_communication().get_description_text()
        self.assertEqual(description_digital_communication, description_dc)

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/212")
    def test_the_collapse_block_ui_hover(self):
        # check hover elements
        get_first_el = self.driver.find_element(*COLLAPSE_BLOCK_FLEXIBLE_LOCATION)
        hover_first_el = (HomePageGuest(self.driver)
                          .hover(get_first_el)
                          .value_of_css_property("background-color"))

        get_second_el = self.driver.find_element(*COLLAPSE_BLOCK_INDIVIDUAL_TIME)
        hover_second_el = (HomePageGuest(self.driver)
                           .hover(get_second_el)
                           .value_of_css_property("background-color"))

        get_third_el = self.driver.find_element(*COLLAPSE_BLOCK_FREE_CHOICE_OF_TUTORS)
        hover_third_el = (HomePageGuest(self.driver)
                          .hover(get_third_el)
                          .value_of_css_property("background-color"))

        get_fourth_el = self.driver.find_element(*COLLAPSE_BLOCK_DIGITAL_COMMUNICATION)
        hover_fourth_el = (HomePageGuest(self.driver)
                           .hover(get_fourth_el)
                           .value_of_css_property("background-color"))
        self.assertEqual("rgba(55, 71, 79, 1)", hover_first_el)
        self.assertEqual("rgba(236, 239, 241, 1)", hover_second_el)
        self.assertEqual("rgba(236, 239, 241, 1)", hover_third_el)
        self.assertEqual("rgba(236, 239, 241, 1)", hover_fourth_el)

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/273")
    def test_the_collapse_block_ui_resize(self):
        HomePageGuest(self.driver).set_size_window(899, 1080)
        width_tablet = (HomePageGuest(self.driver).get_collapse_block().size['width'])
        self.assertEqual(229, width_tablet)

        (HomePageGuest(self.driver).set_size_window(599, 1080))
        sleep(3)
        width_mobile = (
            HomePageGuest(self.driver).get_collapse_list_items_block_mobile_size_screen()[0].node.size['width'])
        self.assertEqual(544, width_mobile)

        is_hidden_first_el = (HomePageGuest(self.driver)
                              .get_collapse_list_items_block_mobile_size_screen()[0].node.get_attribute("aria-hidden"))
        is_hidden_second_el = (HomePageGuest(self.driver)
                               .get_collapse_list_items_block_mobile_size_screen()[1].node.get_attribute("aria-hidden"))
        is_hidden_third_el = (HomePageGuest(self.driver)
                              .get_collapse_list_items_block_mobile_size_screen()[2].node.get_attribute("aria-hidden"))
        is_hidden_fourth_el = (HomePageGuest(self.driver)
                               .get_collapse_list_items_block_mobile_size_screen()[3].node.get_attribute("aria-hidden"))
        self.assertEqual("false", is_hidden_first_el, "First element is hidden")
        self.assertTrue(is_hidden_second_el, "Second element is not hidden")
        self.assertTrue(is_hidden_third_el, "Third element is not hidden")
        self.assertTrue(is_hidden_fourth_el, "Fourth element is not hidden")

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/173")
    def test_the_collapse_block_ui_tab(self):
        # check tab
        (HeaderUnauthorizedComponent(self.driver).tab_key(6))
        sleep(2)
        first_el_tab = (HomePageGuest(self.driver)
                        .get_collapse_list_items_block()[0]
                        .get_background_el_with_tab()
                        .value_of_css_property("background-color"))
        (HeaderUnauthorizedComponent(self.driver).tab_key(7))
        sleep(2)
        second_el_tab = (HomePageGuest(self.driver)
                         .get_collapse_list_items_block()[1]
                         .get_background_el_with_tab()
                         .value_of_css_property("background-color"))
        (HeaderUnauthorizedComponent(self.driver).tab_key(8))
        sleep(2)
        third_el_tab = (HomePageGuest(self.driver)
                        .get_collapse_list_items_block()[2]
                        .get_background_el_with_tab()
                        .value_of_css_property("background-color"))
        (HeaderUnauthorizedComponent(self.driver).tab_key(9))
        sleep(2)
        fourth_el_tab = (HomePageGuest(self.driver)
                         .get_collapse_list_items_block()[3]
                         .get_background_el_with_tab()
                         .value_of_css_property("background-color"))
        self.assertEqual("rgba(0, 0, 0, 0.12)", first_el_tab)
        self.assertEqual("rgba(0, 0, 0, 0.12)", second_el_tab)
        self.assertEqual("rgba(0, 0, 0, 0.12)", third_el_tab)
        self.assertEqual("rgba(0, 0, 0, 0.12)", fourth_el_tab)

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/191")
    def test_the_get_started_for_free_button_ui(self):
        button_is_displayed = (HomePageGuest(self.driver)
                               .get_button_get_started_for_free()
                               .is_displayed())
        self.assertTrue(button_is_displayed, "Element not displayed!")
        button_get_started = self.driver.find_element(*BUTTON_GET_STARTED_FOR_FREE)
        button_hover = (HomePageGuest(self.driver)
                        .hover(button_get_started)
                        .value_of_css_property("background-color"))
        self.assertEqual("rgba(69, 90, 100, 1)", button_hover)
        (HeaderUnauthorizedComponent(self.driver)
         .get_login_btn()
         .send_keys(Keys.TAB))
        sleep(5)
        button_tab = (HomePageGuest(self.driver)
                      .get_button_get_started_for_free()
                      .value_of_css_property("box-shadow"))
        self.assertEqual("rgba(0, 0, 0, 0.2) 0px 3px 5px -1px,"
                         " rgba(0, 0, 0, 0.14) 0px 6px 10px 0px, "
                         "rgba(0, 0, 0, 0.12) 0px 1px 18px 0px", button_tab)
        block_is_displayed = (HomePageGuest(self.driver)
                              .click_button_get_started_for_free()
                              .is_displayed())
        self.assertTrue(block_is_displayed, "Element not displayed!")
