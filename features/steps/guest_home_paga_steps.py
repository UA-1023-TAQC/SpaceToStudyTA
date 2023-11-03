from behave import *


@when("I click on the {button_text} button")
def step_click_get_started_button(context, button_text):
    pass


@when("page scrolled down to the {block_name} block")
def step_what_can_you_do_block_is_displayed(context, block_name):
    pass


@when("I click on the {button_text} button")
def step_click_become_a_tutor_button(context, button_text):
    pass


@then("the {registration_modal} modal is open")
def step_open_registration_modal(context, registration_modal):
    pass


@when("I enter {first_name} in the first name field")
def step_enter_first_name(context, first_name):
    pass


@when("I enter {last_name} in the last name field")
def step_enter_last_name(context, last_name):
    pass


@when("I enter {email} in the email field")
def step_enter_email(context, email):
    pass


@when("I enter {password} in the password field")
def step_enter_incorrect_password(context, password):
    pass


@then("the the error message {error_message} is displayed")
def step_error_message_is_displayed(context, error_message):
    pass