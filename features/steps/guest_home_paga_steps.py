from behave import *

from SpaceToStudy.ui.pages.home_page.home_guest import HomePageGuest
from SpaceToStudy.ui.pages.sign_up_modal.sign_up_modal import RegistrationModal


@when('I click on the "Get started for free" button')
def step_click_get_started_button(context):
    HomePageGuest(context.driver).click_started_for_free()


@when('page scrolled down to the "What can you do" block')
def step_what_can_you_do_block_is_displayed(context):
    block_is_displayed = HomePageGuest(context.driver).get_what_can_u_do_block().is_displayed()
    assert (bool(block_is_displayed), True)


@when('I click on the "Become a tutor button" button')
def step_click_become_a_tutor_button(context):
    HomePageGuest(context.driver).click_become_a_tutor()


@then('the Registration modal is open')
def step_open_registration_modal(context):
    RegistrationModal(context.driver).is_displayed()


@when('I enter {first_name} in the first name field')
def step_enter_first_name(context, first_name):
    RegistrationModal(context.driver).set_first_name(first_name)


@when('I enter {last_name} in the last name field')
def step_enter_last_name(context, last_name):
    RegistrationModal(context.driver).set_last_name(last_name)


@when('I enter {email} in the email field')
def step_enter_email(context, email):
    RegistrationModal(context.driver).set_email(email)


@when('I enter {password} in the password field')
def step_enter_incorrect_password(context, password):
    RegistrationModal(context.driver).set_password(password)


@then('the password "Password must contain at least one alphabetic and one numeric character" is displayed')
def step_error_message_is_displayed(context):
    message = RegistrationModal(context.driver).get_password_error_message()
    assert message == "Password must contain at least one alphabetic and one numeric character"


@then('the password "Password cannot be shorter than 8 and longer than 25 characters" is displayed')
def step_error_message_is_displayed(context):
    message = RegistrationModal(context.driver).get_password_error_message()
    assert message == "Password cannot be shorter than 8 and longer than 25 characters"
