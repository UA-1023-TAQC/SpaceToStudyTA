from time import sleep

from selenium.webdriver.common.by import By

from SpaceToStudy.ui.pages.explore_offers.explore_offers_page import ExploreOffersPage, LIST_OF_OFFERS
from SpaceToStudy.ui.pages.explore_offers.search_by_tutor_name_component import SearchByTutorNameComponent
from SpaceToStudy.ui.pages.home_page.home_student import HomePageStudent

from tests.test_runners import TestRunnerWithStudent


class SortingAndFilteringAllOffersTestCase(TestRunnerWithStudent):

    def test_filters_by_category_subject_and_tutors_name(self):
        home_page_student = HomePageStudent(self.driver)
        sleep(0.2)
        home_page_student.go_to_url(ExploreOffersPage.get_explore_offers_page_address())
        sleep(0.2)
        search_by_tutor_name_component = SearchByTutorNameComponent(self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div[4]/div"))
        sleep(0.2)
        (search_by_tutor_name_component.set_categories_input("Music")
                                       .navigate_categories_input_down()
                                       .choose_categories_item())
        sleep(0.2)
        self.assertEqual(search_by_tutor_name_component.get_categories_input_text(), "Music")
        (search_by_tutor_name_component.set_subjects_input("Guitar")
                                       .navigate_subjects_input_down()
                                       .choose_subjects_item())
        self.assertEqual(search_by_tutor_name_component.get_subjects_input_text(), "Guitar")
        search_by_tutor_name_component.set_search_by_tutor_name_input("Yura")
        sleep(0.2)
        self.assertEqual(search_by_tutor_name_component.get_search_by_tutor_name_input_text(), "Yura")
        search_by_tutor_name_component.click_search_btn()
        sleep(2)
        list_of_filtered_offers = ExploreOffersPage(self.driver.find_element(*LIST_OF_OFFERS))
        self.assertEqual(len(list_of_filtered_offers.get_list_of_filtered_offers()), 2)
        for offer in list_of_filtered_offers.get_list_of_filtered_offers():
            self.assertEqual("GUITAR", offer.get_subject_label())
            self.assertIn("Yura", offer.get_person_name())
