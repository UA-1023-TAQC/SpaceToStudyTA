import time

from behave import *
from tests.utils.value_provider import ValueProvider
from SpaceToStudy.ui.pages.home_page.home_guest import HomePageGuest


@when("I open the Home page")
def step_open_home_page(context):

    pass

@then('I should see the "{button_text}" button displayed')
def step_check_button_displayed(context, button_text):
    pass

@then('I hover over the "Go to categories" button')
def step_3(context):
    pass

@then('the "Go to categories" button color should change to dark grey')
def step_4(context):
    pass


@given("the site is opened")
def step_impl1(context):
    page = HomePageGuest(context.driver)
    assert page.get_header().get_logo() is not None
    """
    :type context: behave.runner.Context
    """
    # raise NotImplementedError(u'STEP: Given the site is opened')


@given("the user is logged in as a Student")
def step_impl2(context):
    (HomePageGuest(context.driver)
     .get_header()
     .click_login_btn()
     .set_email(ValueProvider.get_student_email())
     .set_password(ValueProvider.get_student_password())
     .click_login_button())



@step('I hover over the "Go to categories" button')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # raise NotImplementedError(u'STEP: And I hover over the "Go to categories" button')