import allure
from selenium.webdriver import Keys

from SpaceToStudy.ui.pages.categories.categories_page import CategoriesPage
from SpaceToStudy.ui.pages.explore_offers.explore_offers_page import ExploreOffersPage
from SpaceToStudy.ui.pages.header.header_component import HeaderComponent
from SpaceToStudy.ui.pages.home_page.home_student import HomePageStudent
from tests.ui.test_runners import TestRunnerWithStudent


class TestHomePageStudent(TestRunnerWithStudent):

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/218")
    def test_student_can_see_tutors_offers_at_the_home_page(self):
        (HomePageStudent(self.driver)
         .get_search_input()
         .click_find_tutor_btn())
        list_of_offers = (ExploreOffersPage(self.driver)
                          .get_list_of_offers_inline_card())
        self.assertIsNotNone(list_of_offers, "There are no offers")

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/283")
    def test_the_ui_welcoming_block(self):
        get_input_line = (HomePageStudent(self.driver)
                          .get_search_input()
                          .get_input()
                          .get_attribute("placeholder"))
        get_find_tutor = (HomePageStudent(self.driver)
                          .get_text_button_find_tutor())
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
         .get_navigate_links())[1] \
            .click()
        how_it_works_block = (HomePageStudent(self.driver)
                              .get_how_it_works_block_student())
        block_title = how_it_works_block.get_block_name_student()
        self.assertEqual('How it works', block_title)
        explore_offers = how_it_works_block.click_find_tutor_btn()
        title = explore_offers.get_title_text()
        self.assertEqual("Explore Offers", title)
        self.assertEqual(8, len(explore_offers.get_list_of_offers_inline_card()))

    @allure.step("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/306")
    def test_student_home_page_availability_learning_categories(self):
        home = HomePageStudent(self.driver)
        cards = home.get_categories()[0]
        name = cards.get_name()
        self.assertEqual(name, "Music")
        offers = cards.get_offers()
        self.assertEqual(offers, "28 offers")
        home.click_button_go_to_categories()
        title_of_page = CategoriesPage(self.driver).get_categories_title()
        self.assertEqual(title_of_page, "Categories")

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/334",
                     "Check the student’s home page How it works block UI Test 1")
    def test_how_it_works_ui_find_tutor_btn(self):
        find_tutor_btn = (HomePageStudent(self.driver)
                          .click_navigate_link_in_header_by_name("How it works")
                          .get_how_it_works_block_student()
                          .get_find_tutor_btn())
        find_tutor_is_displayed = find_tutor_btn.is_displayed()
        self.assertTrue(find_tutor_is_displayed, "'Find tutor' button isn't displayed on the page")

        find_tutor_background_color = find_tutor_btn.value_of_css_property("background-color")
        hover_find_tutor_background_color = (HomePageStudent(self.driver)
                                             .hover(find_tutor_btn)
                                             .value_of_css_property("background-color"))
        self.assertNotEqual(find_tutor_background_color, hover_find_tutor_background_color,
                            "'Find tutor' button doesn't changes color when hovered over")

        button_class_with_tab_animation = "Mui-focusVisible"
        find_tutor_class = find_tutor_btn.get_attribute("class")
        self.assertTrue(button_class_with_tab_animation not in find_tutor_class,
                        "'Find tutor' button is flashing without being hovered over or pressed with TAB key")

        (HomePageStudent(self.driver).get_button_go_to_categories().send_keys(Keys.TAB))
        tab_find_tutor_class = find_tutor_btn.get_attribute("class")
        self.assertTrue(button_class_with_tab_animation in tab_find_tutor_class,
                        "'Find tutor' button is not flashing when hovered over by pressing TAB key")
