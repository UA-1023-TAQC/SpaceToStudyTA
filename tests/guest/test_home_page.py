from time import sleep

from SpaceToStudy.ui.pages.header.header_unauthorized_component import HeaderUnauthorizedComponent
from SpaceToStudy.ui.pages.home_page.home_guest import HomePageGuest
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
