
from SpaceToStudy.ui.pages.header.header_authorized_component import HeaderAuthorizedComponent

from SpaceToStudy.ui.pages.my_offers_page import MyOffersPage
from tests.test_runners import TestRunnerWithTutor


class MyOffers(TestRunnerWithTutor):

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/117")
    def test_offers_sort_price_low_high(self):
        menu = HeaderAuthorizedComponent(self.driver)
        (menu.get_user_menu()
         .click_account()
         .click_menu_items_my_offers())
        offers = MyOffersPage(self.driver)
        (offers
         .get_offers_interaction()
         .click_grid_btn()
         .click_get_sort()
         .click_low_high())
        expected = sorted(offers.get_list_prices())
        actual = offers.get_list_prices()
        self.assertEqual(expected, actual)

    @allure.testcase("https://github.com/UA-1023-TAQC/SpaceToStudyTA/issues/117")
    def test_offers_sort_price_high_low(self):
        menu = HeaderAuthorizedComponent(self.driver)
        (menu.get_user_menu()
         .click_account()
         .click_menu_items_my_offers())
        offers = MyOffersPage(self.driver)
        (offers
         .get_offers_interaction()
         .click_grid_btn()
         .click_get_sort()
         .click_high_low())
        expected = sorted(offers.get_list_prices(), reverse=True)
        actual = offers.get_list_prices()
        self.assertEqual(expected, actual)
