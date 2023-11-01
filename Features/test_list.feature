# This feature defines the test for the list functon. Written by: Owen Cawlfield
Feature: To verify the list function works

  Background: Launch the browser and open to the web app page
    Given Launch the Firefox browser
    And Open the browser to the web app

    Scenario: To validate the list feature by adding items
      Given List is empty by default
      When The user types something into the input box and presses "click"
      Then The user sees the string added to the list below
      And Close browser