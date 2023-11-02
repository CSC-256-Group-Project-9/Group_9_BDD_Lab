# This feature defines the test for the navigation bar. Written by: Owen Cawlfield, David Smedberg

Feature:
  Background: Launch the browser and open to the web app page
    Given Launch the Firefox browser
    And Open the browser to the web app

    Scenario: Test the navigation buttons of the web app
      Given User starts on the Testing page of the web app
      When User clicks the API button on the navigation bar
      Then The user sees the API page of the web app

      When User clicks the About Us button on the navigation bar
      Then The user sees the About Us page of the web app

      When User clicks the Contact Us button on the navigation bar
      Then The user sees the Contact Us page of the web app

      When User clicks the Home button on the navigation bar
      Then The user sees the Home page of the web app

      When User clicks the Testing button on the navigation bar
      Then The user is back at the testing page of the web app
      And Close Browser
