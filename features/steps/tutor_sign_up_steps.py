from behave import *

from SpaceToStudy.ui.pages.home_page.home_guest import HomePageGuest
from SpaceToStudy.ui.pages.sign_up_modal.sign_up_modal import RegistrationModal


@given('the "get started for free" button is clicked')
def click_get_started_for_free(context):
    HomePageGuest(context.driver).click_started_for_free()


@given('the "become a tutor" button is clicked')
def click_become_a_tutor(context):
    HomePageGuest(context.driver).click_become_a_tutor()


@when('I enter first name "{first_name}"')
def enter_first_name(context, first_name):
    RegistrationModal(context.driver).set_first_name(first_name)


@when('I click on the "I agree" checkbox')
def click_i_agree_checkbox(context):
    RegistrationModal(context.driver).click_i_agree_checkbox()


@then('The error message "This field cannot be longer than 30 characters" is displayed')
def verify_error_message(context):
    error_msg = RegistrationModal(context.driver).get_first_name_error_message()
    assert error_msg == "This field cannot be longer than 30 characters"
