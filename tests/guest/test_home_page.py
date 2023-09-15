from time import sleep

from selenium.webdriver import Keys

from SpaceToStudy.ui.pages.header.header_unauthorized_component import HeaderUnauthorizedComponent
from SpaceToStudy.ui.pages.home_page.home_guest import HomePageGuest, BUTTON_GET_STARTED_FOR_FREE
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

