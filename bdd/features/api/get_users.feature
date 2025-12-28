Feature: Get users from API
  Verify users API returns valid response

  Scenario: Get users from reqres API
    When I call get users API
    Then API should return status 200
    And response should contain user data
