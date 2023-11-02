Feature: Sorting and filtering all offers

  Background:
    Given the site is opened
    And the user is logged in as a Student

  Scenario:
    When I click "Go to categories"
    And I click "Show all offers"
    And I click "Filters"
    And I click "Beginner" level checkbox
    And I click "Apply filters" button
    Then Every offer in the list of filtered offers contains "BEGINNER" label
    And I can see number "1" near "Filters" button
