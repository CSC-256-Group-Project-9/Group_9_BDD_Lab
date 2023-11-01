# This feature defines the test for the navigation bar. Written by: Owen Cawlfield
Feature:
  Background: Launch the browser and open to the web app page
    Given Launch the Firefox browser
    And Open the browser to the web app

    Scenario: Test the navigation buttons of the web app
      Given User starts on the testing page of the web app
      When User clicks the Home button on the navigation bar
      Then The user sees the home page of the web app
      And Close Browser