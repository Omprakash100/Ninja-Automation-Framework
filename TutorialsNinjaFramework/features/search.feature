@search
Feature: Search functionality

  Background:
    Given I am on the Home page

  Scenario: Search for a valid product
    When I enter valid product into the Search box field
    And I click on Search button
    Then I should see search results containing valid product only

  Scenario: Search for an invalid product
    When I enter invalid product into the Search box field
    And I click on Search button
    Then I should see a message indicating no search product were found

  Scenario: Search without entering any product
    When I dont enter anything into Search box field
    And I click on Search button
    Then I should see a message indicating no search product were found

  Scenario: Search for products and sorts results
    When I enter valid product into the Search box field
    And I click on Search button
    And sorts the results by price in 'decending' order
    Then the results are sorted by price in 'decending' order