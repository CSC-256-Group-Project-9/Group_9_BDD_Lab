# This feature defines the test for the input box function (Test 1). Written by: David Smedberg

Feature: To test the input box of web app

  Background: Launch the browser and open to the web app page
    Given Launch the Firefox browser
    And Open the browser to the web app

    Scenario: Test the text box by inputting data and checking the output
      Given The input box is empty
      When The user selects the input box and types in an item
      Then The value displayed is the same as the input box
      And Close browser
