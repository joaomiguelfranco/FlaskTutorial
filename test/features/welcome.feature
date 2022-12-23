Feature: Check all Pages
  Scenario: Retrieve the welcome page
      Given path to server is "http://127.0.0.1:5000/"
      When I call endpoint "/"
      Then I should get an OK


  Scenario: Retrieve the featureA page
      Given path to server is "http://127.0.0.1:5000/"
      When I call endpoint "/featureA/"
      Then I should get an OK
