from time import sleep

import allure
from selenium.webdriver.common.keys import Keys

from SpaceToStudy.ui.pages.header.header_component import HeaderComponent
from SpaceToStudy.ui.pages.header.header_unauthorized_component import HeaderUnauthorizedComponent
from SpaceToStudy.ui.pages.home_page.home_guest import HomePageGuest
from tests.ui.test_runners import BaseTestRunner


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
         .click_navigate_link_by_name("How it works"))
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

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/186")
    def test_who_we_are_block_contains_video_content(self):
        (HeaderComponent(self.driver)
         .get_navigate_links()[2]
         .click())
        video = (HomePageGuest(self.driver)
                 .get_who_we_are_block()
                 .get_video())
        self.assertTrue(video)

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/190")
    def test_open_who_we_are_block_by_tabs(self):
        logo = HeaderUnauthorizedComponent(self.driver).get_logo()
        logo.send_keys(Keys.TAB, 3, Keys.ENTER)
        title = (HomePageGuest(self.driver).get_who_we_are_block().get_title())
        self.assertEqual("Who we are", title)

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/198")
    def test_that_controls_active_after_navigating_to_them(self):
        sleep(1)
        (HeaderUnauthorizedComponent(self.driver)
         .get_navigate_links()[0]
         .click())
        become_a_student = (HomePageGuest(self.driver)
                            .get_card_learn_from_experts()
                            .get_btn())
        button_before_it_is_hovered_over = become_a_student.value_of_css_property("background-color")
        (HomePageGuest(self.driver).hover(become_a_student))
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

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/197")
    def test_visability_of_the_all_elements_after_resizing_for_what_can_you_do_block(self):
        window_width = 600
        window_height = 1000
        what_can_u_do_block = HomePageGuest(self.driver).click_navigate_link_in_header_by_name("What can you do")

        self.driver.minimize_window()
        what_can_u_do_elements = what_can_u_do_block.get_what_can_u_do_elements()
        for key, element in what_can_u_do_elements.items():
            self.assertTrue(element.is_displayed(), f"Element {key} is not displayed when window is minimized")

        HomePageGuest(self.driver).set_size_window(window_width, window_height)
        what_can_u_do_elements = what_can_u_do_block.get_what_can_u_do_elements()
        for key, element in what_can_u_do_elements.items():
            self.assertTrue(element.is_displayed(),
                            f"Element {key} is not displayed when a window size is set: width {window_width}, height {window_height}")

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

    @allure.testcase('https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/188')
    def test_visability_of_the_all_elements_after_zooming_for_who_we_are_block(self):
        zoom_page = '25%'
        who_we_are = HomePageGuest(self.driver).click_navigate_link_in_header_by_name("Who we are")
        who_we_are.driver.execute_script(f"document.body.style.zoom='{zoom_page}'")
        who_we_are_elements = (who_we_are
                               .get_who_we_are_block()
                               .get_who_we_are_elements())
        for key, element in who_we_are_elements.items():
            self.assertTrue(element.is_displayed(),
                            f"Element {key} is not displayed when a window zoom is set {zoom_page}")

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/187")
    def test_what_can_we_do_elements_in_center(self):
        (HeaderComponent(self.driver)
         .get_navigate_links()[2]
         .click())
        home_page = HomePageGuest(self.driver)
        video_display = (home_page
                         .get_who_we_are_block()
                         .get_video_display())
        text_aligning = (home_page
                         .get_who_we_are_block()
                         .get_text_aligning())
        self.assertEqual("block", video_display)
        self.assertEqual("center", text_aligning)


    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/179")
    def test_how_it_works_block_ui(self):
        width = 1920
        height = 1080
        self.driver.set_window_size(width, height)
        zoom = '100%'
        self.driver.execute_script(f"document.body.style.zoom = '{zoom}'")
        expected_sign_up_title_text = "Sign Up"
        expected_select_a_tutor_title_text = "Select a Tutor"
        expected_send_request_title_text = "Send Request"
        expected_start_learning_title_text = "Start Learning"
        expected_expected_titles = [expected_sign_up_title_text,
                                    expected_select_a_tutor_title_text,
                                    expected_send_request_title_text,
                                    expected_start_learning_title_text]

        expected_sign_up_description_text = "Registering on the Space2Study platform is very simple, just enter your email or use your Google account."
        expected_select_a_tutor_description_text = "Finding a tutor is very easy, select a subject from the list, and then pick the tutor, or enter his name and find directly."
        expected_send_request_description_text = "Write a request to the tutor in two clicks, where you indicate/confirm the price and the desired level of training."
        expected_start_learning_description_text = "After confirming the request, all training opportunities for the chosen course will open for you."
        expected_description_list = [expected_sign_up_description_text,
                                     expected_select_a_tutor_description_text,
                                     expected_send_request_description_text,
                                     expected_start_learning_description_text]
        expected_block_location_x = 387
        expected_location_y_first_element = expected_image_y_first_element = 2342
        expected_cards_retreat = 172
        expected_image_x = 903
        switcher = HomePageGuest(self.driver).get_checkbox_how_it_works_block()

        # print(switcher.is_displayed()) # False
        # print(switcher.is_enabled())   # True

        # self.assertTrue(switcher.is_displayed())

        def elements_and_labels_tests():
            how_it_works_cards_list = [HomePageGuest(self.driver).get_sign_up_items(),
                                       HomePageGuest(self.driver).get_select_a_tutor_items(),
                                       HomePageGuest(self.driver).get_send_request_items(),
                                       HomePageGuest(self.driver).get_start_learning_items()]

            # Verify UI elements alignment
            data_y_element_location = expected_location_y_first_element - expected_cards_retreat
            for card in how_it_works_cards_list:
                x = card.get_web_element().location['x']
                y = card.get_web_element().location['y']
                self.assertEqual(expected_block_location_x, x)
                distance_between_elements = y - data_y_element_location
                self.assertEqual(expected_cards_retreat, distance_between_elements)
                data_y_element_location = y

            data_y_image_location = expected_image_y_first_element
            for card in how_it_works_cards_list:
                x = card.get_image().location['x']
                y = card.get_image().location['y']
                self.assertEqual(expected_image_x, x)
                self.assertEqual(data_y_image_location, y)
                data_y_image_location += expected_cards_retreat

            # Verify labels spelling
            for card, expected_title in zip(how_it_works_cards_list, expected_expected_titles):
                el_title = card.get_name()
                self.assertEqual(expected_title, el_title)

            for card, expected_description in zip(how_it_works_cards_list, expected_description_list):
                el_description = card.get_description()
                self.assertEqual(expected_description, el_description)

            # Verify labels alignment
            first_name_element = how_it_works_cards_list[0].get_web_element_title().location['x']
            second_name_element = how_it_works_cards_list[1].get_web_element_title().location['x']
            third_name_element = how_it_works_cards_list[2].get_web_element_title().location['x']
            fourth_name_element = how_it_works_cards_list[3].get_web_element_title().location['x']
            self.assertEqual(first_name_element, third_name_element)
            self.assertEqual(second_name_element, fourth_name_element)

            first_description_element = how_it_works_cards_list[0].get_description_web_element()
            second_description_element = how_it_works_cards_list[1].get_description_web_element()
            third_description_element = how_it_works_cards_list[2].get_description_web_element()
            fourth_description_element = how_it_works_cards_list[3].get_description_web_element()
            self.assertEqual(first_description_element.location['x'], third_description_element.location['x'])

            first_element_size = second_description_element.size
            fourth_element_size = fourth_description_element.size
            self.assertEqual(second_description_element.location['x'] + first_element_size['width'], fourth_description_element.location['x'] + fourth_element_size['width'])

            # Verify that all UI controls are visible on the screen after resizing
            resized_width = 1366
            resized_height = 768
            self.driver.set_window_size(resized_width, resized_height)

            for card in how_it_works_cards_list:
                data_block = card.get_web_element()
                self.assertTrue(data_block.is_displayed())

            # Verify that the “Become a student”/“Become a tutor” button changes color on hover.
            button_become_a_student_tutor = HomePageGuest(self.driver).get_button_become_a_student_tutor()
            expected_button_basic_color = "rgba(38, 50, 56, 1)"
            expected_button_hovered_color = "rgba(69, 90, 100, 1)"
            basic_button_color = button_become_a_student_tutor.value_of_css_property("background-color")
            self.assertEqual(basic_button_color, expected_button_basic_color)
            (HomePageGuest(self.driver).hover(button_become_a_student_tutor))
            hover_button_color = button_become_a_student_tutor.value_of_css_property("background-color")
            self.assertEqual(hover_button_color, expected_button_hovered_color)

        elements_and_labels_tests()

        self.driver.set_window_size(width, height)
        self.driver.execute_script(f"document.body.style.zoom = '{zoom}'")
        switcher.click()
        sleep(2)

        expected_block_location_x = 387
        expected_location_y_first_element = expected_image_y_first_element = 151

        expected_sign_up_title_text = "Sign Up"
        expected_select_a_tutor_title_text = "Create a Tutor Account"
        expected_send_request_title_text = "Get New Students"
        expected_start_learning_title_text = "Receive Feedbacks"

        expected_expected_titles = [expected_sign_up_title_text,
                                    expected_select_a_tutor_title_text,
                                    expected_send_request_title_text,
                                    expected_start_learning_title_text]

        expected_sign_up_description_text = "Registering on the Space2Study platform is very simple, just enter your email or use your Google account."
        expected_select_a_tutor_description_text = "Creating a tutor account is easy, you just need to select a subject, upload teaching materials and create an offer."
        expected_send_request_description_text = "Create fruitful cooperation with your students, confirming their requests, and start teaching."
        expected_start_learning_description_text = "Receive positive feedback for your work to become popular and get even more satisfied students."
        expected_description_list = [expected_sign_up_description_text,
                                     expected_select_a_tutor_description_text,
                                     expected_send_request_description_text,
                                     expected_start_learning_description_text]

        elements_and_labels_tests()

        # Verify that all UI controls are active and focused when navigating by “Tab” keyboard button.
        HeaderUnauthorizedComponent(self.driver).tab_key(13)
        is_button_selected = (HomePageGuest(self.driver).is_button_become_a_student_tutor_selected())
        self.assertTrue(is_button_selected)




    @allure.testcase('https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/189')
    def test_visability_of_the_all_elements_after_resizing_for_who_we_are_block(self):
        window_width = 600
        window_height = 1000
        who_we_are = (HomePageGuest(self.driver)
                              .get_header()
                              .get_navigate_links()[2]
                              .click())
        HomePageGuest(self.driver).set_size_window(window_width, window_height)
        who_we_are_elements = HomePageGuest(who_we_are)
        sleep(10)
        who_we_are_elements = (who_we_are_elements.get_who_we_are_block()
                               .get_who_we_are_elements())
        for element in who_we_are_elements.values():
            self.assertTrue(element.is_displayed(), f"Element {element} isn't displayed")
