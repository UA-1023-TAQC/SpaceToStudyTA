Feature: Verify login modal
  Background:
    Given The website open in a web browser.
    And The user is not logged in on the website.

  Scenario: Verify that the user cannot close the login modal by clicking outside of it
    When I click the "Login" button in the upper right corner of the header
    When A modal window with the title "Welcome" opens
    When I сlick outside the login modal
    Then Login modal remained open