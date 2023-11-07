from behave import *

from SpaceToStudy.ui.pages.home_page.home_guest import HomePageGuest
from SpaceToStudy.ui.pages.login_modal.login_modal import LoginModal


@when('I click the "Login" button in the upper right corner of the header')
def click_login_btn(context):
    (HomePageGuest(context.driver)
     .get_header()
     .click_login_btn())


@then('A modal window with the title "Welcome" opens')
@then('Login modal remained open')
def open_welcome_login_modal(context):
    assert LoginModal(context).get_title_text() == "Welcome back"


@when('I click outside the login modal')
def click_outside_the_login_modal(context):
    LoginModal(context).outside_click()
