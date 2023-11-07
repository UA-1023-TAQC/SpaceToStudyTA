Feature: Verify UI of general information about Space2Study platform

#  Background:
#    Given the site is opened
#    And the user is logged in as a Student
  @student
  Scenario: Verify "Go to categories" button
    When I open the Home page
    Then I should see the "Go to categories" button displayed
#
#  Scenario: Verify "Go to categories" button color on hover
#    When I open the Home page
#    And I hover over the "Go to categories" button
#    Then the "Go to categories" button color should change to dark grey

  @student
  Scenario: Verify student can see tutors offers at the home page
     When the student clicks on the "Find a Tutor" button
     Then the student should see a list of tutors' offers


