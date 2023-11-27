@register
Feature: Register Account functionality

  Background:
    Given I am on the registration page

  Scenario: Register with mandatory fields
    When I enter below details into mandatory fields
        |first_name|last_name|email            |telephone |password|
        |Arun      |Motoori  |newid15@gmail.com|1234567890|12345   |
    And I select Privacy Policy option
    And I click on Continue button
    Then Account should get created

  Scenario: Register with a duplicate existing email
    When I enter details into all fields except email field
        |first_name|last_name|telephone |password |
        |Arun      |Motoori  |1234567890|12345    |
    And I enter existing accounts email "newid2@gmail.com" into email field
    And I select Privacy Policy option
    And I click on Continue button
    Then I should see a warning message for duplicate email

  Scenario: Register without providing any details
    When I dont enter anything into the fields
    And I click on Continue button
    Then Proper warning messages for every mandatory fields should be displayed
