from behave import *

from SpaceToStudy.ui.pages.explore_offers.explore_offers_page import ExploreOffersPage
from SpaceToStudy.ui.pages.home_page.home_student import HomePageStudent


@When('the student clicks on the "Find a Tutor" button')
def step_click_find_a_tutor_button(context):
    (HomePageStudent(context.driver)
     .get_search_input()
     .click_find_tutor_btn())


@Then("the student should see a list of tutors' offers")
def step_verify_tutors_offers(context):
    list_of_offers = (ExploreOffersPage(context.driver)
                      .get_list_of_offers_inline_card())
    assert list_of_offers is not None, "There are no offers"
