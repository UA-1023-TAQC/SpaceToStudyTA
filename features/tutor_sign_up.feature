Feature: Verify first name input validation for tutor's sign up

  Scenario: Verify first name input validation for tutor's sign up
    Given the site is opened
    And the "get started for free" button is clicked
    And the "become a tutor" button is clicked
    When I enter first name "Vzxcvbnmaszxcvbnmasdasdfghjklqw"
    And I click on the "I agree" checkbox
    Then the error message "This field cannot be longer than 30 characters" is displayed