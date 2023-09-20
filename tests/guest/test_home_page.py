from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from SpaceToStudy.ui.pages.header.header_component import HeaderComponent
from SpaceToStudy.ui.pages.header.header_unauthorized_component import HeaderUnauthorizedComponent
from SpaceToStudy.ui.pages.home_page.home_guest import (HomePageGuest, 
                                                        COLLAPSE_BLOCK_DIGITAL_COMMUNICATION,
                                                        COLLAPSE_BLOCK_FREE_CHOICE_OF_TUTORS,
                                                        COLLAPSE_BLOCK_INDIVIDUAL_TIME,
                                                        COLLAPSE_BLOCK_FLEXIBLE_LOCATION)
from tests.test_runners import BaseTestRunner


class HomePageTestCase(BaseTestRunner):
    def test_switched_modals(self):
        button_become_a_student_text = (HomePageGuest(self.driver)
                                        .click_checkbox_how_it_works_block()
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
                             .get_color_of_description("color"))
        self.assertEqual("rgba(255, 255, 255, 1)", color_description)
        color_title = (HomePageGuest(self.driver)
                       .get_individual_time()
                       .get_color_of_title())
        self.assertEqual("rgba(255, 255, 255, 1)", color_title)
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
                             .get_color_of_description("color"))
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
                             .get_color_of_description("color"))
        self.assertEqual("rgba(255, 255, 255, 1)", color_description)
        color_title = (HomePageGuest(self.driver)
                       .get_digital_communication()
                       .get_color_of_title())
        self.assertEqual("rgba(255, 255, 255, 1)", color_title)
        is_fourth_el_open = (HomePageGuest(self.driver).get_collapse_list_items_block())
        for result in is_fourth_el_open[:3]:
            self.assertFalse(result.get_description().is_displayed(), "Element is selected")

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
        self.assertIn(flexible_location, title_fl)
        description_fl = (HomePageGuest(self.driver)
                          .get_flexible_location().get_description())
        self.assertIn(description_fl, description)
        title_it = (HomePageGuest(self.driver)
                    .get_individual_time()
                    .get_title())
        self.assertIn(individual_time, title_it)
        description_it = (HomePageGuest(self.driver)
                          .get_individual_time()
                          .get_description())
        self.assertIn(description_it, description)
        title_fc = (HomePageGuest(self.driver)
                    .get_free_choice_of_tutors()
                    .get_title())
        self.assertIn(free_choice, title_fc)
        description_fc = (HomePageGuest(self.driver)
                          .get_free_choice_of_tutors()
                          .get_description())
        self.assertIn(description_fc, description)
        title_dc = (HomePageGuest(self.driver)
                    .get_digital_communication()
                    .get_title())
        self.assertIn(digital_communication, title_dc)
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
