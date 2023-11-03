Feature: Sorting and filtering all offers

  Background:
    Given the site is opened
    And the user is logged in as a Student

  Scenario: Test filtering by level
    When I click "Go to categories"
    And I click "Show all offers"
    And I click "Filters"
    And I click "Beginner" level checkbox
    And I click "Apply filters" button
    Then Every offer in the list of filtered offers contains "BEGINNER" label
    And I can see number "1" near "Filters" button

  Scenario Outline: Test filtering by name in sidebar
    When I click "Go to categories"
    And I click "Show all offers"
    And I click "Filters"
    And I set <text> in name input field
    And I click "Apply filters" button
    Then All offers contain <text> in name or offer title
    Examples:
    | text   |
    | Ivanna |

  Scenario: Test filtering by rating in sidebar
    When I click "Go to categories"
    And I click "Show all offers"
    And I click "Filters"
    And I click "4 and above" radiobutton
    And I click "Apply filters" button
    Then All offers have rating 4 stars and above
    And I can see number "1" near "Filters" button

  Scenario: Test filtering by language in sidebar
    When I click "Go to categories"
    And I click "Show all offers"
    And I click "Filters"
    And I set language input "Ukrainian"
    And I click "Apply filters" button
    Then All offers have label "Ukrainian"
    And I can see number "1" near "Filters" button