from time import sleep

from selenium.webdriver import Keys

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

    def test_the_collapse_block_ui_tab(self):
        # check tab
        (HeaderUnauthorizedComponent(self.driver).get_logo().send_keys(Keys.TAB * 7))
        sleep(2)
        first_el_tab = (HomePageGuest(self.driver)
                         .get_collapse_list_items_block()[0]
                         .get_el_tab()
                         .value_of_css_property("background-color"))
        (HeaderUnauthorizedComponent(self.driver).get_logo().send_keys(Keys.TAB * 7))
        sleep(2)
        second_el_tab = (HomePageGuest(self.driver)
                  .get_collapse_list_items_block()[1]
                  .get_el_tab()
                  .value_of_css_property("background-color"))
        (HeaderUnauthorizedComponent(self.driver).get_logo().send_keys(Keys.TAB * 8))
        sleep(2)
        third_el_tab = (HomePageGuest(self.driver)
                         .get_collapse_list_items_block()[2]
                         .get_el_tab()
                         .value_of_css_property("background-color"))
        (HeaderUnauthorizedComponent(self.driver).get_logo().send_keys(Keys.TAB * 8))
        sleep(2)
        fourth_el_tab = (HomePageGuest(self.driver)
                        .get_collapse_list_items_block()[3]
                        .get_el_tab()
                        .value_of_css_property("background-color"))
        self.assertEqual("rgba(0, 0, 0, 0.12)", first_el_tab)
        self.assertEqual("rgba(0, 0, 0, 0.12)", second_el_tab)
        self.assertEqual("rgba(0, 0, 0, 0.12)",  third_el_tab)
        self.assertEqual("rgba(0, 0, 0, 0.12)", fourth_el_tab)



