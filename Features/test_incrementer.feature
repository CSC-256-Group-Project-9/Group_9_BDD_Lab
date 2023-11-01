# This feature defines the test for the incrementer function. Written by: Owen Cawlfield

Feature: To test the counter function of web app

  Background: Launch the browser and open to the web app page
    Given Launch the Firefox browser
    And Open the browser to the web app

    Scenario: Test the counter by clicking the incrementer button
      Given Value displayed is 0 by default
      When The user click the "click!" button 5 times
      Then The value displayed is "Value: 5"
      When The user clicks the "click!" button in Test 3
      Then The counter resets to 0
      And Close browser
