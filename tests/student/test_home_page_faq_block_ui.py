import allure

from SpaceToStudy.ui.pages.home_page.home_student import HomePageStudent
from tests.test_runners import TestRunnerWithStudent


class TestHomePageFAQBlockUI(TestRunnerWithStudent):

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/332")
    def test_home_page_faq_block_ui(self):

        faq_title = HomePageStudent(self.driver).get_questions_block().get_name_questions_block()
        self.assertEqual("Frequently Asked Questions", faq_title)

        list_of_questions = HomePageStudent(self.driver).get_questions_items()
        self.assertEqual(4, len(list_of_questions))

        # alignment of the left side is checked
        left_side_positions = []
        for question in list_of_questions:
            position = self.driver.execute_script('''
                const rect = arguments[0].getBoundingClientRect();
                return rect.left;
            ''', question.node)
            left_side_positions.append(position)
        self.assertTrue(all(position == left_side_positions[0] for position in left_side_positions))





