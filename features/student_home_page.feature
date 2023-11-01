Feature: Verify UI of general information about Space2Study platform

  Background:
    Given the site is opened
    And the user is logged in as a Student

  Scenario: Verify "Go to categories" button
    When I open the Home page
    Then I should see the "Go to categories" button displayed
#
#  Scenario: Verify "Go to categories" button color on hover
#    When I open the Home page
#    And I hover over the "Go to categories" button
#    Then the "Go to categories" button color should change to dark grey



