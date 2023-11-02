from behave import *

from SpaceToStudy.ui.pages.categories.categories_page import CategoriesPage
from SpaceToStudy.ui.pages.explore_offers.explore_offers_page import ExploreOffersPage
from SpaceToStudy.ui.pages.home_page.home_student import HomePageStudent


@when('I click "Go to categories"')
def step_impl(context):
    HomePageStudent(context.driver).click_button_go_to_categories()


@when('I click "Show all offers"')
def step_impl(context):
    CategoriesPage(context.driver).click_show_all_offers_btn()


@when('I click "Filters"')
def step_impl(context):
    ExploreOffersPage(context.driver)\
        .get_filtering_and_sorting_block()\
        .click_filter_title()


@when('I click "Beginner" level checkbox')
def step_impl(context):
    ExploreOffersPage(context.driver)\
        .get_filtering_and_sorting_block()\
        .get_filters_sidebar_component()\
        .click_level_beginner_checkbox()


@when('I click "Apply filters" button')
def step_impl(context):
    ExploreOffersPage(context.driver) \
        .get_filtering_and_sorting_block() \
        .get_filters_sidebar_component()\
        .click_apply_filters_btn()


@then('Every offer in the list of filtered offers contains "BEGINNER" label')
def step_impl(context):
    for offer in ExploreOffersPage(context.driver).get_list_of_offers_inline_card():
        assert "BEGINNER" in offer.get_level_label()


@then('I can see number "1" near "Filters" button')
def step_impl(context):
    filter_quantity = ExploreOffersPage(context.driver) \
        .get_filtering_and_sorting_block() \
        .get_filter_quantity_number()
    assert filter_quantity == 1
