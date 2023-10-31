Feature: To verify radio buttons work on web app

  Background: To launch the browser and open to the web app page
    Given Launch the Firefox browser
    And Open the browser to the web app


  Scenario: To validate radio button selection
    Given radio button 4 is not selected by default
    When The user selects Python radio button and presses submit
    Then The user sees "Favorite Language: Python" is displayed
    And Close Browser


  Scenario: To Validate selection display changed
    Given Radio Button 4 is selected and "Favorite Language: Python" is displayed
    When The user selects Radio Button 1 and presses submit
    Then The user sees ""Favorite Language: JavaScript" is displayed
    And Close Browser