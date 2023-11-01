# This will test if the counter buttons work
# Written by: Owen Cawlfield

from behave import *
from selenium.webdriver.common.by import By

"""Testing to make sure the value is zero by default on page load"""


@given(u'Value displayed is 0 by default')
def counter_zero(context):
    # Tests if the text value equals 0
    assert context.driver.find_element(By.XPATH, '//*[@id="test2-output"]').text == "0"


@when(u'The user click the "click!" button 5 times')
def click_incrementer(context):
    # clicks the button 5 times
    for i in range(5):
        context.driver.find_element(By.XPATH, '//*[@id="test2-button"]').click()


@then(u'The value displayed is "Value: 5"')
def counter_two(context):
    # tests if the text value equals 5
    assert context.driver.find_element(By.XPATH, '//*[@id="test2-output"]').text == "5"


"""Clicks the button to reset the counter"""


@when(u'The user clicks the "click!" button in Test 3')
def reset_counter(context):
    # clicks the button to reset the counter
    context.driver.find_element(By.XPATH, '//*[@id="test3-button"]').click()


"""Testing to see if the counter reset to 0"""


@then(u'The counter resets to 0')
def counter_zero(context):
    # tests to make sure the reset button reset the counter to 0
    assert context.driver.find_element(By.XPATH, '//*[@id="test2-output"]').text == "0"
