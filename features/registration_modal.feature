Feature: Verify registration modal

  Background:
    Given the site is opened
    And the user is not logged in as a Student

  Scenario: Verify the tutor registration modal window is displayed for the guest
    Given the Home page is opened
    When I click on the “Get started for free” button
    And page scrolled down to the What can you do block
    And I click on the “Become a tutor” button
    Then the "Sign up as a tutor" modal window is open

  Scenario: Verify the tutor registration password without alphabetic numeric character
    Given the Home page is opened
    When I click on the “Get started for free” button
    And page scrolled down to the What can you do block
    And I click on the “Become a tutor” button
    And I enter "test" in the first name field
    And I enter "test" in the last name field
    And I enter "test@gmail.com" in the email field
    And I enter "@#$%//////" in the password field
    Then the error message "Password must contain at least one alphabetic and one numeric character" is displayed