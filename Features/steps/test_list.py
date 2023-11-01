# This will test if the List function works
# Written by: Owen Cawlfield

from behave import *
from selenium.webdriver.common.by import By


"""This tests to make sure the displayed list is empty by default"""


@given(u'List is empty by default')
def list_empty(context):
    # test to see if the list displayed is empty
    assert context.driver.find_element(By.XPATH, '//*[@id="list-contents"]').text == ''


"""This finds the text box and enters a string and click the submit button"""


@when(u'The user types something into the input box and presses "click"')
def add_to_list(context):
    text = "Milk and Eggs"
    context.driver.find_element(By.XPATH, '//*[@id="test5-input"]').send_keys(text)  # inputs text
    context.driver.find_element(By.XPATH, '//*[@id="test5-button"]').click()  # clicks the button


"""This tests to see if the list displayed is the same as was entered in the step above"""


@then(u'The user sees the string added to the list below')
def test_list_contents(context):
    text = "Milk and Eggs"
    # checks text in element against "text" variable
    assert context.driver.find_element(By.XPATH, '//*[@id="list-contents"]').text == text


