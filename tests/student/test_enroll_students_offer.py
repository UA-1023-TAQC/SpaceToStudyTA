import unittest
from time import sleep

from SpaceToStudy.ui.pages.home_page.home_student import HomePageStudent
from tests.test_runners import TestRunnerWithStudent


class EnrollStudentsOffer(TestRunnerWithStudent):

    def test_enroll_tutors_offer_with_default_values(self):
        list_of_offers = (HomePageStudent(self.driver)
                          .click_button_go_to_categories()  # main Student -> Categories
                          .click_show_all_offers_btn()  # Categories -> Find offers (explore offers)
                          .get_list_of_filtered_offers)  # returns list
        sleep(5)

        item = list_of_offers[0]  # TypeError <class 'method'>
        var = (item.click_view_details_btn  # (OfferDetailsPage)
               .click_enroll_offer_btn)
        sleep(5)


if __name__ == '__main__':
    unittest.main(verbosity=2)
