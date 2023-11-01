# This will test if the Input Box works as intended
# Written by: David Smedberg

from behave import *
from selenium.webdriver.common.by import By

"""This tests to make sure the input box is empty by default"""

@given(u'The input box is empty')
def input_box_empty(context):
    # test to see if the text box is empty
    assert context.driver.find_element(By.ID, 'test1-input').text == ''

@When(u'The user selects the input box and types in an item')
def select_input_box(context):
    # Selects the text box and types in data
    text = "Schmungus"
    context.driver.find_element(By.ID, 'test1-input').send_keys(text)

@Then(u'The value displayed is the same as the input box')
def check_output(context):
    # Checks output and asserts that the item in the text box is the same as the output
    output_text = context.driver.find_element(By.ID, 'test1-output').text
    input_text = context.driver.find_element(By.ID, 'test1-input').get_attribute("value")
    assert (output_text == input_text), f"error! {input_text}, is not the same as {output_text}"
