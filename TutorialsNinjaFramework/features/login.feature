@login
Feature: Login Functionality

  Background:
    Given I am on the login page

  Scenario: Login with valid credentials
    When I enter valid email
    And I enter valid password
    And I click the login button
    Then I should be redirected to the account page

  Scenario: Login with invalid username
    When I enter invalid email "user@example.com"
    And I enter valid password
    And I click the login button
    Then I should see an error message
    And I should remain on the login page

  Scenario: Login with invalid password
    When I enter valid email
    And I enter invalid password "invalidpassword"
    And I click the login button
    Then I should see an error message
    And I should remain on the login page

  Scenario: Login without entering any credentials
    When I leave both email and password fields empty
    And I click the login button
    Then I should see an error message
    And I should remain on the login page