import allure
from time import sleep

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from SpaceToStudy.ui.pages.header.header_component import HeaderComponent
from SpaceToStudy.ui.pages.header.header_unauthorized_component import HeaderUnauthorizedComponent

from SpaceToStudy.ui.pages.home_page.home_guest import HomePageGuest
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

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/176")
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

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/175")
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

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/198")
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
        self.assertNotEqual(button_before_it_is_hovered_over, button_after_it_is_hovered_over,
                            "The button hasn't changed")

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/198")
    def test_that_controls_active_after_navigating_to_them_by_tab(self):
        (HomePageGuest(self.driver)
         .get_card_learn_from_experts()
         .get_btn()
         .send_keys(Keys.TAB))
        focus_styles = (HomePageGuest(self.driver).get_tub_animation())
        self.assertTrue(focus_styles, "There is no animation")

