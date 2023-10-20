import allure
from selenium.webdriver import ActionChains, Keys

from SpaceToStudy.ui.pages.home_page.home_tutor import HomePageTutor
from tests.ui.test_runners import TestRunnerWithTutor


class HomePageTestCase(TestRunnerWithTutor):
    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/373")
    def test_welcoming_block_ui(self):
        home = HomePageTutor(self.driver)
        self.assertTrue(home.get_search_input().is_displayed())
        self.assertTrue(home.get_search_input_placeholder() == "Who or what do you want to teach?")
        self.assertTrue(home.get_find_student_btn().is_displayed())
        self.assertTrue(home.get_title_text() == "A Global Network of Students")
        self.assertTrue(home.get_description_text() == "A Space2Study platform is the best place where you can teach. "
                                                       "Type who or what would you like to teach and find students "
                                                       "for that.")
        # Checking button flashing after TAB
        self.assertFalse(home.check_find_student_btn_is_flashing())
        home.get_search_input().send_keys(Keys.TAB)
        self.assertTrue(home.check_find_student_btn_is_flashing())

        # Checking color change on hover
        initial_color = home.get_find_student_btn().value_of_css_property("background-color")
        actions = ActionChains(self.driver)
        actions.move_to_element(home.get_find_student_btn()).perform()
        final_color = home.get_find_student_btn().value_of_css_property("background-color")
        self.assertNotEqual(initial_color, final_color)

        # Calling maximize_window() again (after setUp) restores the window size
        self.driver.maximize_window()
        self.assertTrue(home.get_search_input().is_displayed())
        self.assertTrue(home.get_find_student_btn().is_displayed())
        self.driver.maximize_window()  # Restore maximal window size for following tests

        # Checking visibility after manual resize
        self.driver.set_window_size(800, 1200)
        self.assertTrue(home.get_search_input().is_displayed())
        self.assertTrue(home.get_find_student_btn().is_displayed())
