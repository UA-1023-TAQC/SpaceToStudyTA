import allure


from selenium.webdriver import Keys

from SpaceToStudy.ui.pages.categories.categories_page import CategoriesPage
from SpaceToStudy.ui.pages.header.header_component import HeaderComponent
from tests.test_runners import TestRunnerWithStudent
from SpaceToStudy.ui.pages.explore_offers.explore_offers_page import ExploreOffersPage
from SpaceToStudy.ui.pages.home_page.home_student import HomePageStudent


class TestHomePageStudent(TestRunnerWithStudent):

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/218")
    def test_student_can_see_tutors_offers_at_the_home_page(self):
        (HomePageStudent(self.driver)
         .get_search_input()
         .click_find_tutor_btn())
        list_of_offers = (ExploreOffersPage(self.driver)
                          .get_list_of_offers_grid_card())
        self.assertIsNotNone(list_of_offers, "There are no offers")

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/283")
    def test_the_ui_welcoming_block(self):
        get_input_line = (HomePageStudent(self.driver)
                          .get_search_input()
                          .get_input()
                          .get_attribute("placeholder"))
        get_find_tutor = (HomePageStudent(self.driver)
                          .get_text_button_find_tutor)
        self.assertTrue("What would you like to learn ?", get_input_line)
        self.assertTrue("Find tutor", get_find_tutor)

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/284")
    def test_the_welcoming_block_controls_active_after_navigating_to_them(self):
        find_tutor_btn = (HomePageStudent(self.driver)
                          .get_button_find_tutor())
        before_hover = find_tutor_btn.value_of_css_property("background-color")
        after_hover = (HomePageStudent(self.driver)
                       .hover(find_tutor_btn)
                       .value_of_css_property("background-color"))
        self.assertNotEqual(before_hover, after_hover, "The button hasn't changed")

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/284")
    def test_the_welcoming_block_controls_active_after_navigating_to_them_by_tab(self):
        (HomePageStudent(self.driver)
         .get_search_input()
         .get_input()
         .send_keys(Keys.TAB))
        after_hover = (HomePageStudent(self.driver).get_tub_animation())
        self.assertTrue(after_hover, "There is no animation")

    @allure.testcase('https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/305')
    @allure.title('Verify that a Student can find popular learning categories and choose one at the home page')
    def test_verify_student_can_find_popular_categories(self):
        card_element = (HomePageStudent(self.driver).get_categories())[1]
        name = card_element.get_name()
        self.assertEqual("Computer science", name)
        card_element.click()
        title = CategoriesPage(self.driver).get_categories_title()
        self.assertEqual("Computer science Subjects", title)
        sub_category_name = (CategoriesPage(self.driver).get_cards())[0].get_title()
        self.assertEqual("Cybersecurity", sub_category_name)

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/219")
    def test_the_ui_welcoming_block_resize(self):
        HomePageStudent(self.driver).set_size_window(899, 1080)
        tablet_input_block = (HomePageStudent(self.driver).get_search_input().node.size['width'])
        tablet_input = (HomePageStudent(self.driver).get_search_input().get_input().size['width'])
        tablet_find_tutor_btn = (HomePageStudent(self.driver).get_search_input().get_find_tutor_btn().size['width'])
        self.assertEqual(777, tablet_input_block, "The item is not the right size")
        self.assertEqual(563, tablet_input, "The item is not the right size")
        self.assertEqual(130, tablet_find_tutor_btn, "The item is not the right size")
        HomePageStudent(self.driver).set_size_window(599, 1080)
        mobile_input_block = (HomePageStudent(self.driver).get_search_input().node.size['width'])
        mobile_input = (HomePageStudent(self.driver).get_search_input().get_input().size['width'])
        mobile_find_tutor_btn = (HomePageStudent(self.driver).get_search_input().get_find_tutor_btn().size['width'])
        self.assertEqual(493, mobile_input_block, "The item is not the right size")
        self.assertEqual(445, mobile_input, "The item is not the right size")
        self.assertEqual(493, mobile_find_tutor_btn, "The item is not the right size")

    @allure.testcase('https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/333')
    @allure.title('Verify that a Student can see all tutor’s offers at the home page')
    def test_student_view_tutor_offers(self):
        (HeaderComponent(self.driver)
         .get_navigate_links())[1]\
            .click()
        how_it_works_block = (HomePageStudent(self.driver)
                              .get_how_it_works_block_student())
        block_title = how_it_works_block.get_block_name_student()
        self.assertEqual('How it works', block_title)
        explore_offers = how_it_works_block.click_find_tutor_btn()
        title = explore_offers.get_title_text()
        self.assertEqual("Explore Offers", title)
        self.assertEqual(8, len(explore_offers.get_list_of_offers_inline_card()))
