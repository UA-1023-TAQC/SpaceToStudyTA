import allure

from SpaceToStudy.ui.pages.home_page.home_student import HomePageStudent
from tests.test_runners import TestRunnerWithStudent


class TestHomePageFAQBlockUI(TestRunnerWithStudent):

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/332")
    def test_home_page_faq_block_ui(self):

        # Checking FAQ title
        faq_title = HomePageStudent(self.driver).get_questions_block().get_name_questions_block()
        self.assertEqual("Frequently Asked Questions", faq_title)

        # Checking the number of questions in FAQ block
        list_of_questions = HomePageStudent(self.driver).get_questions_items()
        self.assertEqual(4, len(list_of_questions))

        # Checking the alignment of the left side of question blocks
        # left_side_block_positions = []
        # for question in list_of_questions:
        #     position = question.location['x']
        #     left_side_block_positions.append(position)
        # self.assertTrue(all(position == left_side_block_positions[0] for position in left_side_block_positions))

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






