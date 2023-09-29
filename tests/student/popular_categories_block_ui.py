import allure
import re
from SpaceToStudy.ui.pages.home_page.home_student import HomePageStudent, BUTTON_GO_TO_CATEGORIES
from tests.test_runners import TestRunnerWithStudent


class PopularCategoriesBlockUI(TestRunnerWithStudent):

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/203")
    def test_popular_categories_block_ui_button(self):
        button_is_displayed = (HomePageStudent(self.driver)
                               .get_button_go_to_categories()
                               .is_displayed())
        button_text = (HomePageStudent(self.driver)
                       .get_text_button_go_to_categories())
        button = self.driver.find_element(*BUTTON_GO_TO_CATEGORIES)
        button_hover = (HomePageStudent(self.driver)
                        .hover(button)
                        .value_of_css_property("background-color"))
        self.assertEqual("rgba(0, 0, 0, 0.04)", button_hover)
        page_is_displayed = (HomePageStudent(self.driver)
                             .click_button_go_to_categories()
                             .get_categories_block()
                             .is_displayed())
        self.assertEqual("Go to categories", button_text)
        self.assertTrue(button_is_displayed, "Button is not displayed")
        self.assertTrue(page_is_displayed, "Page is not displayed")

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/345")
    def test_popular_categories_block_ui_text(self):
        music = "Music"
        computer = "Computer science"
        design = "Design"
        dance = "Dance"
        mathematics = "Mathematics"
        languages = "Languages"
        title_block = "Popular Categories"
        descriptions_block = "Explore tutoring categories you're passionate about."
        get_title_block = (HomePageStudent(self.driver).get_title_categories_block())
        get_descriptions_block = (HomePageStudent(self.driver).get_description_categories_block())
        category_music = (HomePageStudent(self.driver).get_categories()[0].get_name())
        category_computer = (HomePageStudent(self.driver).get_categories()[1].get_name())
        category_design = (HomePageStudent(self.driver).get_categories()[2].get_name())
        category_dance = (HomePageStudent(self.driver).get_categories()[3].get_name())
        category_mathematics = (HomePageStudent(self.driver).get_categories()[4].get_name())
        category_languages = (HomePageStudent(self.driver).get_categories()[5].get_name())
        self.assertEqual(title_block, get_title_block)
        self.assertEqual(descriptions_block, get_descriptions_block)
        self.assertEqual(music, category_music)
        self.assertEqual(computer, category_computer)
        self.assertEqual(design, category_design)
        self.assertEqual(dance, category_dance)
        self.assertEqual(mathematics, category_mathematics)
        self.assertEqual(languages, category_languages)

        offers = (HomePageStudent(self.driver).get_categories())
        self.list_offers_without_digits = []
        for i in offers:
            text_offers = i.get_offers()
            text_offers_without_digits = re.sub(r"[^A-Za-z]", "", text_offers)
            self.list_offers_without_digits.append(text_offers_without_digits)
        for element in self.list_offers_without_digits:
            self.assertEqual("offers", element)



