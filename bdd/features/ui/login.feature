Feature: Login functionality
  As a user
  I want to login to the application
  So that I can access the secure area

  Scenario: Successful login with valid credentials
    Given user is on login page
    When user logs in with valid credentials
    Then user should see secure area page
