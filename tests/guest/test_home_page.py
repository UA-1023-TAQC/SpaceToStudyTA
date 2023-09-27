import allure
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from SpaceToStudy.ui.pages.header.header_component import HeaderComponent
from SpaceToStudy.ui.pages.header.header_unauthorized_component import HeaderUnauthorizedComponent
from SpaceToStudy.ui.pages.home_page.home_guest import (COLLAPSE_BLOCK_DIGITAL_COMMUNICATION,
                                                        COLLAPSE_BLOCK_FREE_CHOICE_OF_TUTORS,
                                                        COLLAPSE_BLOCK_INDIVIDUAL_TIME,
                                                        COLLAPSE_BLOCK_FLEXIBLE_LOCATION)

from SpaceToStudy.ui.pages.home_page.home_guest import HomePageGuest, BUTTON_GET_STARTED_FOR_FREE
from tests.test_runners import BaseTestRunner


class HomePageTestCase(BaseTestRunner):
    def test_switched_modals(self):
        button_become_a_student_text = (HomePageGuest(self.driver)
                                        .click_checkbox_switch_how_it_works_block()
                                        .get_text_button_become_a_student_tutor())
        self.assertEquals(button_become_a_student_text, "Become a tutor")
        registration_modal = (HomePageGuest(self.driver)
                              .click_button_become_a_student_tutor())
        registration_modal_title = registration_modal.get_title_text()
        self.assertTrue(registration_modal_title, "Sign up as a tutor")
        login_modal_title = (registration_modal
                             .click_login_link()
                             .get_title_text())
        self.assertEquals(login_modal_title, "Welcome back")

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/105")
    def test_how_it_works_block_is_visible_guest(self):
        (HeaderUnauthorizedComponent(self.driver)
         .get_navigate_links()[1]
         .click())
        block_is_displayed = (HomePageGuest(self.driver)
                              .get_how_it_works_block()
                              .is_displayed_how_it_works_block())
        self.assertTrue(block_is_displayed, "Element not displayed!")
        block_learn = (HomePageGuest(self.driver)
                       .get_how_it_works_block()
                       .get_checkbox_learn_from_experts()
                       .value_of_css_property("color"))
        self.assertEqual("rgba(38, 50, 56, 1)", block_learn)
        block_share = (HomePageGuest(self.driver)
                       .get_how_it_works_block()
                       .get_checkbox_share_your_experience()
                       .value_of_css_property("color"))
        self.assertEqual("rgba(96, 125, 139, 1)", block_share)

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
        sleep(2)
        color_description = (HomePageGuest(self.driver)
                             .get_individual_time()
                             .get_description_value_of_css("color"))
        self.assertEqual("rgba(255, 255, 255, 1)",color_description)
        color_title = (HomePageGuest(self.driver)
                       .get_individual_time()
                       .get_color_of_title())
        self.assertEqual("rgba(255, 255, 255, 1)",color_title)
        is_second_el_open = (HomePageGuest(self.driver).get_collapse_list_items_block())
        for result in is_second_el_open[:1] + is_second_el_open[2:]:
            self.assertFalse(result.get_description().is_displayed(), "Element is selected")

        (HomePageGuest(self.driver).click_free_choice_of_tutors())
        sleep(2)
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
            self.assertFalse(result.get_description().is_displayed(), "Element is selected")

        (HomePageGuest(self.driver).click_digital_communication())
        sleep(2)
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
            self.assertFalse(result.get_description().is_displayed(), "Element is selected")

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
        sleep(3)
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
        flexible_location = "Flexible Location"
        individual_time = "Individual Time"
        free_choice = "Free Choice of Tutors"
        digital_communication = "Digital Communication"
        description = ("It is a long established fact that a reader will be distracted by the readable content"
                       " of a page when looking at its layout.")
        title_fl = (HomePageGuest(self.driver)
                    .get_flexible_location()
                    .get_title())
        self.assertEqual(flexible_location, title_fl)
        description_fl = (HomePageGuest(self.driver)
                          .get_flexible_location().get_description())
        self.assertEqual(description_fl, description)
        title_it = (HomePageGuest(self.driver)
                    .get_individual_time()
                    .get_title())
        self.assertEqual(individual_time, title_it)
        description_it = (HomePageGuest(self.driver)
                          .get_individual_time()
                          .get_description())
        self.assertEqual(description_it, description)
        title_fc = (HomePageGuest(self.driver)
                    .get_free_choice_of_tutors()
                    .get_title())
        self.assertEqual(free_choice, title_fc)
        description_fc = (HomePageGuest(self.driver)
                          .get_free_choice_of_tutors()
                          .get_description())
        self.assertIn(description_fc, description)
        title_dc = (HomePageGuest(self.driver)
                    .get_digital_communication()
                    .get_title())
        self.assertEqual(digital_communication, title_dc)
        description_dc = (HomePageGuest(self.driver)
                          .get_digital_communication()
                          .get_description())
        self.assertIn(description_dc, description)

    def test_what_can_you_do_elements_visible(self):
        (HeaderUnauthorizedComponent(self.driver)
         .get_navigate_links()[0]
         .click())
        become_student_button = (HomePageGuest(self.driver)
                                 .get_card_learn_from_experts()
                                 .get_btn())
        self.assertIsNotNone(become_student_button, "The 'Become a student' button is not found")
        become_tutor_button = (HomePageGuest(self.driver)
                               .get_card_share_your_experience()
                               .get_btn())
        self.assertIsNotNone(become_tutor_button, "The 'Become a tutor' button is not found")

    def test_the_list_of_collapse_items(self):
        flexible_location_item = (HomePageGuest(self.driver)
                                  .get_flexible_location())
        self.assertEqual("rgba(55, 71, 79, 1)",
                         flexible_location_item.node.value_of_css_property("background-color"))
        self.assertEqual("rgba(255, 255, 255, 1)", flexible_location_item.get_color_of_title())
        individual_time_item = (HomePageGuest(self.driver)
                                .click_individual_time()
                                .get_individual_time()
                                .is_expanded())
        self.assertTrue(individual_time_item, "Element not displayed")
        self.assertNotEqual(individual_time_item, flexible_location_item.is_expanded(),
                            "The previous element did not close")
        free_choice_of_tutors = (HomePageGuest(self.driver)
                                 .get_free_choice_of_tutors())
        initial_location = free_choice_of_tutors.node.location
        free_choice_of_tutors.click()
        new_location = free_choice_of_tutors.node.location
        self.assertNotEqual(initial_location, new_location, "The element remained in place")

    def test_who_we_are_block_contains_video_content(self):
        (HeaderComponent(self.driver)
         .get_navigate_links()[2]
         .click())
        video = (HomePageGuest(self.driver)
                 .get_who_we_are_block()
                 .get_video())
        self.assertTrue(video)

    def test_open_who_we_are_block_by_tabs(self):
        logo = HeaderUnauthorizedComponent(self.driver).get_logo()
        logo.send_keys(Keys.TAB, 3, Keys.ENTER)
        title = (HomePageGuest(self.driver).get_who_we_are_block().get_title())
        self.assertEqual("Who we are", title)

    def test_that_controls_active_after_navigating_to_them(self):
        sleep(3)
        (HeaderUnauthorizedComponent(self.driver)
         .get_navigate_links()[0]
         .click())
        become_a_student = (HomePageGuest(self.driver)
                            .get_card_learn_from_experts()
                            .get_btn())
        button_before_it_is_hovered_over = become_a_student.value_of_css_property("background-color")
        ActionChains(self.driver).move_to_element(become_a_student).perform()
        sleep(5)
        button_after_it_is_hovered_over = become_a_student.value_of_css_property("background-color")
        self.assertNotEqual(button_before_it_is_hovered_over, button_after_it_is_hovered_over, "The button hasn't changed")

    def test_that_controls_active_after_navigating_to_them_by_tab(self):
        (HomePageGuest(self.driver)
         .get_card_learn_from_experts()
         .get_btn()
         .send_keys(Keys.TAB))
        focus_styles = (HomePageGuest(self.driver)
                        .get_card_share_your_experience()
                        .get_tub_animation())
        self.assertTrue(focus_styles, "There is no animation")

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
        background_fourth_el = (self.driver.find_element(*COLLAPSE_BLOCK_DIGITAL_COMMUNICATION)
                                .value_of_css_property("background-color"))
        self.assertEqual("rgba(236, 239, 241, 1)", hover_first_el)
        self.assertEqual("rgba(236, 239, 241, 1)", hover_second_el)
        self.assertEqual("rgba(236, 239, 241, 1)", hover_third_el)
        self.assertEqual("rgba(55, 71, 79, 1)", background_fourth_el)

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
        self.assertEqual("rgba(0, 0, 0, 0.12)",second_el_tab)
        self.assertEqual("rgba(0, 0, 0, 0.12)", third_el_tab)
        self.assertEqual("rgba(0, 0, 0, 0.12)", fourth_el_tab)
