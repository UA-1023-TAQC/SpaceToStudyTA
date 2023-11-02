Feature: Verify registration modal

  Background:
    Given the site is opened
    And the user is not logged in as a Student

  Scenario: Verify the student registration modal window is displayed for the guest
    When I click on the “Get started for free” button
    And page scrolled down to the What can you do block
    And I click on the “Become a tutor” button
    Then the "Sign up as a tutor" modal window is open