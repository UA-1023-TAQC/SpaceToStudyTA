Feature: Verify that the Guest is shown the tutor registration modal window after clicking the "Get started for free" button

  Background:
    Given the site is opened
    And the user is not logged in as a Student

  Scenario: Verify the student registration modal window is displayed for the guest
    When I click on the “Get started for free” button
    When page scrolled down to the What can you do block
    When I click on the “Become a tutor” button
    Then the "Sign up as a tutor" modal window is open