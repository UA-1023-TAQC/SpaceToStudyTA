from behave import *

from SpaceToStudy.ui.pages.header.header_unauthorized_component import HeaderUnauthorizedComponent
from SpaceToStudy.ui.pages.login_modal.login_modal import LoginModal


@given('the "Login" button on the header is clicked')
def click_login_button_on_header(context):
    HeaderUnauthorizedComponent(context.driver).click_login_btn()


@when('I leave Email" and "Password" fields empty and hover the mouse over the "Login" button')
def get_login_button(context):
    context.button = LoginModal(context.driver).get_login_button()


@then('I should see that the Login button background-color is greyed out')
def verify_login_button_background_color(context):
    expected_background_color = "rgba(0, 0, 0, 0.12)"
    actual_background_color = context.button.get_value_css_property("background-color")
    assert actual_background_color == expected_background_color


@then('the "Login" button is non-clickable')
def verify_login_button_non_clickable(context):
    button_state = context.button.is_enabled_button()
    assert button_state is False
