Feature: Login Popup Functionality

  Scenario: Verify the "Login" button is disabled without entering data into required inputs
    Given the site is opened
    And the "Login" button on the header is clicked
    When I leave Email" and "Password" fields empty and hover the mouse over the "Login" button
    Then I should see that the Login button background-color is greyed out
    And the "Login" button is non-clickable