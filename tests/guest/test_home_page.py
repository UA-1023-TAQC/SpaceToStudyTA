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

