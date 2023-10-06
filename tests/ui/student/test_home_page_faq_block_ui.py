import allure
from selenium.webdriver.common.action_chains import ActionChains

from SpaceToStudy.ui.pages.home_page.home_student import HomePageStudent
from tests.test_runners import TestRunnerWithStudent


class TestHomePageFAQBlockUI(TestRunnerWithStudent):

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/332")
    def test_home_page_faq_block_ui(self):
        home = HomePageStudent(self.driver)

        # Checking FAQ title
        faq_title = home.get_questions_block().get_name_questions_block()
        self.assertEqual("Frequently Asked Questions", faq_title)

        # Checking the number of questions in FAQ block
        list_of_questions = home.get_questions_items()
        self.assertEqual(4, len(list_of_questions))

        # Checking the alignment of the left side of question blocks
        left_side_block_positions = []
        for question in list_of_questions:
            position = question.node.location['x']
            left_side_block_positions.append(position)
        self.assertTrue(all(position == left_side_block_positions[0] for position in left_side_block_positions))

        # Verifying of labels spelling
        self.assertEqual("How to find a tutor", list_of_questions[0].get_text_title_items())
        self.assertEqual("How to book a lesson", list_of_questions[1].get_text_title_items())
        self.assertEqual("Rules for students", list_of_questions[2].get_text_title_items())
        self.assertEqual("How you can pay for lessons", list_of_questions[3].get_text_title_items())

        # Checking the alignment of the left side of text in question blocks
        left_side_text_positions = []
        for question in list_of_questions:
            position = question.node.location['x']
            left_side_text_positions.append(position)
        self.assertTrue(all(position == left_side_text_positions[0] for position in left_side_text_positions))

        # Checking visibility of FAQ block after resize
        # Calling maximize_window() again (after setUp) restores the window size
        self.driver.maximize_window()
        faq_title = home.get_questions_block().get_name_questions_block()
        self.assertEqual("Frequently Asked Questions", faq_title)
        list_of_questions = home.get_questions_items()
        self.assertEqual(4, len(list_of_questions))

        # Checking visibility of FAQ block after manual resize
        self.driver.set_window_size(800, 1200)
        faq_title = home.get_questions_block().get_name_questions_block()
        self.assertEqual("Frequently Asked Questions", faq_title)
        list_of_questions = home.get_questions_items()
        self.assertEqual(4, len(list_of_questions))
        self.driver.maximize_window()  # Restore maximal window size for following tests

        # Checking highlighting on hover
        for question in list_of_questions:
            self.assertIn('rgba(144, 164, 174, 0.12)', question.node.value_of_css_property('box-shadow'))
            actions = ActionChains(self.driver)
            actions.move_to_element(question.node).perform()
            self.assertIn('rgba(144, 164, 174, 0.56)', question.node.value_of_css_property('box-shadow'))

        # Checking the background color of the questions before and after pressing TAB
        for item_index, question in enumerate(list_of_questions):
            self.assertEqual('rgba(0, 0, 0, 0)', question.get_background_color_of_item_block())
            question.go_to_item_by_pressing_tab(item_index + 1)
            self.assertEqual('rgba(0, 0, 0, 0.12)', question.get_background_color_of_item_block())






